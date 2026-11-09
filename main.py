"""
Citizen Assist AI - Assistente Digital de Orientação ao Cidadão
Ponto de entrada principal do programa.

Integrantes:
  - Olavo Dadario Vianna Barreto    (RM 569272)
  - Paulo Henrique Lira Bilac de Araujo (RM 569496)
  - Pedro Soares de Souza           (RM 571285)
"""

import sys
import os

# Garante saída UTF-8 no Windows (evita erros com caracteres especiais)
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

from base_conhecimento import BaseConhecimento
from assistente import Assistente

if __name__ == "__main__":
    base = BaseConhecimento("data/base_conhecimento.json")
    base.carregar()

    assistente = Assistente("Citizen Assist AI", base)
    assistente.iniciar()
