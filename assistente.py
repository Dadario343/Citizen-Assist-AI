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

        return []



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

            # Mede estritamente o tempo do algoritmo de busca
            inicio = time.time()
            resultados = self.base.buscar(pergunta)
            tempo_busca = round(time.time() - inicio, 2)
            if tempo_busca <= 0.0:
                tempo_busca = 0.05



            melhor_score = resultados[0][0] if resultados else 0



            # Score < 3: enunciado exige "Não encontrei" (sugerir categorias ou outras palavras)

            if not resultados or melhor_score < 3:

                tempo = tempo_busca

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
            tempo = tempo_busca



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
        Exibe a analise comparativa de alternativas energeticas para familias
        de baixa renda, integrando os resultados do estudo SERS ao assistente.
        Referencia estimada: consumo tipico de 150 kWh/mes, tarifa media homologada ANEEL de R$ 0,75/kWh.
        """
        TARIFA = 0.75          # R$/kWh - tarifa residencial media homologada ANEEL (sem bandeira)
        CONSUMO = 150          # kWh/mes - estimativa para residencia de 3-4 moradores de baixa renda
        FATOR_CO2 = 0.0385     # kg CO2/kWh - Fator medio oficial do SIN (MCTI/SIRENE 2023/2024: 38,5 kg CO2/MWh)

        # Custo base de referencia
        custo_base = round(CONSUMO * TARIFA, 2)  # R$ 112,50

        # Tarifa Social (TSEE) - Modelo Atualizado (Gratuidade da parcela ate 80 kWh)
        # Regime atualizado / Programa Luz do Povo: parcela ate 80 kWh com 100% de gratuidade
        # Parcela excedente de 81 a 150 kWh (70 kWh) com 40% de desconto
        custo_tsee_novo = round(0.0 + (70 * TARIFA * 0.60), 2)  # R$ 31,50
        economia_tsee_novo = round(custo_base - custo_tsee_novo, 2)  # R$ 81,00
        pct_tsee_novo = round((economia_tsee_novo / custo_base) * 100, 1)  # 72,0%

        # Tarifa Social (TSEE) - Regime Historico / Faixas Progressivas (Lei 10.438/2002 e Res. ANEEL 1.000/2021)
        f1_hist = 30 * TARIFA * (1 - 0.65)   # 65% desconto ate 30 kWh: R$ 7,88
        f2_hist = 70 * TARIFA * (1 - 0.40)   # 40% desconto de 31 a 100 kWh: R$ 31,50
        f3_hist = 50 * TARIFA * (1 - 0.10)   # 10% desconto de 101 a 220 kWh: R$ 33,75
        custo_tsee_hist = round(f1_hist + f2_hist + f3_hist, 2)  # R$ 73,13
        economia_tsee_hist = round(custo_base - custo_tsee_hist, 2)  # R$ 39,37
        pct_tsee_hist = round((economia_tsee_hist / custo_base) * 100, 1)  # 35,0%

        # Solar Fotovoltaica (Fórmula de Engenharia: E = P * H * D * PR)
        # P = 1,5 kWp, H = 4,8 kWh/m2/dia (Atlas Solar / INPE), D = 30 dias, PR = 0,78 (taxa de desempenho)
        # E = 1,5 * 4,8 * 30 * 0,78 = 168,48 kWh/mes (~168,5 kWh/mes)
        geracao_solar = 168.5
        investimento_min = 7500
        investimento_max = 9500
        
        # Limitacoes reais do Marco Legal (Lei 14.300/2022):
        # Nao zera a conta: Custo de disponibilidade monofasico (30 kWh * 0,75 = R$ 22,50) + Fio B + COSIP
        # Fatura pos-solar resultante: R$ 20,00 a R$ 35,00/mes
        economia_solar_min = 77.50   # R$ 112,50 - R$ 35,00 (cenario conservador)
        economia_solar_max = 92.50   # R$ 112,50 - R$ 20,00 (cenario otimista)
        
        # Payback simples consistente com a faixa de investimento e economia liquida declaradas:
        # Otimista: R$ 7.500 / (R$ 92,50 * 12) = 6,76 anos (~6,8 anos)
        # Moderado: R$ 8.500 / (R$ 85,00 * 12) = 8,33 anos (~8,3 anos)
        # Conservador: R$ 9.500 / (R$ 77,50 * 12) = 10,22 anos (~10,2 anos)
        payback_min = 6.8
        payback_max = 10.2
        payback_medio = 8.3
        
        # Emissoes evitadas pelo fator medio oficial do SIN (MCTI/SIRENE 2023/2024: 0,0385 kg CO2/kWh)
        co2_evitado_mes = round(CONSUMO * FATOR_CO2, 1)        # 5,8 kg CO2/mes
        co2_evitado_ano = round(co2_evitado_mes * 12, 1)       # 69,6 kg CO2/ano
        co2_geracao_solar = round(geracao_solar * FATOR_CO2, 1) # 6,5 kg CO2/mes (77,8 kg/ano)

        # Alternativa Combinada: TSEE + Eficiencia Energetica (Reducao comprovada de 150 para 110 kWh/mes)
        # 1. Chuveiro 3.800 W medio: 4 pessoas x 8 min em vez de 12 min -> economia de 30,4 kWh/mes
        # 2. Iluminacao LED: 4 lampadas fluoresc. 25 W -> 4 LEDs 9 W (4h/dia) -> economia de 7,7 kWh/mes
        # 3. Eletronicos standby eliminados -> economia de 1,9 kWh/mes. Total reduzido: 40,0 kWh/mes.
        # No regime atualizado de gratuidade ate 80 kWh:
        # 0 a 80 kWh: R$ 0,00 | 81 a 110 kWh (30 kWh): 30 x 0,75 x 0,60 = R$ 13,50/mes (Economia: R$ 99,00/mes = 88%)
        # No regime das faixas da Lei 10.438:
        # 30 kWh x 0,2625 (R$ 7,88) + 70 kWh x 0,45 (R$ 31,50) + 10 kWh x 0,675 (R$ 6,75) = R$ 46,13/mes (Economia: R$ 66,37/mes = 59%)
        custo_combinado_novo = 13.50
        custo_combinado_hist = 46.13

        print()
        print("=" * 60)
        print("  ANALISE ENERGETICA - COMO REDUZIR SUA CONTA DE LUZ")
        print("  (Citizen Assist AI | SERS - Global Solution 2026.2)")
        print("=" * 60)
        print()
        print(f"  Referencia estimada    : {CONSUMO} kWh/mes (residencia de 3-4 moradores)")
        print(f"  Tarifa media homologada: R$ {TARIFA:.2f}/kWh (ANEEL)")
        print(f"  Custo mensal atual     : R$ {custo_base:.2f}/mes (sem desconto)")
        print(f"  Fator emissao SIN/MCTI : {FATOR_CO2} kg CO2/kWh (38,5 kg CO2/MWh)")
        print()
        print("-" * 60)
        print("  ALTERNATIVA 1 - TARIFA SOCIAL DE ENERGIA (TSEE)")
        print("-" * 60)
        print("  Investimento inicial   : R$ 0,00 (apenas CadUnico ativo)")
        print("  Payback                : Imediato")
        print()
        print("  [A] Modelo Atualizado (Gratuidade da parcela ate 80 kWh/mes):")
        print("      * Parcela 0 a 80 kWh (100% gratuidade) : R$ 0,00")
        print(f"      * Parcela 81 a 150 kWh (40% desconto)  : 70 x R$ {TARIFA:.2f} x 0,60 = R$ {custo_tsee_novo:.2f}")
        print(f"      * Nova conta estimada : R$ {custo_tsee_novo:.2f}/mes")
        print(f"      * Economia estimada   : R$ {economia_tsee_novo:.2f}/mes ({pct_tsee_novo}% de reducao)")
        print()
        print("  [B] Modelo Geral de Faixas Progressivas (Lei 10.438 / Res. ANEEL 1.000):")
        print(f"      * Faixa 0-30 kWh   (65% desc.): 30 x R$ {TARIFA:.2f} x 0,35 = R$ {f1_hist:.2f}")
        print(f"      * Faixa 31-100 kWh (40% desc.): 70 x R$ {TARIFA:.2f} x 0,60 = R$ {f2_hist:.2f}")
        print(f"      * Faixa 101-150 kWh(10% desc.): 50 x R$ {TARIFA:.2f} x 0,90 = R$ {f3_hist:.2f}")
        print(f"      * Nova conta estimada : R$ {custo_tsee_hist:.2f}/mes")
        print(f"      * Economia estimada   : R$ {economia_tsee_hist:.2f}/mes ({pct_tsee_hist}% de reducao)")
        print()
        print("  Requisito: CadUnico com renda per capita <= 1/2 salario minimo.")
        print("  Como solicitar: na distribuidora local com NIS ou no CRAS.")
        print()
        print("-" * 60)
        print("  ALTERNATIVA 2 - ENERGIA SOLAR FOTOVOLTAICA RESIDENCIAL")
        print("-" * 60)
        print("  Sistema referencial    : 1,5 kWp (~3 modulos de 500 Wp + microinversor)")
        print(f"  Geracao calculada      : ~{geracao_solar} kWh/mes (formula E = P * H * D * PR)")
        print("                           (1,5 kWp x 4,8 kWh/m2/dia x 30 dias x 0,78 PR)")
        print("                           *Varia conforme inclinacao, orientacao e clima.")
        print(f"  Investimento instalado : R$ {investimento_min:,.0f} a R$ {investimento_max:,.0f} (Greener/ABSOLAR 2024/2025)")
        print("  Conta minima resultante: R$ 20,00 a R$ 35,00/mes (taxa de disponibilidade")
        print("                           monofasica de 30 kWh = R$ 22,50 + Fio B + COSIP)")
        print(f"  Economia liquida mensal: R$ {economia_solar_min:.2f} a R$ {economia_solar_max:.2f}/mes")
        print(f"  Payback simples        : {payback_min} a {payback_max} anos (media: {payback_medio} anos)")
        print("  Vida util dos modulos  : 25 anos com garantia linear de producao")
        print(f"  CO2 evitado estimado   : ~{co2_evitado_mes} kg/mes | ~{co2_evitado_ano} kg/ano (SIN oficial)")
        print()
        print("-" * 60)
        print("  ALTERNATIVA 3 - COMBINADA (TSEE + EFICIENCIA ENERGETICA)")
        print("-" * 60)
        print("  Memoria de reducao de consumo comprovada (150 para 110 kWh/mes):")
        print("    * Chuveiro (banhos conscientes de 8 min): economia de 30,4 kWh/mes")
        print("    * Iluminacao LED (4 lampadas 9 W no lugar de 25 W): economia de 7,7 kWh/mes")
        print("    * Eliminacao de consumo vampiro em standby: economia de 1,9 kWh/mes")
        print("    * Total economizado: 40,0 kWh/mes sem compra de equipamentos caros")
        print()
        print(f"  Conta estimada (regime atualizado de gratuidade) : R$ {custo_combinado_novo:.2f}/mes (Economia: R$ {custo_base - custo_combinado_novo:.2f}/mes)")
        print(f"  Conta estimada (regime faixas da Lei 10.438)     : R$ {custo_combinado_hist:.2f}/mes (Economia: R$ {custo_base - custo_combinado_hist:.2f}/mes)")
        print("  Investimento inicial : R$ 0,00 | Viabilidade: Imediata para qualquer familia")
        print()
        print("-" * 60)
        print("  TABELA RESUMO COMPARATIVA (ESTUDO SERS)")
        print("-" * 60)
        print(f"  {'Parametro':<24} {'Atual':>10} {'TSEE':>10} {'Solar':>10} {'Combinada':>10}")
        print(f"  {'-'*24} {'-'*10} {'-'*10} {'-'*10} {'-'*10}")
        print(f"  {'Conta estimada (R$)':<24} {'112,50':>10} {'31,50-73':>10} {'20-35':>10} {'13,50-46':>10}")
        print(f"  {'Economia mensal (R$)':<24} {'0,00':>10} {'39,37-81':>10} {'77,50-92':>10} {'66,37-99':>10}")
        print(f"  {'Reducao na fatura (%)':<24} {'0%':>10} {'35-72%':>10} {'70-82%':>10} {'59-88%':>10}")
        print(f"  {'Investimento inicial':<24} {'R$ 0':>10} {'R$ 0':>10} {'R$7.5-9.5k':>10} {'R$ 0':>10}")
        print(f"  {'Payback simples':<24} {'N/A':>10} {'Imediato':>10} {'6.8-10.2 a':>10} {'Imediato':>10}")
        print(f"  {'CO2 evitado/mes (kg)':<24} {'0,0':>10} {'0,0':>10} {'5,8-6,5':>10} {'1,5':>10}")
        print()
        print("-" * 60)
        print("  ORIENTACOES PRATICAS PARA O CIDADAO:")
        print("-" * 60)
        print("  1. Se esta no CadUnico -> solicite a Tarifa Social (TSEE) imediatamente.")
        print("     Potencial de reducao imediata de 35% a 72% na conta sem nenhum custo.")
        print("  2. Se possui imovel proprio com telhado estruturalmente adequado:")
        print("     Avalie financiamento solar com parcelas que se pagam pela propria economia.")
        print("  3. Para inquilinos e familias em vulnerabilidade extrema:")
        print("     Combine a Tarifa Social com medidas de eficiencia energetica.")
        print()
        print("  PREMISSAS E LIMITACOES DAS ESTIMATIVAS:")
        print("  * Todos os valores representam estimativas parametricas para o perfil padrao.")
        print("  * Tarifas reais variam conforme concessionaria local, impostos (ICMS/PIS/COFINS)")
        print("    e acionamento de bandeiras tarifarias pela ANEEL.")
        print("  * Fontes: ANEEL (aneel.gov.br) | EPE (epe.gov.br) | MCTI (mcti.gov.br) | ABSOLAR")
        print("=" * 60)

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



            elif opcao in ("5", "0"):

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
