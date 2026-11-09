import json
import os
from orientacao import Orientacao

# Mapa de substituição de acentos para normalização de texto
ACENTOS = {
    "á": "a", "à": "a", "ã": "a", "â": "a",
    "é": "e", "ê": "e",
    "í": "i", "î": "i",
    "ó": "o", "õ": "o", "ô": "o",
    "ú": "u", "û": "u",
    "ç": "c",
    "ä": "a", "ë": "e", "ï": "i", "ö": "o", "ü": "u",
}


def normalizar(texto):
    """
    Normaliza o texto: lowercase, remove acentos, remove pontuação,
    e envolve em espaços para facilitar busca por palavras inteiras.
    Retorna a string no formato ' palavra1 palavra2 ... '.
    """
    texto = texto.lower().strip()
    for letra, troca in ACENTOS.items():
        texto = texto.replace(letra, troca)
    for sinal in "?!.,;:()[]{}\"'/-_":
        texto = texto.replace(sinal, " ")
    # Retorna com espaço no início e fim para facilitar busca com " palavra "
    return " " + " ".join(texto.split()) + " "


class BaseConhecimento:
    """Carrega e gerencia a base de orientações ao cidadão."""

    def __init__(self, caminho):
        self.caminho = caminho
        self.orientacoes = []  # lista de objetos Orientacao

    def carregar(self):
        """Carrega as orientações do arquivo JSON. Trata erros de arquivo/formato."""
        if not os.path.exists(self.caminho):
            print(f"[Aviso] Arquivo de base de conhecimento não encontrado: {self.caminho}")
            print("[Aviso] O assistente iniciará com base vazia.")
            self.orientacoes = []
            return

        try:
            with open(self.caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[Aviso] Erro ao ler o arquivo JSON ({e}). Base de conhecimento vazia.")
            self.orientacoes = []
            return
        except Exception as e:
            print(f"[Aviso] Erro inesperado ao carregar base ({e}). Base de conhecimento vazia.")
            self.orientacoes = []
            return

        self.orientacoes = []
        for item in dados:
            try:
                orientacao = Orientacao(
                    id=item.get("id", 0),
                    categoria=item.get("categoria", "Geral"),
                    titulo=item.get("titulo", "Sem título"),
                    palavras_chave=item.get("palavras_chave", []),
                    resposta=item.get("resposta", ""),
                    documentos=item.get("documentos", []),
                    onde=item.get("onde", ""),
                    fonte=item.get("fonte", ""),
                    verificado_em=item.get("verificado_em", "")
                )
                self.orientacoes.append(orientacao)
            except Exception as e:
                print(f"[Aviso] Erro ao carregar item id={item.get('id','?')}: {e}")

        print(f"[Info] Base de conhecimento carregada: {len(self.orientacoes)} orientações.")

    def categorias(self):
        """Retorna lista ordenada de categorias únicas."""
        cats = set(o.categoria for o in self.orientacoes)
        return sorted(cats)

    def por_categoria(self, categoria):
        """Retorna lista de Orientacao objects de uma dada categoria."""
        return [o for o in self.orientacoes if o.categoria == categoria]

    def pontuar(self, pergunta, orientacao):
        """
        Calcula a pontuação de relevância de uma orientação para uma pergunta.
        Regras:
          +3 para cada palavra-chave da orientação encontrada na pergunta normalizada
          +1 para cada palavra da pergunta (4+ letras) encontrada no título normalizado
        Retorna inteiro >= 0.
        """
        pergunta_norm = normalizar(pergunta)
        titulo_norm = normalizar(orientacao.titulo)
        score = 0

        # +3 por palavra-chave encontrada na pergunta
        for chave in orientacao.palavras_chave:
            chave_norm = normalizar(chave).strip()
            if chave_norm and f" {chave_norm} " in pergunta_norm:
                score += 3

        # +1 por palavra da pergunta (4+ letras) encontrada no título
        palavras_pergunta = pergunta_norm.split()
        for palavra in palavras_pergunta:
            if len(palavra) >= 4 and f" {palavra} " in titulo_norm:
                score += 1

        return score

    def buscar(self, pergunta):
        """
        Busca orientações relevantes para a pergunta.
        Retorna lista de tuplas (score, orientacao) ordenada por score decrescente,
        incluindo apenas itens com score > 0.
        """
        resultados = []
        for orientacao in self.orientacoes:
            score = self.pontuar(pergunta, orientacao)
            if score > 0:
                resultados.append((score, orientacao))

        # Ordena por score decrescente; em empate, mantém ordem original
        resultados.sort(key=lambda x: x[0], reverse=True)
        return resultados
