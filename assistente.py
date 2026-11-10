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
        Permite ao usuario digitar uma duvida em linguagem natural,
        busca na base de conhecimento e exibe a orientacao encontrada.
        Retorna '0' se o usuario desejar voltar ao menu principal.
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

            # Verificacao de dados pessoais (LGPD): bloqueia e nao registra
            if self._contem_dado_pessoal(pergunta):
                print()
                print("  [!] Atencao: nao digite CPF, telefone ou e-mail.")
                print("      Reescreva sua pergunta sem dados pessoais.")
                continue

            tentativas += 1
            inicio = time.time()

            # Busca na base de conhecimento
            resultados = self.base.buscar(pergunta)
            tempo = round(time.time() - inicio, 1)
            melhor_score = resultados[0][0] if resultados else 0

            # Score < 3: orientacao nao encontrada
            if not resultados or melhor_score < 3:
                print()
                print("  Nao encontrei uma orientacao especifica para sua duvida.")
                cats = ", ".join(self.base.categorias())
                print(f"  Categorias disponiveis: {cats}")
                print("  Sugestoes:")
                print("   * Tente palavras diferentes (ex: 'tarifa social' em vez de 'desconto luz')")
                print("   * Use a opcao 'categorias' para navegar pelos temas disponiveis")
                print("   * Procure o CRAS mais proximo para orientacao presencial")
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

            # Define nivel de confianca (score >= 3 garantido aqui)
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

            # Exibe ate 2 alternativas adicionais (estritamente com score >= 3)
            alternativas = [alt for alt in resultados[1:3] if alt[0] >= 3]
            if alternativas:
                print("  Outros temas relacionados relevantes:")
                for idx, (sc, alt) in enumerate(alternativas, start=1):
                    print(f"   {idx}. {alt.titulo} [{alt.categoria}] (pontuacao: {sc})")
                print()

            # Pergunta se ajudou (sem incluir o tempo de resposta do usuario no cronometro de busca)
            ajudou = self._perguntar_feedback()

            self.registrar(
                origem="pergunta",
                pergunta=pergunta,
                orientacao_id=melhor.id,
                encontrou=True,
                ajudou=ajudou,
                tentativas=tentativas,
                tempo=tempo
            )

            # Reseta tentativas para a proxima pergunta
            tentativas = 0

            print()
            continuar = self._input_seguro("  Deseja fazer outra pergunta? (s/0 para voltar): ").strip().lower()
            if continuar == "0" or continuar == "n":
                return "0"

    def _perguntar_feedback(self):
        """Pergunta se a orientacao ajudou e retorna True/False com validacao de entrada."""
        while True:
            resp = self._input_seguro("  Essa orientacao respondeu sua duvida? (s/n): ").strip().lower()
            if resp in ("s", "sim", "y", "yes"):
                return True
            if resp in ("n", "nao", "nao", "no"):
                return False
            print("  [!] Por favor, responda com 's' (sim) ou 'n' (nao).")

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
            tempo = round(time.time() - inicio, 1)
            ajudou = self._perguntar_feedback()



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



        # 2. Tempo médio para encontrar (segundos) - Consolidado e Desdobrado
        tempos = [h["tempo_segundos"] for h in encontrados if h["tempo_segundos"] is not None]
        tempo_medio = (sum(tempos) / len(tempos)) if tempos else 0.0

        tempos_busca = [h["tempo_segundos"] for h in encontrados if h.get("origem") == "pergunta" and h["tempo_segundos"] is not None]
        t_busca_medio = (sum(tempos_busca) / len(tempos_busca)) if tempos_busca else 0.0

        tempos_nav = [h["tempo_segundos"] for h in encontrados if h.get("origem") == "categoria" and h["tempo_segundos"] is not None]
        t_nav_medio = (sum(tempos_nav) / len(tempos_nav)) if tempos_nav else 0.0

        # 3. Taxa de acerto: ajudou (%)
        taxa_ajudou = (len(ajudados) / total * 100) if total > 0 else 0

        # 4. Tentativas por atendimento
        tentativas_list = [h["tentativas"] for h in self.historico]
        media_tentativas = (sum(tentativas_list) / len(tentativas_list)) if tentativas_list else 0.0

        print(f"  Total de atendimentos      : {total}")
        print(f"  Resposta encontrada        : {len(encontrados)} ({taxa_encontrada:.1f}%)")
        print(f"  Tempo médio de resposta    : {tempo_medio:.1f}s")
        print(f"    * Busca por pergunta     : {t_busca_medio:.1f}s (algoritmo heurístico puro)")
        print(f"    * Navegação em categoria : {t_nav_medio:.1f}s (renderização em tela)")
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

        # Cabeçalho oficial padronizado com 8 colunas (PCP)
        cabecalho = ["data", "origem", "pergunta", "id_orientacao",
                     "encontrou", "ajudou", "tentativas", "tempo_segundos"]

        try:
            os.makedirs("data", exist_ok=True)
            with open(caminho, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=cabecalho)
                writer.writeheader()
                for entry in self.historico:
                    linha = {k: entry.get(k, "") for k in cabecalho}
                    if not linha["id_orientacao"] and "id" in entry:
                        linha["id_orientacao"] = entry["id"]
                    writer.writerow(linha)

            print(f"  [Info] Atendimentos exportados para: {caminho}")

        except Exception as e:

            print(f"  [Aviso] Não foi possível exportar CSV: {e}")



    # ------------------------------------------------------------------
    # Metodos Estatisticos e Matematicos de Calculo Energetico (SERS)
    # ------------------------------------------------------------------

    @staticmethod
    def _arredondar_moeda(val):
        from decimal import Decimal, ROUND_HALF_UP
        return float(Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

    @staticmethod
    def calcular_tarifa_social_lei10438(consumo, tarifa):
        """
        Calcula a fatura e economia pelo REGIME HISTORICO ANTERIOR da TSEE (Lei Federal nº 10.438/2002):
        Mantido exclusivamente para fins de comparacao retrospectiva com a regra anterior a julho/2025.
          - Faixa 0 a 30 kWh: 65% de desconto
          - Faixa 31 a 100 kWh: 40% de desconto
          - Faixa 101 a 220 kWh: 10% de desconto
          - Acima de 220 kWh: tarifa cheia sem desconto
        """
        from decimal import Decimal
        ar = Assistente._arredondar_moeda
        d_tarifa = Decimal(str(tarifa))
        f1 = ar(Decimal(str(min(consumo, 30))) * d_tarifa * Decimal('0.35'))
        f2 = ar(Decimal(str(max(0, min(consumo - 30, 70)))) * d_tarifa * Decimal('0.60'))
        f3 = ar(Decimal(str(max(0, min(consumo - 100, 120)))) * d_tarifa * Decimal('0.90'))
        f4 = ar(Decimal(str(max(0, consumo - 220))) * d_tarifa)
        total = round(f1 + f2 + f3 + f4, 2)
        base = ar(Decimal(str(consumo)) * d_tarifa)
        economia = round(base - total, 2)
        pct = round((economia / base) * 100, 1) if base > 0 else 0.0
        return total, economia, pct, f1, f2, f3

    @staticmethod
    def calcular_tarifa_social_gratuidade(consumo, tarifa):
        """
        Calcula a fatura e economia pela REGRA ATUAL VIGENTE da TSEE (Lei Federal nº 15.235/2025):
          - Parcela 0 a 80 kWh: 100% de gratuidade (isencao integral de TE e TUSD = R$ 0,00)
          - Excedente acima de 80 kWh: cobranca regular pela tarifa homologada da distribuidora
        """
        f1 = 0.0
        f2 = round(max(0, consumo - 80) * tarifa, 2)
        total = round(f1 + f2, 2)
        base = round(consumo * tarifa, 2)
        economia = round(base - total, 2)
        pct = round((economia / base) * 100, 1) if base > 0 else 0.0
        return total, economia, pct

    @staticmethod
    def calcular_geracao_solar(potencia_kwp, irradiacao_kwh_m2_dia, dias, pr):
        """
        Calcula geracao solar mensal pela formula de engenharia:
        E = P * H * D * PR
        """
        return round(potencia_kwp * irradiacao_kwh_m2_dia * dias * pr, 2)

    @staticmethod
    def calcular_payback(investimento, economia_mensal):
        """Calcula o tempo de retorno simples do investimento em anos."""
        if economia_mensal <= 0:
            return 999.0
        return round(investimento / (economia_mensal * 12), 2)

    @staticmethod
    def calcular_co2(kwh, fator_sin):
        """Calcula emissoes evitadas de CO2 pelo fator oficial do SIN."""
        return round(kwh * fator_sin, 2)

    # ------------------------------------------------------------------
    # Analise Energetica Integrada (SERS)
    # ------------------------------------------------------------------

    def analise_energetica(self):
        """
        Exibe a analise comparativa de alternativas energeticas para familias
        de baixa renda, calculando todas as variaveis dinamicamente.
        Referencia estimada: consumo tipico de 150 kWh/mes, tarifa media ANEEL de R$ 0,75/kWh.
        """
        TARIFA = 0.75          # R$/kWh - tarifa residencial media homologada ANEEL
        CONSUMO = 150          # kWh/mes - estimativa para residencia tipica de baixa renda
        FATOR_CO2 = 0.0385     # kg CO2/kWh - Fator medio oficial do SIN (MCTI/SIRENE 2023/2024: 38,5 kg CO2/MWh)

        # 1. Custo base de referencia sem subsidios
        custo_base = round(CONSUMO * TARIFA, 2)  # R$ 112,50

        # 2. Alternativa 1: Tarifa Social (TSEE)
        # Regime da Lei Federal nº 10.438/2002 e Res. ANEEL 1.000:
        custo_tsee_hist, econ_tsee_hist, pct_tsee_hist, f1, f2, f3 = self.calcular_tarifa_social_lei10438(CONSUMO, TARIFA)
        # Modelo Atualizado (Gratuidade ate 80 kWh com excedente integral a R$ 0,75/kWh):
        custo_tsee_novo, econ_tsee_novo, pct_tsee_novo = self.calcular_tarifa_social_gratuidade(CONSUMO, TARIFA)

        # 3. Alternativa 2: Solar Fotovoltaica (Formula E = P * H * D * PR)
        POTENCIA_KWP = 1.5
        IRRADIACAO = 4.8       # kWh/m2/dia (Atlas Brasileiro de Energia Solar / INPE)
        DIAS = 30
        PR = 0.78              # Performance Ratio (perdas termicas, inversor e poeira)
        geracao_solar = self.calcular_geracao_solar(POTENCIA_KWP, IRRADIACAO, DIAS, PR)

        INV_MIN = 7500
        INV_MED = 8500
        INV_MAX = 9500
        
        # Limitações da Lei 14.300/2022 (taxa mínima monofásica 30 kWh = R$ 22,50 + Fio B + COSIP):
        # Para quem paga a tarifa cheia (R$ 112,50):
        # Custo residual pós-solar: R$ 22,50 (piso monofásico puro de 30 kWh) a R$ 35,00/mês (com Fio B residual e COSIP)
        econ_solar_max = 90.00   # fatura residual mínima de R$ 22,50/mês (R$ 112,50 - R$ 22,50)
        econ_solar_med = 83.75   # fatura residual média de R$ 28,75/mês (R$ 112,50 - R$ 28,75)
        econ_solar_min = 77.50   # fatura residual conservadora de R$ 35,00/mês (R$ 112,50 - R$ 35,00)

        payback_otimista = self.calcular_payback(INV_MIN, econ_solar_max)      # 6.94 anos
        payback_moderado = self.calcular_payback(INV_MED, econ_solar_med)      # 8.46 anos
        payback_conservador = self.calcular_payback(INV_MAX, econ_solar_min)  # 10.22 anos

        co2_evitado_consumo = self.calcular_co2(CONSUMO, FATOR_CO2)
        co2_evitado_solar = self.calcular_co2(geracao_solar, FATOR_CO2)

        # 4. Alternativa 3: Cenario Combinado (TSEE + Eficiencia de 150 para 110 kWh/mes)
        # Auditoria de aparelhos: chuveiro 28 kWh + iluminacao LED 7,68 kWh + standby desligado 4,32 kWh = 40,0 kWh
        CONSUMO_COMBINADO = 110
        custo_comb_hist, _, _, _, _, _ = self.calcular_tarifa_social_lei10438(CONSUMO_COMBINADO, TARIFA)
        custo_comb_novo, _, _ = self.calcular_tarifa_social_gratuidade(CONSUMO_COMBINADO, TARIFA)
        
        # Reducao total consolidada em relacao a fatura inicial de 150 kWh (R$ 112,50):
        econ_comb_hist = round(custo_base - custo_comb_hist, 2)   # R$ 66,37
        pct_comb_hist = round((econ_comb_hist / custo_base) * 100, 1)  # 59,0%
        econ_comb_novo = round(custo_base - custo_comb_novo, 2)   # R$ 90,00
        pct_comb_novo = round((econ_comb_novo / custo_base) * 100, 1)  # 80,0%
        co2_evitado_comb = self.calcular_co2(CONSUMO - CONSUMO_COMBINADO, FATOR_CO2)

        # 5. Comparativo Critico de Viabilidade Solar para Beneficiarios da TSEE:
        # Se a familia ja recebe a Tarifa Social, sua fatura ja e reduzida (R$ 73,13 historico ou R$ 52,50 atual).
        # Apos o solar (fatura minima de R$ 22,50 a R$ 35,00), a economia gerada pelo sistema e drasticamente menor:
        # - Sob a Lei 10.438: economia de R$ 38,13 a R$ 50,63/mes -> Payback medio de 16,0 anos.
        # - Sob a Gratuidade ate 80 kWh: economia de R$ 17,50 a R$ 30,00/mes -> Payback medio de 29,8 anos!
        econ_solar_tsee_hist_otim = round(custo_tsee_hist - 22.50, 2)  # 50.63
        econ_solar_tsee_hist_med = round(custo_tsee_hist - 28.75, 2)   # 44.38
        payback_solar_tsee_hist = self.calcular_payback(INV_MED, econ_solar_tsee_hist_med)  # 16.0 anos

        econ_solar_tsee_novo_otim = round(custo_tsee_novo - 22.50, 2)  # 30.00
        econ_solar_tsee_novo_med = round(custo_tsee_novo - 28.75, 2)   # 23.75
        payback_solar_tsee_novo = self.calcular_payback(INV_MED, econ_solar_tsee_novo_med)   # 29.8 anos

        print()
        print("=" * 60)
        print("  ANALISE ENERGETICA - COMO REDUZIR SUA CONTA DE LUZ")
        print("  (Citizen Assist AI | SERS - Global Solution 2026.2)")
        print("=" * 60)
        print()
        print(f"  Referencia estimada    : {CONSUMO} kWh/mes (residencia de 3-4 moradores)")
        print(f"  Tarifa parametrica     : R$ {TARIFA:.2f}/kWh (premissa de simulacao - Painel ANEEL Subgrupo B1)")
        print(f"                           * Nota: contas reais variam por regiao e incluem impostos (ICMS, PIS/COFINS),")
        print(f"                             bandeiras tarifarias e Contribuicao de Iluminacao Publica (COSIP).")
        print(f"  Custo mensal atual     : R$ {custo_base:.2f}/mes (sem beneficios)")
        print(f"  Fator emissao SIN/MCTI : {FATOR_CO2} kg CO2/kWh (Tabela oficial SIRENE/MCTI ano-base 2023/2024)")
        print()
        print("-" * 60)
        print("  ALTERNATIVA 1 - TARIFA SOCIAL DE ENERGIA (TSEE)")
        print("-" * 60)
        print("  Investimento inicial   : R$ 0,00 (apenas CadUnico ativo)")
        print("  Payback                : Imediato")
        print()
        print("  [A] REGRA ATUAL VIGENTE (Lei Federal nº 15.235/2025 - Gratuidade ate 80 kWh):")
        print("      * Parcela 0 a 80 kWh (100% isencao TE/TUSD) : R$ 0,00 (gratuita)")
        print(f"      * Excedente 81 a 150 kWh (70 kWh regulares) : 70 x R$ {TARIFA:.2f} = R$ {custo_tsee_novo:.2f}")
        print(f"      * Fatura estimada     : R$ {custo_tsee_novo:.2f}/mes")
        print(f"      * Economia estimada   : R$ {econ_tsee_novo:.2f}/mes ({pct_tsee_novo}% de reducao)")
        print("      * Criterios de Elegibilidade Plenos (MME / ANEEL / Lei 12.212):")
        print("        1. CadUnico com renda familiar per capita <= 1/2 salario minimo;")
        print("        2. Idosos (>= 65 anos) ou PCDs beneficiarios do BPC/LOAS;")
        print("        3. CadUnico ate 3 SM com pessoa que necessite de aparelhos eletricos vitais;")
        print("        4. Familias indigenas e quilombolas inscritas no CadUnico.")
        print("      * Modalidade Adicional (Jan/2026 - MME): 'Desconto Social' para CadUnico com renda")
        print("        entre 1/2 e 1 SM, com isencao da CDE para consumo ate 120 kWh/mes (~11,8% de reducao")
        print("        na tarifa media; a isencao de CDE reduz encargos, nao sendo gratuidade total).")
        print("      * Nota metodologica: estimativa simplificada da parcela ativa; faturas reais continuam")
        print("        sujeitas a taxa municipal de iluminacao publica (COSIP).")
        print()
        print("  [B] REGIME HISTORICO ANTERIOR (Lei Federal nº 10.438/2002 - Faixas de Desconto):")
        print(f"      * Faixa 0-30 kWh   (65% desc.): 30 x R$ {TARIFA:.2f} x 0,35 = R$ {f1:.2f}")
        print(f"      * Faixa 31-100 kWh (40% desc.): 70 x R$ {TARIFA:.2f} x 0,60 = R$ {f2:.2f}")
        print(f"      * Faixa 101-150 kWh(10% desc.): 50 x R$ {TARIFA:.2f} x 0,90 = R$ {f3:.2f}")
        print(f"      * Fatura historica    : R$ {custo_tsee_hist:.2f}/mes")
        print(f"      * Economia historica  : R$ {econ_tsee_hist:.2f}/mes ({pct_tsee_hist}% de reducao)")
        print("      * Nota: apresentado exclusivamente para fins de comparacao retrospectiva.")
        print()
        print("-" * 60)
        print("  ALTERNATIVA 2 - ENERGIA SOLAR FOTOVOLTAICA RESIDENCIAL")
        print("-" * 60)
        print("  Sistema referencial    : 1,5 kWp (~3 modulos de 500 Wp + microinversor)")
        print(f"  Geracao calculada      : {geracao_solar:.1f} kWh/mes (formula E = P * H * D * PR)")
        print(f"                           ({POTENCIA_KWP} kWp x {IRRADIACAO} kWh/m2/dia [Atlas INPE Sudeste/Centro-Oeste] x {DIAS}d x {PR} PR)")
        print(f"  Investimento instalado : R$ {INV_MIN:,.0f} a R$ {INV_MAX:,.0f} (Tabela Greener 1S-2024 / ABSOLAR ate 2 kWp)")
        print("  Conta minima residual  : R$ 22,50 a R$ 35,00/mes (taxa de disponibilidade monofasica")
        print("                           de 30 kWh = R$ 22,50 + encargos de Fio B sob Lei 14.300 + COSIP)")
        print(f"  Economia liquida mensal: R$ {econ_solar_min:.2f} a R$ {econ_solar_max:.2f}/mes (68,9% a 80,0% na tarifa cheia)")
        print(f"  Payback simples        : {payback_otimista:.2f} a {payback_conservador:.2f} anos (cenario medio: {payback_moderado:.2f} anos)")
        print(f"  CO2 evitado estimado   : ~{co2_evitado_solar:.1f} kg/mes | ~{co2_evitado_solar*12:.1f} kg/ano (sobre {geracao_solar:.1f} kWh gerados)")
        print()
        print("  [!] AVALIACAO DE VIABILIDADE PARA FAMILIAS COM TARIFA SOCIAL:")
        print(f"  Para quem ja recebe a TSEE Historica (fatura R$ {custo_tsee_hist:.2f}), a economia real")
        print(f"  do solar e de apenas R$ {econ_solar_tsee_hist_otim:.2f}/mes, elevando o payback medio para {payback_solar_tsee_hist:.1f} anos.")
        print(f"  Sob a TSEE Vigente (gratuidade ate 80 kWh, fatura R$ {custo_tsee_novo:.2f}), a economia cai")
        print(f"  para R$ {econ_solar_tsee_novo_otim:.2f}/mes e o payback salta para {payback_solar_tsee_novo:.1f} anos!")
        print("  Conclusao: para familias de baixa renda no CadUnico, a compra de placas")
        print("  proprias e inviavel sem subsidio estatal integral ou cooperativas solares.")
        print()
        print("-" * 60)
        print("  ALTERNATIVA 3 - COMBINADA (TSEE + EFICIENCIA ENERGETICA)")
        print("-" * 60)
        print("  Auditoria de aparelhos para reducao de 40 kWh/mes (150 para 110 kWh/mes):")
        print("    * Chuveiro eletrico 3.500 W (banhos de 8 min em vez de 12 min): -28,00 kWh/mes")
        print("    * Iluminacao LED (4 lampadas 25 W trocadas por 9 W, 4h/dia): -7,68 kWh/mes")
        print("    * Standby desligado (TV + deco 10 W desligados 14,4h/dia no filtro): -4,32 kWh/mes")
        print("    * Total economizado: 40,00 kWh/mes com investimento de R$ 0 a R$ 40 em lampadas")
        print()
        print(f"  Fatura estimada (Lei 10.438) : R$ {custo_comb_hist:.2f}/mes (Economia: R$ {econ_comb_hist:.2f}/mes = {pct_comb_hist}%)")
        print(f"  Fatura estimada (Gratuidade) : R$ {custo_comb_novo:.2f}/mes (Economia: R$ {econ_comb_novo:.2f}/mes = {pct_comb_novo}%)")
        print(f"  CO2 evitado por eficiencia   : ~{co2_evitado_comb:.1f} kg/mes")
        print("  Investimento inicial : R$ 0,00 | Viabilidade: Universal e imediata")
        print()
        print("-" * 60)
        print("  TABELA COMPARATIVA RESUMO (ESTUDO SERS)")
        print("-" * 60)
        print(f"  {'Cenario Analisado':<34} {'Conta (R$)':>12} {'Economia':>12}")
        print(f"  {'-'*34} {'-'*12} {'-'*12}")
        print(f"  {'1. Atual (Tarifa Cheia, 150 kWh)':<34} {'R$ 112,50':>12} {'R$ 0,00':>12}")
        print(f"  {'2. TSEE Vigente (Lei 15.235/2025)':<34} {f'R$ {custo_tsee_novo:.2f}':>12} {f'R$ {econ_tsee_novo:.2f} (53%)':>12}")
        print(f"  {'3. TSEE Historica (Lei 10.438/2002)':<34} {f'R$ {custo_tsee_hist:.2f}':>12} {f'R$ {econ_tsee_hist:.2f} (35%)':>12}")
        print(f"  {'4. Solar 1,5 kWp (Tarifa Cheia)':<34} {'R$ 22.50-35':>12} {'R$ 77.50-90':>12}")
        print(f"  {'5. Combinada Vigente (110 kWh)':<34} {f'R$ {custo_comb_novo:.2f}':>12} {f'R$ {econ_comb_novo:.2f} (80%)':>12}")
        print(f"  {'6. Combinada Historica (110 kWh)':<34} {f'R$ {custo_comb_hist:.2f}':>12} {f'R$ {econ_comb_hist:.2f} (59%)':>12}")
        print()
        print("-" * 60)
        print("  ORIENTACOES PRATICAS PARA O CIDADAO:")
        print("-" * 60)
        print("  1. Se esta no CadUnico -> priorize a Tarifa Social e eficiencia no chuveiro.")
        print("     Reducao imediata de ate 80% na fatura (59% a 80% demonstrados) sem gastar com placas solares.")
        print("  2. Placas solares proprias tem retorno atrativo (6,9 a 10,2 anos) apenas")
        print("     para familias que pagam tarifa cheia (R$ 112,50) e tem imovel proprio.")
        print("=" * 60)

    # ------------------------------------------------------------------
    # Menu principal
    # ------------------------------------------------------------------

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
