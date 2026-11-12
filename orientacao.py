class Orientacao:
    """Representa uma orientacao ao cidadao da base de conhecimento."""

    def __init__(self, id, categoria, titulo, palavras_chave, resposta,
                 documentos, onde, fonte, verificado_em):
        self.id = id
        self.categoria = categoria
        self.titulo = titulo
        self.palavras_chave = palavras_chave
        self.resposta = resposta
        self.documentos = documentos
        self.onde = onde
        self.fonte = fonte
        self.verificado_em = verificado_em

    def exibir(self):
        """Exibe a orientacao de forma formatada no terminal."""
        separador = "=" * 60
        print()
        print(separador)
        print(f"  {self.titulo}  [{self.categoria}]")
        print(separador)
        print()
        print("ORIENTACAO:")
        # Exibe respeitando quebras de linha e paragrafos
        for bloco in self.resposta.split("\n"):
            bloco_strip = bloco.strip()
            if not bloco_strip:
                print()
                continue
            indent = "  "
            if bloco.startswith("  "):
                indent = "    "
            palavras = bloco_strip.split()
            linha = ""
            for palavra in palavras:
                if len(linha) + len(palavra) + 1 > 68:
                    print(f"{indent}{linha}")
                    linha = palavra
                else:
                    linha = f"{linha} {palavra}".strip()
            if linha:
                print(f"{indent}{linha}")
        print()

        if self.documentos:
            print("DOCUMENTOS NECESSARIOS:")
            for doc in self.documentos:
                print(f"  * {doc}")
            print()

        print("ONDE BUSCAR:")
        print(f"  {self.onde}")
        print()

        print("FONTE OFICIAL:")
        for fonte_item in self.fonte.split("|"):
            print(f"  * {fonte_item.strip()}")
        print()

        print(f"Verificado em: {self.verificado_em}")
        print()
        print("-" * 60)
        print("[!] Aviso: este assistente NAO e um canal oficial.")
        print("   Confirme sempre as informacoes nas fontes indicadas.")
        print(separador)
        print()
