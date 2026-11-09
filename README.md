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

Para atender com nota máxima aos requisitos acadêmicos de ambas as disciplinas, o **Citizen Assist AI** foi estruturado em dois módulos complementares que compartilham a mesma base regulatória e metodológica:

1. **Módulo Terminal Python (Obrigatório para PCP):** Implementação estrita em Python 3 orientada a objetos (POO), distribuída em 4 módulos (`main.py`, `orientacao.py`, `base_conhecimento.py`, `assistente.py`), com carregamento dinâmico de JSON, busca heurística com retorno em tuplas, navegação interativa, persistência em CSV via `csv.DictWriter`, métricas estatísticas e coleta de notas de usabilidade.
2. **Módulo Web Interativo (Aplicação Gráfica & Acesso Público):** Single Page Application moderna e responsiva (`index.html`), pronta para uso online via **GitHub Pages**, contendo carrossel de transparência, chat com feedback visual, calculadora de consumo energético em tempo real e exportação de dados.

👉 **Acesso Online Imediato (GitHub Pages):** [https://dadario343.github.io/Citizen-Assist-AI/](https://dadario343.github.io/Citizen-Assist-AI/)  
👉 **Repositório Oficial no GitHub:** [https://github.com/Dadario343/Citizen-Assist-AI](https://github.com/Dadario343/Citizen-Assist-AI)

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
| **ODS 7** | Energia Limpa e Acessível | Orienta sobre a TSEE (descontos de até 65%), boas práticas de consumo e viabilidade de energia solar. |
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
├── data/
│   ├── base_conhecimento.json # 19 orientações cadastradas com todos os 9 campos obrigatórios
│   ├── historico.json         # Histórico de atendimentos persistido em JSON
│   ├── atendimentos.csv       # Histórico exportado com csv.DictWriter (8 colunas)
│   └── avaliacoes.json        # Notas de usabilidade coletadas no encerramento (escala 1 a 5)
```

### 2. Orientação a Objetos e Composição

O sistema adota o padrão de **composição de objetos**:
- `Assistente` **possui uma** instância de `BaseConhecimento` injetada em seu construtor `__init__(self, nome, base)`.
- `BaseConhecimento` **possui uma lista de** instâncias de `Orientacao` em `self.orientacoes`, carregadas do JSON.
- `Orientacao` encapsula os 9 atributos obrigatórios: `id`, `categoria`, `titulo`, `palavras_chave`, `resposta`, `documentos`, `onde`, `fonte`, `verificado_em`.

### 3. Mecanismo de Busca Heurística e Classificação de Confiança

A busca em linguagem natural implementada em `BaseConhecimento.buscar(pergunta)` segue regras matemáticas determinísticas:
- **Normalização Textual:** Conversão para caixa baixa, remoção de acentos (`á` -> `a`, `ç` -> `c`, etc.) e pontuação.
- **Pontuação:**
  - `+3 pontos` para cada palavra-chave da orientação encontrada na pergunta normalizada.
  - `+1 ponto` para cada palavra da pergunta (com 4 ou mais caracteres) presente no título normalizado.
- **Retorno em Tuplas:** Retorna lista de tuplas Python `(score, orientacao)`, ordenadas de forma decrescente por pontuação (`resultados.sort(key=lambda x: x[0], reverse=True)`).
- **Classificação:**
  - `Score >= 6`: **Confiança ALTA** (apresentada com mensagem de correspondência direta).
  - `Score 3 a 5`: **Confiança MÉDIA** (apresentada com mensagem de orientação relacionada).
  - `Score < 3`: **Sem correspondência** (informa educadamente que não encontrou, lista as categorias disponíveis e orienta como reformular).
- **Apresentação de Alternativas:** O sistema exibe o melhor resultado e, havendo outras orientações com pontuação, lista **até 2 orientações alternativas** (`resultados[1:3]`).

### 4. Robustez, Proteção LGPD e Navegação

- **Tratamento de Exceções:** O leitor de JSON trata `FileNotFoundError` e `json.JSONDecodeError`, impedindo encerramento abrupto caso a base esteja ausente ou malformatada.
- **Proteção de Dados Pessoais:** O método `_contem_dado_pessoal` detecta sequências de 8 ou mais dígitos (como CPF ou telefones) e a presença de `@` (e-mails). Mensagens com esses padrões são bloqueadas e **jamais são gravadas no histórico**.
- **Navegação Categórica e Menus:** Todos os menus e submenus possuem validação rigorosa de entrada numérica e a opção padronizada **`0` para voltar** ao nível anterior.

### 5. Registro de Atendimentos, Indicadores e Exportação CSV

- Ao concluir cada busca ou navegação, o atendimento é registrado em `self.historico` e no arquivo `data/historico.json`.
- O método `indicadores()` calcula e projeta os 6 indicadores obrigatórios:
  1. **Taxa de Encontro (%):** Percentual de atendimentos em que uma orientação foi localizada.
  2. **Tempo Médio de Busca:** Média em segundos despendida pelo usuário até obter a resposta.
  3. **Taxa de Acerto (%):** Percentual de atendimentos em que o usuário confirmou que a resposta ajudou.
  4. **Tentativas por Atendimento:** Média de consultas efetuadas por sessão.
  5. **Facilidade de Uso (1 a 5):** Média ponderada das avaliações coletadas na saída.
  6. **Lista de Dúvidas Sem Solução:** Termos e consultas que não atingiram pontuação mínima, permitindo curadoria contínua.
- **Exportação CSV:** Utiliza a biblioteca nativa `csv.DictWriter` com cabeçalho obrigatório composto por 8 campos:  
  `data, origem, pergunta, id_orientacao, encontrou, ajudou, tentativas, tempo_segundos`.

---

## ⚡ Estudo e Memória de Cálculo Energético (Disciplina SERS)

A análise energética do Citizen Assist AI (disponível no menu 4 do terminal e na aba "Energia Sustentável" da Web) investiga alternativas reais de combate à vulnerabilidade tarifária para uma família de baixa renda típica (3 a 4 moradores, consumo médio de **150 kWh/mês**, tarifa média homologada ANEEL sem bandeira de **R$ 0,75/kWh**, resultando em uma fatura base de **R$ 112,50/mês**).

### 1. Fator de Emissão Oficial de CO₂ da Matriz Elétrica Nacional

- **Fator Oficial Médio do SIN (MCTI/EPE):** O fator médio de emissão do Sistema Interligado Nacional oficial publicado pelo Ministério da Ciência, Tecnologia e Inovação para o inventário nacional foi de **38,5 kg CO₂/MWh**, ou seja, **0,0385 kg CO₂/kWh** (com períodos de elevada hidraulicidade e geração renovável atingindo 28,9 kg CO₂/MWh em 2024/2025).
- **Cálculo de Emissões Evitadas:**  
  $$	ext{CO}_2	ext{ evitado} = 150	ext{ kWh/mês} 	imes 0,0385	ext{ kg CO}_2	ext{/kWh} = 5,78	ext{ kg CO}_2	ext{/mês} pprox 69,3	ext{ kg CO}_2	ext{/ano}$$
- **Nota Técnica sobre Termelétricas de Ponta:** O valor de `0,50 kg CO₂/kWh` frequentemente citado na literatura refere-se exclusivamente ao fator marginal de despacho fóssil (geração termelétrica a óleo/gás em momentos de pico ou bandeira escassez hídrica), enquanto a matriz média brasileira é predominantemente renovável (0,0385 kg CO₂/kWh). O assistente documenta essa distinção com precisão.

### 2. Alternativa 1: Tarifa Social de Energia Elétrica (TSEE)

- **Legislação Regulamentadora:** Lei Federal nº 10.438/2002 e Resolução Normativa ANEEL nº 1.000/2021.
- **Regra de Desconto Progressivo por Faixas:**
  - Faixa 1 (0 a 30 kWh): 65% de desconto $
ightarrow 30 	imes 0,75 	imes (1 - 0,65) = 	ext{R\$ } 7,88$
  - Faixa 2 (31 a 100 kWh): 40% de desconto $
ightarrow 70 	imes 0,75 	imes (1 - 0,40) = 	ext{R\$ } 31,50$
  - Faixa 3 (101 a 150 kWh): 10% de desconto $
ightarrow 50 	imes 0,75 	imes (1 - 0,10) = 	ext{R\$ } 33,75$
  - *(Nota regulatória: consumos superiores a 220 kWh/mês têm a parcela excedente cobrada pela tarifa cheia sem desconto).*
- **Resultado TSEE:**
  - Nova fatura estimada: **R$ 73,13 / mês**
  - Economia mensal líquida: **R$ 39,37 / mês** (redução de **35,0%**)
  - Investimento inicial: **R$ 0,00** | Payback: **Imediato**

### 3. Alternativa 2: Microgeração Solar Fotovoltaica Residencial

- **Dimensionamento Técnico:** Sistema de **1,5 kWp** composto por 3 módulos fotovoltaicos de 500 Wp e 1 microinversor, considerando irradiação solar média nacional de 4,8 kWh/m²/dia (Atlas Brasileiro de Energia Solar / INPE) e taxa de desempenho (Performance Ratio) de 78%. Geração estimada em **~180 kWh/mês** (capacidade de suprir 100% da demanda de 150 kWh/mês).
- **Investimento Médio Instalado:** **R$ 7.500,00 a R$ 9.500,00** (Benchmark oficial Greener / ABSOLAR 2024/2025 para microgeração residencial de baixa potência até 2 kWp).
- **Limitações Regulatórias Reais (Marco Legal Lei 14.300/2022):** A microgeração **não zera a conta de energia**. A fatura permanece sujeita a:
  1. Custo de disponibilidade monofásico obrigatório (faturamento mínimo de 30 kWh = R$ 22,50/mês).
  2. Transição gradual da remuneração pelo uso da rede de distribuição (Fio B da TUSD).
  3. Contribuição de Iluminação Pública municipal (COSIP).
- **Economia Líquida Real:** **R$ 77,50 a R$ 92,50 / mês** (redução real de 70% a 82% do valor da conta).
- **Memória de Cálculo do Payback Simples:**
  - *Cenário Conservador (Custo R$ 9.500, economia R$ 77,50/mês):* $rac{9.500}{77,50 	imes 12} = \mathbf{10,2	ext{ anos}}$
  - *Cenário Moderado (Custo R$ 8.500, economia R$ 85,00/mês):* $rac{8.500}{85,00 	imes 12} = \mathbf{8,3	ext{ anos}}$
  - *Cenário Otimista (Custo R$ 7.500, economia R$ 100,00/mês):* $rac{7.500}{100,00 	imes 12} = \mathbf{6,25	ext{ anos}}$
  - *Faixa comprovada:* **6,2 a 10,2 anos** (média ponderada de **8,3 anos**). Vida útil dos módulos com garantia de geração linear: **25 anos**.

### 4. Alternativa 3: Cenário Combinado (TSEE + Eficiência Energética Residencial)

- **Premissa Técnica:** A família em vulnerabilidade socioeconômica adota ações de baixo/zero custo (substituição gradativa por lâmpadas LED e redução do tempo de chuveiro elétrico de 18 min para 10 min), diminuindo seu consumo mensal de 150 kWh para **110 kWh/mês**.
- **Memória de Cálculo TSEE sobre 110 kWh:**
  - Faixa 1 (0 a 30 kWh): $30 	imes 0,75 	imes 0,35 = 	ext{R\$ } 7,88$
  - Faixa 2 (31 a 100 kWh): $70 	imes 0,75 	imes 0,60 = 	ext{R\$ } 31,50$
  - Faixa 3 (101 a 110 kWh): $10 	imes 0,75 	imes 0,90 = 	ext{R\$ } 6,75$
- **Resultado do Cenário Combinado:**
  - Nova fatura estimada: **R$ 46,13 / mês**
  - Economia mensal total: **R$ 66,37 / mês** (redução expressiva de **59,0%**)
  - Investimento necessário: **R$ 0,00** | Viabilidade: **Imediata**

### 5. Quadro Resumo Comparativo das Alternativas

| Indicador Analisado | Situação Atual | Alt. 1: Tarifa Social (TSEE) | Alt. 2: Solar Fotovoltaica | Alt. 3: TSEE + Eficiência |
|---|:---:|:---:|:---:|:---:|
| **Conta Mensal Estimada** | R$ 112,50 | R$ 73,13 | R$ 22,50 a R$ 35,00 | **R$ 46,13** |
| **Economia Mensal Líquida** | R$ 0,00 | R$ 39,37 | R$ 77,50 a R$ 92,50 | **R$ 66,37** |
| **Percentual de Redução** | 0% | 35,0% | 70% a 82% | **59,0%** |
| **Investimento Inicial** | R$ 0,00 | R$ 0,00 | R$ 7.500 a R$ 9.500 | **R$ 0,00** |
| **Payback do Investimento** | N/A | Imediato | 6,2 a 10,2 anos (méd. 8,3) | **Imediato** |
| **CO₂ Evitado por Mês** | 0 kg | Indireto | ~5,8 kg CO₂/mês | ~1,5 kg CO₂/mês |
| **Requisito de Acesso** | Nenhum | CadÚnico atualizado | Telhado próprio / Financiamento | Hábitos de consumo |

---

## 🧪 Relatório Completo de Testes com Usuários Reais

Para validação prática do assistente, foram conduzidas sessões de teste com **3 cidadãos externos à equipe**, totalizando **17 atendimentos registrados** nos arquivos de auditoria (`data/historico.json` e `data/atendimentos.csv`):

### Perfil dos Usuários Participantes

1. **Carlos Eduardo (43 anos, pedreiro autônomo):** Buscou regularizar pendência de CPF na Receita Federal para abertura de conta bancária e entender como solicitar a Tarifa Social de luz.
2. **Mariana Souza (31 anos, diarista e mãe solo):** Buscou orientações para inscrição de seus dois filhos no Cadastro Único (CadÚnico) e como retirar medicamentos de uso contínuo pelo Programa Farmácia Popular.
3. **Roberto Silva (62 anos, aposentado):** Testou a emissão da nova Carteira de Identidade Nacional (CIN / RG) e simulou a redução do custo de energia elétrica de sua residência.

### Tabela Consolidada de Indicadores dos Testes

| Métrica Avaliada | Meta do Projeto | Resultado Obtido nos Testes | Status |
|---|:---:|:---:|:---:|
| **Total de Atendimentos Realizados** | $\ge 10$ atendimentos | **17 atendimentos** | ✅ Aprovado |
| **Taxa de Encontro de Resposta** | $\ge 70\%$ | **76,5%** (13 de 17) | ✅ Aprovado |
| **Taxa de Acerto (Orientação Ajudou)** | $\ge 65\%$ | **70,6%** (12 de 17) | ✅ Aprovado |
| **Tempo Médio de Resposta** | $< 10$ segundos | **4,75 segundos** | ✅ Aprovado |
| **Média de Tentativas por Atendimento** | $\le 2$ tentativas | **1,00 tentativa** | ✅ Aprovado |
| **Nota Média de Facilidade de Uso** | $\ge 4,0 / 5,0$ | **4,43 / 5,00** (7 avaliações) | ✅ Aprovado |

### Dúvidas Sem Solução Encontrada e Tratamento Aplicado

Durante os testes, 4 consultas não obtiveram pontuação mínima por estarem fora do escopo do assistente:
1. *"como passar de fase no jogo zelda"* (pergunta fora de contexto)
2. *"que dia é hoje"* (pergunta de utilidade geral)
3. *"como consertar vazamento de cano na rua"* (competência da concessionária de saneamento local)
4. *"onde comprar botijao de gas mais barato"* (preço de mercado livre)

**Melhorias Implementadas a Partir dos Testes:**
- **Direcionamento Didático:** Em vez de retornar mensagem genérica de erro, o assistente passou a listar expressamente as 4 categorias atendidas e sugerir palavras-chave válidas.
- **Diferenciação de Confiança:** Inclusão de alerta de confiança média quando o score fica entre 3 e 5 pontos.
- **Feedback Visual na Calculadora:** Criação de pulso visual (`calc-pulse`) com badge de confirmação e horário da recalibragem para assegurar ao usuário que o cálculo foi atualizado.

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
