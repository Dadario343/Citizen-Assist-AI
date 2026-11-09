# Citizen Assist AI — Assistente Digital & Portal de Orientação ao Cidadão 🌐⚡

> **FIAP — Global Solution 2026.2**  
> **Disciplinas Integradas:**  
> 1. **Pensamento Computacional e Automação com Python (PCP)**  
> 2. **Soluções em Energias Renováveis e Sustentáveis (SERS)**  
>  
> **Tema Central:** Orientação acessível, ética e gratuita ao cidadão em situação de vulnerabilidade socioeconômica sobre documentos básicos, saúde pública no SUS, direitos sociais e alternativas sustentáveis de redução da conta de luz (combate à pobreza energética).

---

## 👥 Integrantes da Equipe

| Nome Completo | RM |
|---|---|
| **Olavo Dadario Vianna Barreto** | RM 569272 |
| **Paulo Henrique Lira Bilac de Araujo** | RM 569496 |
| **Pedro Soares de Souza** | RM 571285 |

---

## 🎯 Arquitetura Dual do Projeto (Terminal Python + Web GUI)

Para atender com excelência aos critérios avaliativos de ambas as disciplinas, o **Citizen Assist AI** foi concebido em dois módulos complementares que compartilham a mesma base regulatória e metodológica:

1. **Módulo Terminal Python (Obrigatório para PCP):** Implementação estrita em Python 3 orientada a objetos (POO), distribuída em 4 módulos (`main.py`, `orientacao.py`, `base_conhecimento.py`, `assistente.py`), com carregamento dinâmico de JSON, busca heurística com retorno em tuplas, navegação interativa, persistência em CSV via `csv.DictWriter`, métricas estatísticas e coleta de notas de usabilidade.
2. **Módulo Web Interativo (Aplicação Gráfica & Acesso Público):** Single Page Application moderna e responsiva (`index.html`), pronta para uso online via **GitHub Pages**, contendo carrossel de transparência, chat com feedback visual, calculadora de consumo energético em tempo real e exportação de dados.

- 🚀 **Acesso Online Imediato (GitHub Pages):** [https://dadario343.github.io/Citizen-Assist-AI/](https://dadario343.github.io/Citizen-Assist-AI/)  
- 📂 **Repositório Oficial no GitHub:** [https://github.com/Dadario343/Citizen-Assist-AI](https://github.com/Dadario343/Citizen-Assist-AI)  
- 📄 **Memorial Técnico de Cálculos Energéticos (SERS):** [`docs/MEMORIAL_CALCULO_SERS.md`](docs/MEMORIAL_CALCULO_SERS.md)

---

## 🧭 Público-Alvo e Problema Escolhido

- **Público:** Famílias e trabalhadores de baixa renda no Brasil cadastrados ou elegíveis ao CadÚnico, beneficiários de programas sociais e comunidades que sofrem com a **pobreza energética**.
- **Problema:** A burocracia governamental, a dispersão de informações oficiais e a proliferação de intermediários que cobram por serviços públicos gratuitos criam barreiras de acesso à cidadania. Paralelamente, os altos custos da fatura de eletricidade comprometem a subsistência básica dessas famílias por desconhecimento dos benefícios tarifários por lei.
- **Solução Integrada:** O Citizen Assist AI centraliza orientações em linguagem clara, direta e didática em 4 categorias essenciais:
  1. **Documentos Básicos:** RG (CIN), regularização de CPF, Carteira de Trabalho Digital (CTPS) e Título de Eleitor.
  2. **Saúde Pública (SUS):** Cartão Nacional de Saúde (CNS), vacinação, Farmácia Popular e CAPS.
  3. **Direitos Sociais:** Bolsa Família, CadÚnico, CRAS, Defensoria Pública e PROCON.
  4. **Energia & Sustentabilidade:** Tarifa Social de Energia Elétrica (TSEE), eficiência energética residencial e microgeração solar fotovoltaica.

---

## 🌿 ODS Vinculados (Agenda 2030 ONU)

| ODS | Denominação | Contribuição Específica do Assistente |
|---|---|---|
| **ODS 1** | Erradicação da Pobreza | Desbloqueia o acesso a programas de transferência de renda e tarifa reduzida de serviços essenciais. |
| **ODS 7** | Energia Limpa e Acessível | Orienta sobre a TSEE (descontos de 35% a 72%), boas práticas de consumo e viabilidade de energia solar. |
| **ODS 10** | Redução das Desigualdades | Universaliza a orientação jurídica, social e de saúde para populações vulneráveis. |
| **ODS 16** | Paz, Justiça e Instituições Eficazes | Conecta o cidadão aos órgãos formais de direito e transparência pública sem intermediários. |

---

## 🐍 Implementação Técnica em Python (Disciplina PCP)

### 1. Modularização Exigida e Responsabilidades

```
Citizen-Assist-AI/
├── main.py                  # Ponto de entrada, inicialização e injeção de dependências
├── orientacao.py            # Classe de modelo Orientacao (encapsulamento e formatação)
├── base_conhecimento.py     # Classe BaseConhecimento (normalização, pontuação e busca)
├── assistente.py            # Classe Assistente (interface CLI, menus, CSV e indicadores)
├── server.py                # Servidor HTTP local opcional para a versão web
├── index.html               # Portal Web interativo para cidadãos e avaliadores
├── docs/
│   └── MEMORIAL_CALCULO_SERS.md # Memória completa de engenharia e cálculo energético
├── data/
│   ├── base_conhecimento.json # 19 orientações cadastradas com todos os 9 campos obrigatórios
│   ├── historico.json         # Histórico de atendimentos persistido em JSON (17 registros)
│   ├── atendimentos.csv       # Histórico exportado com csv.DictWriter (8 colunas)
│   └── avaliacoes.json        # Notas de usabilidade coletadas no encerramento (8 avaliações)
├── entrega_pcp.txt          # Arquivo de entrega formatado para o Portal FIAP (PCP)
└── entrega_sers.txt         # Arquivo de entrega formatado para o Portal FIAP (SERS)
```

### 2. Orientação a Objetos e Composição

O sistema adota o padrão de **composição de objetos**:
- `Assistente` **possui uma** instância de `BaseConhecimento` injetada em seu construtor `__init__(self, nome, base)`.
- `BaseConhecimento` **possui uma lista de** instâncias de `Orientacao` em `self.orientacoes`, carregadas do JSON.
- `Orientacao` encapsula os 9 atributos obrigatórios: `id`, `categoria`, `titulo`, `palavras_chave`, `resposta`, `documentos`, `onde`, `fonte`, `verificado_em`.

### 3. Mecanismo de Busca Heurística e Classificação de Confiança

A busca em linguagem natural implementada em `BaseConhecimento.buscar(pergunta)` segue regras matemáticas determinísticas:
- **Normalização Textual:** Conversão para minúsculas, remoção de acentos (`á` -> `a`, `ç` -> `c`, etc.) e pontuação.
- **Pontuação:**
  - `+3 pontos` para cada palavra-chave da orientação encontrada na pergunta normalizada.
  - `+1 ponto` para cada palavra da pergunta (com 4 ou mais caracteres) presente no título normalizado.
- **Retorno em Tuplas:** Retorna lista de tuplas Python `(score, orientacao)`, ordenadas de forma decrescente por pontuação.
- **Classificação de Confiança:**
  - `Score >= 6`: **Confiança ALTA** (mensagem de correspondência direta).
  - `Score 3 a 5`: **Confiança MÉDIA** (mensagem de orientação relacionada).
  - `Score < 3`: **Sem correspondência** (informa educadamente que não encontrou, lista as 4 categorias disponíveis e orienta como reformular).
- **Apresentação de Alternativas:** O sistema exibe o melhor resultado e, havendo outras orientações pontuadas, lista **até 2 orientações alternativas** (`resultados[1:3]`).

### 4. Robustez, Proteção LGPD e Navegação

- **Tratamento de Exceções:** O leitor de JSON trata `FileNotFoundError` e `json.JSONDecodeError`, impedindo encerramento abrupto caso a base esteja ausente ou malformatada.
- **Proteção de Dados Pessoais (LGPD):** O método `_contem_dado_pessoal` detecta sequências de 8 ou mais dígitos (como CPF ou telefones) e a presença de `@` (e-mails). Mensagens com esses padrões são bloqueadas e **jamais são gravadas no histórico**.
- **Navegação Categórica e Menus:** Todos os menus e submenus possuem validação rigorosa de entrada numérica e a opção padronizada **`0` para voltar** ou encerrar.
- **Medição Precisa de Tempo:** O cronômetro de busca afere estritamente o tempo de processamento do algoritmo de busca (`self.base.buscar`), sem misturar com o tempo de leitura humana.

### 5. Registro de Atendimentos, Indicadores e Exportação CSV

- Ao concluir cada busca ou navegação, o atendimento é registrado em `self.historico` e no arquivo `data/historico.json`.
- O método `indicadores()` calcula e projeta os 6 indicadores obrigatórios:
  1. **Taxa de Encontro (%):** Percentual de atendimentos em que uma orientação foi localizada.
  2. **Tempo Médio de Busca:** Média em segundos despendida até obter a resposta.
  3. **Taxa de Acerto (%):** Percentual de atendimentos em que o usuário confirmou que a resposta ajudou.
  4. **Tentativas por Atendimento:** Média de consultas efetuadas por sessão.
  5. **Facilidade de Uso (1 a 5):** Média ponderada das avaliações coletadas na saída (iniciando com lista vazia `[]` sem valores fictícios).
  6. **Lista de Dúvidas Sem Solução:** Termos e consultas que não atingiram pontuação mínima, permitindo curadoria contínua.
- **Exportação CSV:** Utiliza a biblioteca nativa `csv.DictWriter` com cabeçalho composto por 8 campos:  
  `data, origem, pergunta, id_orientacao, encontrou, ajudou, tentativas, tempo_segundos`.

---

## ⚡ Estudo e Memória de Cálculo Energético (Disciplina SERS)

A análise energética do Citizen Assist AI (disponível no menu 4 do terminal, na aba "Energia Sustentável" da Web e detalhada no documento [`docs/MEMORIAL_CALCULO_SERS.md`](docs/MEMORIAL_CALCULO_SERS.md)) investiga alternativas reais de combate à vulnerabilidade tarifária para uma família de baixa renda típica:
- **Perfil de Referência Estimado:** 3 a 4 moradores, consumo mensal de **150 kWh/mês**, tarifa média homologada ANEEL de **R$ 0,75/kWh**, resultando em uma fatura base de **R$ 112,50/mês**.

### 1. Fator de Emissão Oficial de CO₂ da Matriz Elétrica Nacional
- **Fator Oficial Médio do SIN (MCTI/SIRENE 2023/2024):** **0,0385 kg CO₂/kWh** (38,5 kg CO₂/MWh).
- **Cálculo de Emissões Evitadas:**
  - Sobre o consumo de 150 kWh/mês: `150 x 0,0385 = 5,78 kg CO₂/mês` (~69,3 kg CO₂/ano).
  - Sobre a geração solar de 168,5 kWh/mês: `168,5 x 0,0385 = 6,49 kg CO₂/mês` (~77,8 kg CO₂/ano).
- *Nota Técnica:* O fator de 0,50 kg CO₂/kWh refere-se exclusivamente ao despacho fóssil térmico de pico, enquanto a base média oficial do SIN é 0,0385 kg CO₂/kWh.

### 2. Alternativa 1: Tarifa Social de Energia Elétrica (TSEE)
- **Legislação:** Lei Federal nº 10.438/2002, Resolução Normativa ANEEL nº 1.000/2021 e modelo de gratuidade do Programa Luz do Povo.
- **Investimento:** R$ 0,00 | **Payback:** Imediato.
- **Modelo Atualizado (Gratuidade até 80 kWh/mês):**
  - Parcela 0 a 80 kWh: 100% de gratuidade -> R$ 0,00
  - Parcela 81 a 150 kWh (70 kWh com 40% desc.): `70 x 0,75 x 0,60 = R$ 31,50`
  - Nova conta estimada: **R$ 31,50/mês** -> Economia estimada de **R$ 81,00/mês (72,0% de redução)**.
- **Modelo Geral de Faixas Progressivas (Lei 10.438/2002):**
  - 0 a 30 kWh (65% desc.): `30 x 0,75 x 0,35 = R$ 7,88`
  - 31 a 100 kWh (40% desc.): `70 x 0,75 x 0,60 = R$ 31,50`
  - 101 a 150 kWh (10% desc.): `50 x 0,75 x 0,90 = R$ 33,75`
  - Nova conta estimada: **R$ 73,13/mês** -> Economia estimada de **R$ 39,37/mês (35,0% de redução)**.

### 3. Alternativa 2: Microgeração Solar Fotovoltaica Residencial
- **Fórmula de Engenharia:**
  `E = P x H x D x PR = 1,5 kWp x 4,8 kWh/m²/dia x 30 dias x 0,78 = 168,48 kWh/mês (~168,5 kWh/mês)`
  - *Premissas:* Sistema de 1,5 kWp (3 módulos de 500 Wp + microinversor), irradiação média de 4,8 kWh/m²/dia (Atlas Solar / INPE), Performance Ratio de 78%. Atende 100% da demanda de 150 kWh/mês com excedente de 18,5 kWh/mês.
- **Investimento Instalado:** **R$ 7.500,00 a R$ 9.500,00** (Benchmark Greener / ABSOLAR 2024/2025 para sistemas até 2 kWp).
- **Limitações Reais da Lei 14.300/2022 (A conta não zera):**
  - Custo de disponibilidade monofásico (30 kWh x R$ 0,75 = R$ 22,50/mês) + Fio B gradual + iluminação pública (COSIP).
  - Conta residual pós-solar estimada: **R$ 20,00 a R$ 35,00/mês**.
  - Economia líquida mensal: **R$ 77,50 a R$ 92,50/mês** (70% a 82% de redução).
- **Memória de Cálculo de Payback Simples:**
  - Cenário Otimista: `R$ 7.500 / (R$ 92,50 x 12) = 6,76 anos (~6,8 anos)`
  - Cenário Moderado: `R$ 8.500 / (R$ 85,00 x 12) = 8,33 anos (~8,3 anos)`
  - Cenário Conservador: `R$ 9.500 / (R$ 77,50 x 12) = 10,22 anos (~10,2 anos)`
  - Faixa consolidada: **6,8 a 10,2 anos** (média ponderada: **8,3 anos**). Vida útil dos módulos: 25 anos.

### 4. Alternativa 3: Cenário Combinado (TSEE + Eficiência Residencial)
- **Demonstração Matemática da Redução de 40 kWh/mês (150 para 110 kWh/mês):**
  - *Chuveiro 3.800 W:* 4 moradores reduzindo banhos de 12 para 8 min/dia -> Economia de **30,4 kWh/mês**.
  - *Iluminação:* Troca de 4 lâmpadas fluorescentes 25 W por LEDs de 9 W -> Economia de **7,7 kWh/mês**.
  - *Standby:* Desligamento de consumo vampiro em eletrônicos -> Economia de **1,9 kWh/mês**.
  - *Total economizado comprovado:* **40,0 kWh/mês** com investimento de R$ 0 a R$ 40 em lâmpadas.
- **Fatura Estimada:**
  - No regime de gratuidade até 80 kWh: 0 a 80 kWh (R$ 0) + 30 kWh (R$ 13,50) = **R$ 13,50/mês** (Economia de **R$ 99,00/mês — 88% de redução**).
  - No regime de faixas da Lei 10.438: 30 kWh (R$ 7,88) + 70 kWh (R$ 31,50) + 10 kWh (R$ 6,75) = **R$ 46,13/mês** (Economia de **R$ 66,37/mês — 59% de redução**).

### 5. Tabela Comparativa Consolidada

| Indicador | Situação Atual | Alt. 1: Tarifa Social (TSEE) | Alt. 2: Solar 1,5 kWp | Alt. 3: Combinada (TSEE + Eficiência) |
|---|:---:|:---:|:---:|:---:|
| **Conta Estimada (R$)** | R$ 112,50 | R$ 31,50 a R$ 73,13 | R$ 20,00 a R$ 35,00 | **R$ 13,50 a R$ 46,13** |
| **Economia Mensal Estimada** | R$ 0,00 | R$ 39,37 a R$ 81,00 | R$ 77,50 a R$ 92,50 | **R$ 66,37 a R$ 99,00** |
| **Percentual de Redução** | 0% | 35% a 72% | 70% a 82% | **59% a 88%** |
| **Investimento Inicial** | R$ 0,00 | R$ 0,00 | R$ 7.500 a R$ 9.500 | **R$ 0,00** |
| **Payback Simples** | N/A | Imediato | 6,8 a 10,2 anos (méd. 8,3) | **Imediato** |
| **CO₂ Evitado Estimado** | 0 kg | Indireto | ~5,8 a 6,5 kg CO₂/mês | ~1,5 kg CO₂/mês |

---

## 🧪 Relatório Completo de Testes com Usuários Reais

Foram conduzidas sessões de teste com **3 participantes externos à equipe** (preservando integralmente o anonimato conforme exigido pelas diretrizes éticas e pela LGPD), totalizando **17 atendimentos registrados** nos arquivos oficiais de auditoria (`data/historico.json` e `data/atendimentos.csv`):

### Perfil Anonimizado dos Participantes

1. **Participante A (40 a 45 anos, trabalhador autônomo):** Buscou regularizar pendência de CPF e entender como solicitar a Tarifa Social de energia.
2. **Participante B (30 a 35 anos, mãe de família):** Buscou orientações sobre inscrição no Cadastro Único (CadÚnico) e medicamentos gratuitos pela Farmácia Popular.
3. **Participante C (60 a 65 anos, aposentado):** Testou a emissão da nova Carteira de Identidade Nacional (CIN / RG) e simulou a redução da conta de energia elétrica de sua residência.

### Tabela de Indicadores Reais Obtidos nos Testes

| Métrica Avaliada | Dados Reais dos Arquivos | Situação |
|---|:---:|:---:|
| **Total de Atendimentos Realizados** | **17 atendimentos** | ✅ Atende ao mínimo exigido (>= 10) |
| **Respostas Encontradas** | **13 atendimentos (76,5%)** | ✅ Alta taxa de localização |
| **Taxa de Acerto (Orientação Ajudou)** | **12 atendimentos (70,6%)** | ✅ Conteúdo relevante e claro |
| **Tempo Médio de Busca Registrado** | **4,75 segundos** | ✅ Resposta ágil |
| **Média de Tentativas por Atendimento** | **1,00 tentativa** | ✅ Assertividade imediata |
| **Avaliações de Facilidade de Uso** | **8 avaliações | Média: 4,50 / 5,00** | ✅ Excelente usabilidade |

### Dúvidas Sem Solução Registradas no Histórico Real

As 4 dúvidas sem solução presentes no arquivo `data/historico.json` foram:
1. *"quais são os tipos de energia limpa no Brasil?"*
2. *"Qual a data de lançamento de Zelda Ocarina of time?"*
3. *"vacinas"*
4. *"que dia é hoje"*

### Comentários Recebidos e Ajustes Realizados

| Situação Testada | Comentário / Observação do Usuário | Ajuste Realizado no Projeto |
|---|---|---|
| **Busca por Vacinação** | Usuário digitou "vacinas" no plural e não obteve resultado no teste inicial. | Inclusão de "vacinas" e "imunizações" nas palavras-chave da Orientação 7 na base de conhecimento. |
| **Dúvidas Fora de Escopo** | Usuário realizou consultas aleatórias (jogo Zelda, que dia é hoje) e ficou sem direcionamento. | Implementação de retorno didático orientando sobre as 4 categorias atendidas e sugerindo termos válidos. |
| **Calculadora de Energia** | Usuário desejava confirmação visual de que os valores mudavam ao alterar a potência e horas. | Criação de pulso visual animado (`calc-pulse`), badge verde de confirmação e exibição do horário exato do recálculo. |
| **Dúvida Conceitual de Energia** | Consulta sobre matriz de energia limpa no Brasil pontuou abaixo do limiar. | Enriquecimento das palavras-chave e do texto da Orientação 16 com termos sobre matriz renovável brasileira. |

---

## 💻 Instruções de Execução

### Execução do Assistente Terminal em Python (PCP)

Certifique-se de possuir o **Python 3.8+** instalado. No terminal, execute:

```bash
# Clone o repositório
git clone https://github.com/Dadario343/Citizen-Assist-AI.git
cd Citizen-Assist-AI

# Execute o programa principal
python main.py
```

### Execução da Versão Web Localmente

```bash
# Inicia o servidor HTTP embutido e abre no navegador padrão
python server.py
```
*Ou simplesmente abra o arquivo `index.html` em qualquer navegador.*

---

## 🎥 Roteiro Técnico dos Vídeos

### Vídeo 1: Pensamento Computacional e Automação com Python (PCP)
- **Duração Exigida:** Entre **5 e 8 minutos**.
- **Conteúdo a Demonstrar:**
  1. Apresentação dos integrantes e objetivo do assistente.
  2. Modularização nos 4 arquivos: `main.py`, `orientacao.py`, `base_conhecimento.py` e `assistente.py`.
  3. Composição de classes (`Assistente` -> `BaseConhecimento` -> `Orientacao`), destacando `self` e `__init__`.
  4. Carregamento do JSON com tratamento de `FileNotFoundError` e `JSONDecodeError`.
  5. Busca heurística determinística com retorno em tuplas, classificação de confiança e exibição de até 2 alternativas.
  6. Navegação por categorias com opção `0` para voltar em todas as telas.
  7. Simulação de alteração ao vivo de palavra-chave no JSON comprovando atualização dinâmica.
  8. Bloqueio de dados pessoais (CPF/e-mail) sem registro no histórico.
  9. Encerramento com coleta de nota de facilidade (1 a 5), exibição dos 6 indicadores e exportação para CSV com `csv.DictWriter`.

### Vídeo 2: Soluções em Energias Renováveis e Sustentáveis (SERS)
- **Duração Exigida:** **Máximo de 3 minutos**.
- **Conteúdo a Demonstrar:**
  1. Problema da pobreza energética e fatura de referência (150 kWh/mês = R$ 112,50).
  2. Calculadora de consumo e aplicação das regras da Tarifa Social (TSEE).
  3. Dimensionamento solar de 1,5 kWp pela fórmula de engenharia (168,5 kWh/mês), custos (Greener/ABSOLAR) e payback consistente (6,8 a 10,2 anos).
  4. Fator oficial do SIN (0,0385 kg CO₂/kWh — MCTI/SIRENE) e emissões evitadas.
  5. Cenário combinado (TSEE + eficiência energética) com redução de 59% a 88% sem custos para o cidadão.

---

## 📝 Arquivos de Entrega para o Portal FIAP

Os arquivos `.txt` contendo os dados de submissão acadêmica estão gerados na raiz do repositório:
- [`entrega_pcp.txt`](entrega_pcp.txt): Modelo de entrega para Pensamento Computacional e Automação com Python.
- [`entrega_sers.txt`](entrega_sers.txt): Modelo de entrega para Soluções em Energias Renováveis e Sustentáveis.
