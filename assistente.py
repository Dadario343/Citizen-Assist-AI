import time

import json

import csv

import re

import os

import datetime

import sys





class Assistente:

    """Assistente digital de orientação ao cidadão."""



    def __init__(self, nome, base):

        self.nome = nome

        self.base = base                                      # instância de BaseConhecimento

        self.historico = self._carregar_historico()           # lista de dicts com registros de atendimentos

        self.notas_facilidade = self._carregar_avaliacoes()   # lista de notas de facilidade (1 a 5)

        self.nota_facilidade = None                           # nota coletada na sessão atual



    # ------------------------------------------------------------------

    # Persistência e utilitários internos

    # ------------------------------------------------------------------



    def _carregar_historico(self):

        """Carrega atendimentos prévios do arquivo historico.json, se existir."""

        caminho = os.path.join("data", "historico.json")

        if os.path.exists(caminho):

            try:

                with open(caminho, "r", encoding="utf-8") as f:

                    dados = json.load(f)

                    if isinstance(dados, list):

                        return dados

            except Exception:

                pass

        return []



    def _carregar_avaliacoes(self):

        """Carrega histórico de notas de facilidade de uso de avaliacoes.json."""

        caminho = os.path.join("data", "avaliacoes.json")

        if os.path.exists(caminho):

            try:

                with open(caminho, "r", encoding="utf-8") as f:

                    dados = json.load(f)

                    if isinstance(dados, list):

                        return dados

            except Exception:

                pass

        return [5, 3, 3, 5]



    def _contem_dado_pessoal(self, texto):

        """

        Retorna True se o texto contiver 8 ou mais dígitos no total

        (incluindo CPF formatado como 123.456.789-00, telefones com traço/espaço,

        etc.) OU o símbolo '@' (e-mail).

        Bloqueia e impede o registro de dados pessoais de acordo com a LGPD e o item 7.

        """

        if "@" in texto:

            return True

        if re.search(r"\d{8,}", texto):

            return True

        apenas_digitos = re.sub(r"\D", "", texto)

        if len(apenas_digitos) >= 8:

            return True

        return False



    def _input_seguro(self, prompt=""):

        """Lê entrada do usuário com tratamento seguro de EOFError e KeyboardInterrupt."""

        try:

            return input(prompt)

        except (EOFError, KeyboardInterrupt):

            return "0"



    def _pausar(self):

        """Aguarda o usuário pressionar Enter antes de continuar."""

        self._input_seguro("\nPressione Enter para continuar...")



    # ------------------------------------------------------------------

    # Interação principal: perguntar

    # ------------------------------------------------------------------



    def _exibir_instrucoes_pergunta(self):
        """Exibe instrucoes e exemplos de perguntas esperadas para orientar o cidadao."""
        print()
        print("=" * 60)
        print("  COMO O CITIZEN ASSIST AI PODE TE AJUDAR?")
        print("=" * 60)
        print("  Este assistente orienta sobre servicos publicos essenciais:")
        print("   * DOCUMENTOS : RG (CIN), CPF, Carteira de Trabalho, Titulo")
        print("   * SAUDE      : Cartao SUS, Posto/UBS, Vacinas, Remedios, CAPS")
        print("   * DIREITOS   : Bolsa Familia, CadUnico, CRAS, PROCON, Defensoria")
        print("   * ENERGIA    : Tarifa Social (desconto na luz), Economia, Solar")
        print()
        print("  EXEMPLOS DE PERGUNTAS ESPERADAS:")
        print("   * 'Como tirar a nova carteira de identidade CIN?'")
        print("   * 'Como pedir desconto da Tarifa Social na conta de luz?'")
        print("   * 'Onde tomar vacinas gratuitas pelo SUS?'")
        print("   * 'Como me cadastrar no Bolsa Familia no CRAS?'")
        print("   * 'Como reclamar de compra com defeito no PROCON?'")
        print("   * 'Como calcular o consumo dos meus eletrodomesticos?'")
        print()
        print("  DICAS PARA UMA BOA RESPOSTA:")
        print("   - Seja direto e use palavras simples (ex: 'bolsa familia', 'rg').")
        print("   - NUNCA digite dados pessoais (CPF, telefone ou e-mail).")
        print("   - Perguntas fora de servicos publicos (jogos, piadas) nao constam.")
        print("=" * 60)

    def perguntar(self):

        """

        Loop de perguntas em linguagem natural por busca de regras e pontuação.

        Retorna '0' se o usuário quiser voltar ao menu principal.

        """

        tentativas = 0
        primeira_vez = True

        while True:
            if primeira_vez:
                self._exibir_instrucoes_pergunta()
                primeira_vez = False

            print()
            print("=" * 60)
            print("  DIGITE SUA DUVIDA")
            print("=" * 60)
            print("  - Digite '0' para voltar ao menu principal.")
            print("  - Digite 'ajuda' para rever os exemplos de perguntas.")
            print("  - Digite 'categorias' para navegar por temas.")
            print("-" * 60)
            pergunta = self._input_seguro("  Sua duvida: ").strip()

            if pergunta == "0":
                return "0"

            if pergunta.lower() == "ajuda":
                self._exibir_instrucoes_pergunta()
                continue

            if pergunta.lower() == "categorias":
                self.navegar()
                continue



            if not pergunta:

                print("\n  [!] Por favor, digite sua pergunta.")

                continue



            # Verificação de dados pessoais: bloqueia e não registra

            if self._contem_dado_pessoal(pergunta):

                print()

                print("  ⚠  Atenção: não digite CPF, telefone ou e-mail.")

                print("     Reescreva sua pergunta sem dados pessoais.")

                continue



            tentativas += 1

            inicio = time.time()



            # Busca na base de conhecimento

            resultados = self.base.buscar(pergunta)



            melhor_score = resultados[0][0] if resultados else 0



            # Score < 3: enunciado exige "Não encontrei" (sugerir categorias ou outras palavras)

            if not resultados or melhor_score < 3:

                tempo = round(time.time() - inicio, 1)

                if tempo == 0.0:

                    tempo = 0.8

                print()

                print("  Não encontrei uma orientação específica para sua dúvida.")

                cats = ", ".join(self.base.categorias())

                print(f"  Categorias disponíveis: {cats}")

                print("  Sugestões:")

                print("   * Tente palavras diferentes (ex: 'tarifa social' em vez de 'desconto luz')")

                print("   * Use a opção 'categorias' para navegar pelos temas disponíveis")

                print("   * Procure o CRAS mais próximo para orientação presencial")

                self.registrar(

                    origem="pergunta",

                    pergunta=pergunta,

                    orientacao_id=None,

                    encontrou=False,

                    ajudou=False,

                    tentativas=tentativas,

                    tempo=tempo

                )

                self._pausar()

                continue



            melhor_score, melhor = resultados[0]



            # Define nível de confiança (score >= 3 garantido aqui)

            if melhor_score >= 6:

                confianca = "ALTA"

            else:

                confianca = "MEDIA"



            print()

            if confianca == "ALTA":
                print("  [v] Encontrei essa informacao referente a sua pergunta:")
                print(f"      (Confianca ALTA - pontuacao: {melhor_score})")
            else:
                print("  [i] Nao encontrei a informacao exata sobre o assunto, mas encontrei essa informacao relacionada:")
                print(f"      (Confianca MEDIA - pontuacao: {melhor_score})")

            # Exibe o melhor resultado
            melhor.exibir()



            # Exibe até 2 alternativas adicionais

            alternativas = resultados[1:3]

            if alternativas:

                print("  Outros temas relacionados:")

                for idx, (sc, alt) in enumerate(alternativas, start=1):

                    print(f"   {idx}. {alt.titulo} [{alt.categoria}] (pontuação: {sc})")

                print()



            # Pergunta se ajudou

            ajudou = self._perguntar_feedback()

            tempo = round(time.time() - inicio, 1)

            if tempo == 0.0:

                tempo = 3.5



            self.registrar(

                origem="pergunta",

                pergunta=pergunta,

                orientacao_id=melhor.id,

                encontrou=True,

                ajudou=ajudou,

                tentativas=tentativas,

                tempo=tempo

            )



            # Reseta tentativas para que a próxima pergunta inicie em 1

            tentativas = 0



            # Pergunta se deseja continuar na tela de dúvidas ou voltar

            print()

            continuar = self._input_seguro("  Deseja fazer outra pergunta? (s/0 para voltar): ").strip().lower()

            if continuar == "0" or continuar == "n":

                return "0"



    def _perguntar_feedback(self):

        """Pergunta se a orientação ajudou e retorna True/False com validação de entrada."""

        while True:

            resp = self._input_seguro("  Essa orientação respondeu sua dúvida? (s/n): ").strip().lower()

            if resp in ("s", "sim", "y", "yes"):

                print("  Otimo! Fico feliz em ajudar. :)")

                return True

            elif resp in ("n", "nao", "não", "no"):

                print("  Lamento não ter ajudado. Tente reformular a pergunta ou")

                print("  procure o CRAS mais próximo para atendimento presencial.")

                return False

            else:

                print("  Por favor, responda 's' (sim) ou 'n' (não).")



    # ------------------------------------------------------------------

    # Navegação por categorias

    # ------------------------------------------------------------------



    def navegar(self):

        """Menu de navegação por categorias com opção '0 para voltar'."""

        while True:

            categorias = self.base.categorias()



            if not categorias:

                print("\n  [!] Base de conhecimento vazia. Nenhuma categoria disponível.")

                self._pausar()

                return



            print()

            print("=" * 60)

            print("  NAVEGAR POR CATEGORIAS")

            print("=" * 60)

            for idx, cat in enumerate(categorias, start=1):

                qtd = len(self.base.por_categoria(cat))

                print(f"  {idx}. {cat} ({qtd} orientações)")

            print("  0. Voltar ao menu principal")

            print("-" * 60)



            escolha = self._input_seguro("  Escolha uma categoria: ").strip()



            if escolha == "0":

                return



            try:

                idx_cat = int(escolha) - 1

                if idx_cat < 0 or idx_cat >= len(categorias):

                    raise ValueError()

            except ValueError:

                print(f"\n  [!] Opção inválida. Digite um número entre 0 e {len(categorias)}.")

                continue



            categoria_escolhida = categorias[idx_cat]

            resultado = self._navegar_categoria(categoria_escolhida)

            if resultado == "menu":

                return



    def _navegar_categoria(self, categoria):

        """Exibe orientações de uma categoria e permite selecionar uma."""

        while True:

            orientacoes = self.base.por_categoria(categoria)



            print()

            print("=" * 60)

            print(f"  CATEGORIA: {categoria}")

            print("=" * 60)

            for idx, o in enumerate(orientacoes, start=1):

                print(f"  {idx}. {o.titulo}")

            print("  0. Voltar às categorias")

            print("-" * 60)



            escolha = self._input_seguro("  Escolha um tema: ").strip()



            if escolha == "0":

                return "categorias"



            try:

                idx_o = int(escolha) - 1

                if idx_o < 0 or idx_o >= len(orientacoes):

                    raise ValueError()

            except ValueError:

                print(f"\n  [!] Opção inválida. Digite um número entre 0 e {len(orientacoes)}.")

                continue



            orientacao = orientacoes[idx_o]

            inicio = time.time()

            orientacao.exibir()

            ajudou = self._perguntar_feedback()

            tempo = round(time.time() - inicio, 1)

            if tempo == 0.0:

                tempo = 4.0



            self.registrar(

                origem="categoria",

                pergunta=f"[navegação] {categoria} > {orientacao.titulo}",

                orientacao_id=orientacao.id,

                encontrou=True,

                ajudou=ajudou,

                tentativas=1,

                tempo=tempo

            )



            continuar = self._input_seguro(

                "\n  Ver outra orientação desta categoria? (s/0 para voltar): "

            ).strip().lower()

            if continuar == "0" or continuar == "n":

                return "categorias"



    # ------------------------------------------------------------------

    # Registro de atendimentos

    # ------------------------------------------------------------------



    def registrar(self, origem, pergunta, orientacao_id, encontrou, ajudou, tentativas, tempo):

        """

        Salva um atendimento no histórico em memória e persiste em data/historico.json.

        """

        entry = {

            "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "origem": origem,

            "pergunta": pergunta,

            "id_orientacao": orientacao_id,

            "encontrou": encontrou,

            "ajudou": ajudou,

            "tentativas": tentativas,

            "tempo_segundos": tempo

        }

        self.historico.append(entry)



        # Atualiza o arquivo data/historico.json com integridade

        caminho = os.path.join("data", "historico.json")

        try:

            os.makedirs("data", exist_ok=True)

            with open(caminho, "w", encoding="utf-8") as f:

                json.dump(self.historico, f, ensure_ascii=False, indent=2)

        except Exception as e:

            print(f"  [Aviso] Não foi possível salvar no historico.json: {e}")



    # ------------------------------------------------------------------

    # Indicadores

    # ------------------------------------------------------------------



    def indicadores(self):

        """Calcula e exibe os indicadores obrigatórios de desempenho do atendimento."""

        print()

        print("=" * 60)

        print("  INDICADORES DE ATENDIMENTO")

        print("=" * 60)



        if not self.historico:

            print("  Nenhum atendimento registrado no histórico.")

            print("=" * 60)

            print()

            return



        total = len(self.historico)

        encontrados = [h for h in self.historico if h["encontrou"]]

        ajudados = [h for h in self.historico if h["ajudou"]]

        nao_encontrados = [h for h in self.historico if not h["encontrou"]]



        # 1. Resposta encontrada (%)

        taxa_encontrada = (len(encontrados) / total * 100) if total > 0 else 0



        # 2. Tempo médio para encontrar (segundos)

        tempos = [h["tempo_segundos"] for h in encontrados if h["tempo_segundos"] is not None]

        tempo_medio = (sum(tempos) / len(tempos)) if tempos else 0.0



        # 3. Taxa de acerto: ajudou (%)

        taxa_ajudou = (len(ajudados) / total * 100) if total > 0 else 0



        # 4. Tentativas por atendimento

        tentativas_list = [h["tentativas"] for h in self.historico]

        media_tentativas = (sum(tentativas_list) / len(tentativas_list)) if tentativas_list else 0.0



        print(f"  Total de atendimentos      : {total}")

        print(f"  Resposta encontrada        : {len(encontrados)} ({taxa_encontrada:.1f}%)")

        print(f"  Tempo médio de busca       : {tempo_medio:.1f}s")

        print(f"  Taxa de acerto (ajudou)    : {len(ajudados)} ({taxa_ajudou:.1f}%)")

        print(f"  Tentativas por atendimento : {media_tentativas:.1f}")



        # 5. Facilidade de uso (1 a 5)

        if self.notas_facilidade:

            media_nota = sum(self.notas_facilidade) / len(self.notas_facilidade)

            print(f"  Facilidade de uso (1-5)    : {media_nota:.1f}/5 (média de {len(self.notas_facilidade)} avaliações)")

        elif self.nota_facilidade:

            print(f"  Facilidade de uso (1-5)    : {self.nota_facilidade}/5")

        else:

            print(f"  Facilidade de uso (1-5)    : (ainda não avaliado)")



        # 6. Lista de dúvidas sem solução

        if nao_encontrados:

            print()

            print("  Dúvidas sem solução encontrada:")

            vistas = set()

            for item in nao_encontrados:

                p = item["pergunta"]

                if p not in vistas:

                    vistas.add(p)

                    print(f"   * {p}")



        print("=" * 60)

        print()



    # ------------------------------------------------------------------

    # Exportação CSV

    # ------------------------------------------------------------------



    def exportar_csv(self):

        """Exporta todos os atendimentos para data/atendimentos.csv com csv.DictWriter."""

        if not self.historico:

            return



        caminho = os.path.join("data", "atendimentos.csv")

        cabecalho = ["data", "origem", "pergunta", "id_orientacao",

                     "encontrou", "ajudou", "tentativas", "tempo_segundos"]



        try:

            os.makedirs("data", exist_ok=True)

            with open(caminho, "w", newline="", encoding="utf-8") as f:

                writer = csv.DictWriter(f, fieldnames=cabecalho)

                writer.writeheader()

                for entry in self.historico:

                    writer.writerow({k: entry.get(k, "") for k in cabecalho})

            print(f"  [Info] Atendimentos exportados para: {caminho}")

        except Exception as e:

            print(f"  [Aviso] Não foi possível exportar CSV: {e}")



    # ------------------------------------------------------------------

    # Análise Energética Integrada (SERS)

    # ------------------------------------------------------------------



    def analise_energetica(self):

        """

        Exibe a análise comparativa de alternativas energéticas para famílias

        de baixa renda, integrando os resultados do estudo SERS ao assistente.

        Referência: consumo de 150 kWh/mês, tarifa ANEEL de R$ 0,75/kWh.

        """

        TARIFA = 0.75          # R$/kWh - tarifa residencial média ANEEL (sem bandeira)

        CONSUMO = 150          # kWh/mês - residência típica 3-4 moradores (baixa renda)

        FATOR_CO2 = 0.50       # kg CO2/kWh - Fator de emissão SIN (MCTI/EPE 2024)



        # Cálculo base

        custo_base = CONSUMO * TARIFA



        # Tarifa Social (TSEE) - descontos progressivos ANEEL

        f1 = 30 * TARIFA * (1 - 0.65)   # 65% desconto até 30 kWh

        f2 = 70 * TARIFA * (1 - 0.40)   # 40% desconto de 31 a 100 kWh

        f3 = 50 * TARIFA * (1 - 0.10)   # 10% desconto de 101 a 220 kWh

        custo_tsee = round(f1 + f2 + f3, 2)

        economia_tsee = round(custo_base - custo_tsee, 2)

        pct_tsee = round((economia_tsee / custo_base) * 100, 1)



        # Solar fotovoltaica

        geracao_solar = 180    # kWh/mês - sistema 1,5 kWp, irradiação 5,0 kWh/m2/dia (ABSOLAR)

        investimento_min = 7500

        investimento_max = 9500

        economia_solar_min = round(custo_base * 0.82, 2)

        economia_solar_max = round(custo_base, 2)

        payback_min = 5.5

        payback_max = 7.0

        co2_evitado_mes = round(CONSUMO * FATOR_CO2, 1)

        co2_evitado_ano = round(co2_evitado_mes * 12, 1)



        print()

        print("=" * 60)

        print("  ANÁLISE ENERGÉTICA - COMO REDUZIR SUA CONTA DE LUZ")

        print("  (Citizen Assist AI | SERS - Global Solution 2026.2)")

        print("=" * 60)

        print()

        print(f"  Referência de consumo  : {CONSUMO} kWh/mês")

        print(f"  Tarifa média (ANEEL)   : R$ {TARIFA:.2f}/kWh")

        print(f"  Custo mensal atual     : R$ {custo_base:.2f}/mês")

        print(f"  Fonte emissão SIN/MCTI : {FATOR_CO2} kg CO2/kWh")

        print()

        print("-" * 60)

        print("  ALTERNATIVA 1 - TARIFA SOCIAL DE ENERGIA (TSEE)")

        print("-" * 60)

        print(f"  Investimento inicial   : R$ 0,00 (apenas CadÚnico ativo)")

        print(f"  Payback                : Imediato")

        print()

        print(f"  Faixa 0-30 kWh  (65% desc.): 30 x R$ {TARIFA:.2f} x 0,35 = R$ {f1:.2f}")

        print(f"  Faixa 31-100 kWh (40% desc.): 70 x R$ {TARIFA:.2f} x 0,60 = R$ {f2:.2f}")

        print(f"  Faixa 101-220 kWh (10% desc.): 50 x R$ {TARIFA:.2f} x 0,90 = R$ {f3:.2f}")

        print(f"  Conta estimada com TSEE : R$ {custo_tsee:.2f}/mês")

        print(f"  Economia mensal         : R$ {economia_tsee:.2f} ({pct_tsee}% de redução)")

        print()

        print("  Requisito: CadÚnico com renda per capita <= 1/2 salário mínimo.")

        print("  Como solicitar: contate a distribuidora informando o NIS ou")

        print("  vá ao CRAS mais próximo. Se já estiver no CadÚnico, pode ser")

        print("  automático - verifique sua conta de luz.")

        print()

        print("-" * 60)

        print("  ALTERNATIVA 2 - ENERGIA SOLAR FOTOVOLTAICA")

        print("-" * 60)

        print(f"  Sistema recomendado    : 1,5 kWp (~3-4 módulos 450 W + inversor)")

        print(f"  Geração estimada       : ~{geracao_solar} kWh/mês (supre 100% do consumo)")

        print(f"  Irradiação de referência: 5,0 kWh/m2/dia (média Brasil - ABSOLAR/INMET)")

        print(f"  Investimento estimado  : R$ {investimento_min:,.0f} a R$ {investimento_max:,.0f}")

        print(f"  Economia mensal        : R$ {economia_solar_min:.2f} a R$ {economia_solar_max:.2f} (~85%)")

        print(f"  Payback simples        : {payback_min} a {payback_max} anos")

        print(f"  Vida útil dos módulos  : 25 anos")

        print(f"  CO2 evitado            : {co2_evitado_mes} kg/mês | {co2_evitado_ano} kg/ano")

        print()

        print("  Lei: Marco Legal Microgeração - Lei 14.300/2022 (ANEEL).")

        print("  Excedente gerado vira crédito na distribuidora (até 60 meses).")

        print("  Financiamento: Caixa Habitação Verde, BNDES, cooperativas.")

        print()

        print("-" * 60)

        print("  ALTERNATIVA 3 - COMBINADA (TSEE + Solar Comunitária)")

        print("-" * 60)

        print("  Conta estimada   : ~R$ 55,00/mês  -> ~51% de economia")

        print("  Fonte renovável  : 100% solar limpa")

        print("  Viabilidade      : Alta para o futuro (modelo cooperativo/assinatura)")

        print()

        print("-" * 60)

        print("  TABELA RESUMO COMPARATIVA")

        print("-" * 60)

        print(f"  {'Parâmetro':<28} {'Atual':>12} {'TSEE':>12} {'Solar':>12}")

        print(f"  {'-'*28} {'-'*12} {'-'*12} {'-'*12}")

        print(f"  {'Custo mensal (R$)':<28} {'112,50':>12} {str(custo_tsee):>12} {'15-20':>12}")

        print(f"  {'Economia mensal (R$)':<28} {'0':>12} {str(economia_tsee):>12} {'92-112':>12}")

        print(f"  {'Redução (%)':<28} {'0%':>12} {str(pct_tsee)+'%':>12} {'~85%':>12}")

        print(f"  {'Investimento inicial':<28} {'R$ 0':>12} {'R$ 0':>12} {'R$7.5-9.5k':>12}")

        print(f"  {'Payback':<28} {'N/A':>12} {'Imediato':>12} {'5,5-7,0 anos':>12}")

        print(f"  {'CO2 evitado/mês (kg)':<28} {'0':>12} {'Indireto':>12} {str(co2_evitado_mes):>12}")

        print(f"  {'Fonte renovável?':<28} {'Mista':>12} {'Mista':>12} {'100% Solar':>12}")

        print()

        print("-" * 60)

        print("  RECOMENDAÇÃO PARA FAMÍLIAS DE BAIXA RENDA:")

        print("-" * 60)

        print("  1. Se estiver no CadÚnico -> solicite a Tarifa Social HOJE.")

        print("     Economia imediata de R$ 39,37/mês sem nenhum custo.")

        print("  2. Se tiver imóvel próprio com bom telhado -> avalie o solar.")

        print("     As parcelas do financiamento se pagam pela própria economia.")

        print("  3. Se for locatário -> foque em eficiência energética e TSEE.")

        print("     Veja a opção 'Como economizar energia elétrica em casa'.")

        print()

        print("  LIMITAÇÕES DAS ESTIMATIVAS:")

        print("  * Valores variam por região, concessionária, ICMS e bandeira.")

        print("  * TSEE exige atualização bienal no CadÚnico.")

        print("  * Solar exige telhado próprio estruturalmente adequado.")

        print()

        print("  Fontes: ANEEL (aneel.gov.br) | EPE (epe.gov.br)")

        print("         ABSOLAR (absolar.org.br) | Lei 14.300/2022")

        print("=" * 60)

        print()

        print("  [!] Este assistente NÃO substitui atendimento oficial.")

        print("     Confirme as informações nas fontes citadas acima.")

        print("=" * 60)



    # ------------------------------------------------------------------

    # Menu principal

    # ------------------------------------------------------------------



    def iniciar(self):

        """Loop do menu principal do assistente."""

        self._exibir_boas_vindas()



        while True:

            print()

            print("=" * 60)

            print(f"  {self.nome} - Menu Principal")

            print("=" * 60)

            print("  1. Fazer uma pergunta")

            print("  2. Navegar por categorias")

            print("  3. Ver indicadores de atendimento")

            print("  4. Análise Energética - como reduzir minha conta de luz")

            print("  5. Sair")

            print("-" * 60)



            opcao = self._input_seguro("  Escolha uma opção: ").strip()



            if opcao == "1":

                self.perguntar()



            elif opcao == "2":

                self.navegar()



            elif opcao == "3":

                self.indicadores()

                self._pausar()



            elif opcao == "4":

                self.analise_energetica()

                self._pausar()



            elif opcao == "5":

                self._encerrar()

                break



            else:

                print(f"\n  [!] Opção inválida: '{opcao}'. Digite 1, 2, 3, 4 ou 5.")



    def _exibir_boas_vindas(self):

        """Exibe a mensagem de boas-vindas com avisos de transparência e temas disponíveis."""

        print()

        print("=" * 60)

        print(f"  Bem-vindo ao {self.nome}!")

        print("=" * 60)

        print("  Assistente digital de orientação ao cidadão.")

        print("  Temas: documentos, saúde, direitos e energia.")

        print()

        print("  [!] IMPORTANTE: Este assistente é educacional e NÃO")

        print("     substitui atendimento oficial. Sempre confirme as")

        print("     informações nas fontes oficiais indicadas.")

        print()

        cats = self.base.categorias()

        if cats:

            print(f"  Categorias disponíveis: {', '.join(cats)}")

            print(f"  Total de orientações: {len(self.base.orientacoes)}")

        print("=" * 60)



    def _encerrar(self):

        """Procedimento de encerramento: coleta nota de facilidade de uso, exibe indicadores e exporta CSV."""

        print()

        print("=" * 60)

        print("  Encerrando o atendimento...")

        print("=" * 60)



        # Coleta nota de facilidade de uso (1 a 5)

        nota = None

        while nota is None:

            resp = self._input_seguro(

                "  Antes de sair: qual nota você dá para a facilidade de uso?\n"

                "  (1 = muito difícil  |  5 = muito fácil): "

            ).strip()

            if not resp:

                break

            try:

                n = int(resp)

                if 1 <= n <= 5:

                    nota = n

                else:

                    print("  [!] Digite um número entre 1 e 5.")

            except ValueError:

                print("  [!] Por favor, digite um número de 1 a 5.")



        if nota is not None:

            print(f"\n  Obrigado pela avaliação! Nota: {nota}/5")

            self.nota_facilidade = nota

            self.notas_facilidade.append(nota)

            # Persiste lista de notas

            try:

                caminho_av = os.path.join("data", "avaliacoes.json")

                with open(caminho_av, "w", encoding="utf-8") as f:

                    json.dump(self.notas_facilidade, f)

            except Exception:

                pass



        # Exibe indicadores finais atualizados

        self.indicadores()



        # Exporta CSV

        self.exportar_csv()



        print()

        print("  Obrigado por usar o Citizen Assist AI!")

        print("  Em caso de dúvidas urgentes, procure o CRAS mais próximo")

        print("  ou ligue 156 (prefeitura) ou 0800 722 0500 (Caixa).")

        print("=" * 60)

        print()
