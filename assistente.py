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
        self.base = base          # instância de BaseConhecimento
        self.historico = []       # lista de dicts com registros de atendimentos

    # ------------------------------------------------------------------
    # Utilitários internos
    # ------------------------------------------------------------------

    def _contem_dado_pessoal(self, texto):
        """
        Retorna True se o texto contiver 8 ou mais dígitos no total
        (incluindo CPF formatado como 123.456.789-00, telefones com traço/espaço,
        etc.) OU o símbolo '@' (e-mail).
        A verificação remove pontuação antes de contar os dígitos para detectar
        formatos como XXX.XXX.XXX-XX ou (XX) XXXXX-XXXX.
        """
        if "@" in texto:
            return True
        # Verifica sequência consecutiva de 8+ dígitos (sem formatação)
        if re.search(r"\d{8,}", texto):
            return True
        # Remove tudo que não é dígito e verifica se sobram 8+ dígitos no total
        # (captura CPF, CNPJ e telefones formatados com pontos, traços e espaços)
        apenas_digitos = re.sub(r"\D", "", texto)
        if len(apenas_digitos) >= 8:
            return True
        return False

    def _input_seguro(self, prompt=""):
        """Lê entrada do usuário com tratamento básico de EOFError."""
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

    def perguntar(self):
        """
        Loop de perguntas em linguagem natural.
        Retorna '0' se o usuário quiser voltar ao menu principal.
        """
        tentativas = 0

        while True:
            print()
            print("=" * 60)
            print("  FAZER UMA PERGUNTA")
            print("=" * 60)
            print("  Digite '0' para voltar ao menu principal.")
            print("  Digite 'categorias' para navegar por categorias.")
            print("-" * 60)
            pergunta = self._input_seguro("  Sua dúvida: ").strip()

            if pergunta == "0":
                return "0"

            if pergunta.lower() == "categorias":
                self.navegar()
                continue

            if not pergunta:
                print("\n  [!] Por favor, digite sua pergunta.")
                continue

            # Verificação de dados pessoais
            if self._contem_dado_pessoal(pergunta):
                print()
                print("  ⚠  Atenção: não digite CPF, telefone ou e-mail.")
                print("     Reescreva sua pergunta sem dados pessoais.")
                continue

            tentativas += 1
            inicio = time.time()

            # Busca na base de conhecimento
            resultados = self.base.buscar(pergunta)

            tempo = round(time.time() - inicio, 2)

            melhor_score = resultados[0][0] if resultados else 0

            # Score < 3: enunciado exige "Não encontrei" (igual a nenhum resultado)
            if not resultados or melhor_score < 3:
                print()
                print("  Não encontrei uma orientação específica para sua dúvida.")
                cats = ", ".join(self.base.categorias())
                print(f"  Categorias disponíveis: {cats}")
                print("  Sugestões:")
                print("   • Tente palavras diferentes (ex: 'tarifa social' em vez de 'desconto luz')")
                print("   • Use a opção 'categorias' para navegar pelos temas disponíveis")
                print("   • Procure o CRAS mais próximo para orientação presencial")
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
            print(f"  [{'v' if confianca == 'ALTA' else '~'}] Confiança da resposta: {confianca} (pontuação: {melhor_score})")

            # Exibe o melhor resultado
            melhor.exibir()

            # Exibe até 2 alternativas
            alternativas = resultados[1:3]
            if alternativas:
                print("  Outros temas relacionados:")
                for idx, (sc, alt) in enumerate(alternativas, start=1):
                    print(f"   {idx}. {alt.titulo} [{alt.categoria}] (pontuação: {sc})")
                print()

            # Pergunta se ajudou
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

            # Após feedback, pergunta se quer continuar ou voltar
            print()
            continuar = self._input_seguro("  Deseja fazer outra pergunta? (s/0 para voltar): ").strip().lower()
            if continuar == "0" or continuar == "n":
                return "0"
            # Caso contrário, continua o loop

    def _perguntar_feedback(self):
        """Pergunta se a orientação ajudou e retorna True/False."""
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
        """Menu de navegação por categorias e orientações."""
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
            tempo = round(time.time() - inicio, 2)

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
        Salva um atendimento no histórico em memória e no arquivo historico.json.
        Carrega entradas existentes antes de acrescentar para não sobrescrever.
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

        # Atualiza o arquivo historico.json de forma segura
        caminho = os.path.join("data", "historico.json")
        existentes = []
        if os.path.exists(caminho):
            try:
                with open(caminho, "r", encoding="utf-8") as f:
                    existentes = json.load(f)
                if not isinstance(existentes, list):
                    existentes = []
            except Exception:
                existentes = []

        existentes.append(entry)

        try:
            os.makedirs("data", exist_ok=True)
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(existentes, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"  [Aviso] Não foi possível salvar no historico.json: {e}")

    # ------------------------------------------------------------------
    # Indicadores
    # ------------------------------------------------------------------

    def indicadores(self):
        """Calcula e exibe os indicadores de desempenho do atendimento."""
        print()
        print("=" * 60)
        print("  INDICADORES DE ATENDIMENTO")
        print("=" * 60)

        if not self.historico:
            print("  Nenhum atendimento registrado nesta sessão.")
            print()
            return

        total = len(self.historico)
        encontrados = [h for h in self.historico if h["encontrou"]]
        ajudados = [h for h in self.historico if h["ajudou"]]
        nao_encontrados = [h for h in self.historico if not h["encontrou"]]

        # Taxa de resposta encontrada
        taxa_encontrada = (len(encontrados) / total * 100) if total > 0 else 0
        # Tempo médio (apenas dos que encontraram resposta)
        tempos = [h["tempo_segundos"] for h in encontrados if h["tempo_segundos"] is not None]
        tempo_medio = (sum(tempos) / len(tempos)) if tempos else 0
        # Taxa de acerto (ajudou)
        taxa_ajudou = (len(ajudados) / total * 100) if total > 0 else 0
        # Tentativas médias
        tentativas_list = [h["tentativas"] for h in self.historico]
        media_tentativas = (sum(tentativas_list) / len(tentativas_list)) if tentativas_list else 0

        print(f"  Total de atendimentos      : {total}")
        print(f"  Resposta encontrada        : {len(encontrados)} ({taxa_encontrada:.1f}%)")
        print(f"  Tempo médio de busca       : {tempo_medio:.2f}s")
        print(f"  Taxa de acerto (ajudou)    : {len(ajudados)} ({taxa_ajudou:.1f}%)")
        print(f"  Tentativas por atendimento : {media_tentativas:.1f}")

        # Facilidade de uso (coletada no encerramento)
        nota = getattr(self, "nota_facilidade", None)
        if nota is not None and nota > 0:
            print(f"  Facilidade de uso (1-5)    : {nota}/5")
        else:
            print(f"  Facilidade de uso (1-5)    : (ainda não avaliado)")

        if nao_encontrados:
            print()
            print("  Dúvidas sem solução encontrada:")
            for item in nao_encontrados:
                print(f"   • {item['pergunta']}")

        print("=" * 60)
        print()

    # ------------------------------------------------------------------
    # Exportação CSV
    # ------------------------------------------------------------------

    def exportar_csv(self):
        """Exporta o histórico da sessão para data/atendimentos.csv."""
        if not self.historico:
            return

        caminho = os.path.join("data", "atendimentos.csv")
        cabecalho = ["data", "origem", "pergunta", "id_orientacao",
                     "encontrou", "ajudou", "tentativas", "tempo_segundos"]

        # Verifica se o arquivo já existe para saber se deve escrever cabeçalho
        arquivo_existe = os.path.exists(caminho) and os.path.getsize(caminho) > 0

        try:
            os.makedirs("data", exist_ok=True)
            with open(caminho, "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=cabecalho)
                if not arquivo_existe:
                    writer.writeheader()
                for entry in self.historico:
                    writer.writerow({k: entry.get(k, "") for k in cabecalho})
            print(f"  [Info] Atendimentos exportados para: {caminho}")
        except Exception as e:
            print(f"  [Aviso] Não foi possível exportar CSV: {e}")

    # ------------------------------------------------------------------
    # Menu principal
    # ------------------------------------------------------------------

    def iniciar(self):
        """Loop do menu principal do assistente."""
        self.nota_facilidade = None  # armazenada no encerramento
        self._exibir_boas_vindas()

        while True:
            print()
            print("=" * 60)
            print(f"  {self.nome} - Menu Principal")
            print("=" * 60)
            print("  1. Fazer uma pergunta")
            print("  2. Navegar por categorias")
            print("  3. Ver indicadores de atendimento")
            print("  4. Sair")
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
                self._encerrar()
                break

            else:
                print(f"\n  [!] Opção inválida: '{opcao}'. Digite 1, 2, 3 ou 4.")

    def _exibir_boas_vindas(self):
        """Exibe a mensagem de boas-vindas."""
        print()
        print("=" * 60)
        print(f"  Bem-vindo ao {self.nome}!")
        print("=" * 60)
        print("  Assistente digital de orientacao ao cidadao.")
        print("  Temas: documentos, saude, direitos e energia.")
        print()
        print("  [!] IMPORTANTE: Este assistente e educacional e NAO")
        print("     substitui atendimento oficial. Sempre confirme as")
        print("     informacoes nas fontes oficiais indicadas.")
        print()
        cats = self.base.categorias()
        if cats:
            print(f"  Categorias disponíveis: {', '.join(cats)}")
            print(f"  Total de orientações: {len(self.base.orientacoes)}")
        print("=" * 60)

    def _encerrar(self):
        """Procedimento de encerramento: coleta nota e salva dados."""
        print()
        print("=" * 60)
        print("  Encerrando o atendimento...")
        print("=" * 60)

        # Coleta nota de facilidade de uso
        nota = None
        while nota is None:
            resp = self._input_seguro(
                "  Antes de sair: qual nota você dá para a facilidade de uso?\n"
                "  (1 = muito difícil  |  5 = muito fácil): "
            ).strip()
            if not resp:
                # EOF ou entrada vazia — aceita sem nota
                nota = 0
                break
            try:
                n = int(resp)
                if 1 <= n <= 5:
                    nota = n
                else:
                    print("  [!] Digite um número entre 1 e 5.")
            except ValueError:
                print("  [!] Por favor, digite um número de 1 a 5.")

        print(f"\n  Obrigado pela avaliação! Nota: {nota}/5")

        # Salva a nota para aparecer nos indicadores
        self.nota_facilidade = nota

        # Exibe indicadores finais
        self.indicadores()

        # Exporta CSV
        self.exportar_csv()

        print()
        print("  Obrigado por usar o Citizen Assist AI!")
        print("  Em caso de dúvidas urgentes, procure o CRAS mais próximo")
        print("  ou ligue 156 (prefeitura) ou 0800 722 0500 (Caixa).")
        print("=" * 60)
        print()
