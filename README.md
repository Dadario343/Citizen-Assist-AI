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
| **ODS 7** | Energia Limpa e Acessível | Orienta sobre a TSEE (descontos de 35% a 53%), boas práticas de consumo e viabilidade de energia solar. |
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
└── data/
    ├── base_conhecimento.json # 19 orientações cadastradas com todos os 9 campos obrigatórios
    ├── historico.json         # Histórico de atendimentos persistido em JSON (14 registros reais)
    ├── atendimentos.csv       # Histórico exportado com csv.DictWriter (8 colunas)
    └── avaliacoes.json        # Notas de usabilidade coletadas no encerramento (8 avaliações)
```

### 2. Orientação a Objetos e Composição

O sistema adota o padrão de **composição de objetos**:
- `Assistente` **possui uma** instância de `BaseConhecimento` injetada em seu construtor `__init__(self, nome, base)`.
- `BaseConhecimento` **possui uma lista de** instâncias de `Orientacao` em `self.orientacoes`, carregadas do JSON.
- `Orientacao` encapsula os 9 atributos obrigatórios: `id`, `categoria`, `titulo`, `palavras_chave`, `resposta`, `documentos`, `onde`, `fonte`, `verificado_em`.

### 3. Mecanismo de Busca Heurística e Filtragem Relevante

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
- **Filtragem Inteligente de Alternativas:** O sistema exibe o melhor resultado e lista até 2 alternativas adicionais **estritamente se tiverem pontuação relevante (`score >= 3`)**, eliminando recomendações de pontuação espúria.

### 4. Robustez, Proteção LGPD e Navegação

- **Tratamento de Exceções:** O leitor de JSON trata `FileNotFoundError` e `json.JSONDecodeError`, impedindo encerramento abrupto caso a base esteja ausente ou malformatada.
- **Proteção de Dados Pessoais (LGPD):** O método `_contem_dado_pessoal` detecta sequências de 8 ou mais dígitos (como CPF ou telefones) e a presença de `@` (e-mails). Mensagens com esses padrões são bloqueadas e **jamais são gravadas no histórico**.
- **Navegação Categórica e Menus:** Todos os menus e submenus possuem validação de entrada numérica e a opção padronizada **`0` para voltar** ou encerrar.
- **Medição Oficial de Tempo (PCP):** O cronômetro afere exclusivamente o tempo de processamento algorítmico do sistema (`inicio = time.time()` seguido de `tempo = round(time.time() - inicio, 1)`), registrado imediatamente após `self.base.buscar(pergunta)` e `orientacao.exibir()`, sem qualquer piso artificial e sem incluir o tempo humano de leitura ou resposta do usuário, em conformidade com o enunciado da disciplina.

### 5. Registro de Atendimentos, Indicadores e Exportação CSV

- Ao concluir cada busca ou navegação, o atendimento é registrado em `self.historico` e no arquivo `data/historico.json`.
- O método `indicadores()` calcula e projeta os 6 indicadores obrigatórios:
  1. **Taxa de Encontro (%):** Percentual de atendimentos em que uma orientação foi localizada.
  2. **Tempo Médio de Atendimento:** Média em segundos despendida no processamento do atendimento (1 casa decimal).
  3. **Taxa de Acerto (%):** Percentual de atendimentos em que o usuário confirmou que a resposta ajudou.
  4. **Tentativas por Atendimento:** Média de consultas efetuadas por sessão.
  5. **Facilidade de Uso (1 a 5):** Média ponderada das avaliações coletadas na saída (iniciando com lista vazia `[]` sem valores fictícios).
  6. **Lista de Dúvidas Sem Solução:** Termos e consultas que não atingiram pontuação mínima, permitindo curadoria contínua.
- **Exportação CSV com 8 Colunas Oficiais:** Utiliza a biblioteca nativa `csv.DictWriter` com as 8 colunas padronizadas:  
  `data, origem, pergunta, id_orientacao, encontrou, ajudou, tentativas, tempo_segundos`.
- **Desdobramento do Tempo Médio:** O relatório de `indicadores()` exibe o tempo médio consolidado e detalha separadamente o tempo de **busca heurística algorítmica** (consultas por texto) e o tempo de **navegação em categorias** (renderização em tela).

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
- **Investimento:** R$ 0,00 | **Payback:** Imediato.

#### A. Regra Atual Vigente (Lei Federal nº 15.235/2025 — Gratuidade até 80 kWh/mês)
- **Marco Legal:** Em vigor desde 5 de julho de 2025 e consolidada pela **Lei Federal nº 15.235/2025**, a nova regulamentação garante **gratuidade integral (100% de isenção de TE e TUSD)** sobre a faixa de consumo básico até 80 kWh/mês para os beneficiários elegíveis.
- **Estrutura de Faturamento:**
  - Parcela 0 a 80 kWh: 100% de isenção -> **R$ 0,00 (gratuita)**.
  - Excedente 81 a 150 kWh (70 kWh cobrados pela tarifa regular homologada de R$ 0,75/kWh): `70 x 0,75 = R$ 52,50 / mês`.
  - **Fatura mensal estimada:** **R$ 52,50 / mês** -> Economia estimada de **R$ 60,00 / mês (53,3% de redução)**.
- **Critérios Plenos de Elegibilidade (Lei nº 12.212/2010, Lei nº 15.235/2025 e ANEEL):**
  1. Famílias inscritas no Cadastro Único com renda familiar mensal per capita menor ou igual a meio salário mínimo nacional;
  2. Idosos com 65 anos ou mais ou pessoas com deficiência que recebam o Benefício de Prestação Continuada (BPC/LOAS);
  3. Famílias no CadÚnico com renda mensal de até 3 salários mínimos com pessoa portadora de doença ou deficiência cujo tratamento exija o uso continuado de aparelhos elétricos vitais;
  4. Famílias indígenas e quilombolas inscritas no Cadastro Único.
- **Nova Modalidade Adicional (Vigência a partir de Janeiro de 2026) — Desconto Social:**
  - Diretriz do Ministério de Minas e Energia (MME) para famílias inscritas no CadÚnico com renda familiar per capita **entre meio e um salário mínimo** (> 1/2 e <= 1 SM).
  - Isenta a cobrança da Conta de Desenvolvimento Energético (CDE) para consumo até **120 kWh/mês**, proporcionando uma redução média estimada pelo MME de **aproximadamente 11,8%** na tarifa média (o percentual exato varia conforme a estrutura tarifária da distribuidora local; ressalta-se que a isenção de CDE incide sobre encargos setoriais e não representa gratuidade da conta integral).
- **Ressalva Metodológica:** A gratuidade incide sobre o consumo ativo; contas reais continuam sujeitas à Contribuição de Iluminação Pública (COSIP).

#### B. Regime Histórico Anterior (Lei Federal nº 10.438/2002 e Res. ANEEL 1.000/2021)
- *Mantido no assistente exclusivamente para fins de análise comparativa retrospectiva com o regime anterior a julho de 2025:*
  - 0 a 30 kWh (desc. 65%): R$ 7,88 | 31 a 100 kWh (desc. 40%): R$ 31,50 | 101 a 150 kWh (desc. 10%): R$ 33,75
  - **Fatura mensal histórica:** **R$ 73,13 / mês** -> Economia histórica de **R$ 39,37 / mês (35,0% de redução)**.

### 3. Alternativa 2: Microgeração Solar Fotovoltaica Residencial
- **Fórmula de Engenharia:**
  `E = P x H x D x PR = 1,5 kWp x 4,8 kWh/m²/dia x 30 dias x 0,78 = 168,48 kWh/mês (~168,5 kWh/mês)`
  - *Premissas:* Sistema de 1,5 kWp (3 módulos de 500 Wp + microinversor), irradiação média de 4,8 kWh/m²/dia (Atlas Solar / INPE para Sudeste e Centro-Oeste), Performance Ratio de 78%. Atende 100% da demanda de 150 kWh/mês com excedente de 18,5 kWh/mês.
- **Investimento Instalado:** **R$ 7.500,00 a R$ 9.500,00** (Benchmark Greener / ABSOLAR 2024 para sistemas até 2 kWp, média R$ 8.500).
- **Limitações Reais da Lei 14.300/2022 (A conta não zera):**
  - Custo de disponibilidade monofásico obrigatório (30 kWh x R$ 0,75 = R$ 22,50/mês, conforme art. 291 da Res. ANEEL 1.000/2021) + encargos de injeção Fio B + taxa de iluminação pública municipal (COSIP).
  - Conta residual pós-solar estimada: **R$ 22,50 a R$ 35,00/mês**.
  - Economia líquida mensal (tarifa cheia): **R$ 77,50 a R$ 90,00/mês** (68,9% a 80,0% de redução).
- **Payback Simples (Consumidor que paga tarifa cheia R$ 112,50):**
  - Cenário Otimista: `R$ 7.500 / (R$ 90,00 x 12) = 6,94 anos (~6,9 anos)`
  - Cenário Moderado: `R$ 8.500 / (R$ 83,75 x 12) = 8,46 anos (~8,5 anos)`
  - Cenário Conservador: `R$ 9.500 / (R$ 77,50 x 12) = 10,22 anos (~10,2 anos)`
  - Faixa consolidada: **6,9 a 10,2 anos** (cenário intermediário: **8,5 anos**). Vida útil: 25 anos.

- **AVALIAÇÃO CRÍTICA DE ENGENHARIA: Viabilidade do Solar para quem JÁ TEM Tarifa Social:**
  - Se a família de baixa renda já recebe a Tarifa Social (fatura de R$ 73,13 pela Lei 10.438 ou R$ 52,50 pelo modelo vigente de 80 kWh), a fatura mínima pós-solar continua tendo piso em R$ 22,50 a R$ 35,00/mês:
    - Sob a Lei 10.438: economia líquida de apenas `R$ 38,13 a R$ 50,63 / mês` -> **Payback médio de 16,0 anos**.
    - Sob a gratuidade vigente até 80 kWh: economia líquida de apenas `R$ 17,50 a R$ 30,00 / mês` -> **Payback médio de 29,8 anos** (e até **45,2 anos** no cenário conservador)!
  - *Conclusão de Engenharia:* Placas solares próprias têm retorno excessivamente lento e barreira financeira intransponível para famílias no CadÚnico. Para baixa renda, o solar só é viável via subsídios públicos integrais ou cooperativas de energia solar comunitária.

### 4. Alternativa 3: Cenário Combinado (TSEE + Eficiência Residencial)
- **Demonstração Matemática da Redução de 40 kWh/mês (150 para 110 kWh/mês):**
  - *Chuveiro 3.500 W:* 4 pessoas reduzindo banhos de 12 para 8 min/dia -> Economia de **28,00 kWh/mês** (`3,5 x 0,8 x 30 = 84,00 kWh` para `3,5 x 0,533 x 30 = 56,00 kWh`).
  - *Iluminação:* Troca de 4 lâmpadas fluorescentes 25 W por LEDs de 9 W -> Economia de **7,68 kWh/mês** (`12,00 - 4,32 kWh`).
  - *Standby:* Desligamento de TV e receptor (10 W) no filtro de linha nos períodos ociosos (14,4h/dia) -> Economia de **4,32 kWh/mês** (`0,010 kW x 14,4 h x 30 d = 4,32 kWh` para 0,00 kWh).
  - *Total economizado comprovado:* `28,00 + 7,68 + 4,32 = 40,00 kWh/mês`.
- **Fatura Estimada:**
  - No regime de faixas da Lei 10.438: 30 kWh (R$ 7,88) + 70 kWh (R$ 31,50) + 10 kWh (R$ 6,75) = **R$ 46,13/mês** (Economia total de **R$ 66,37/mês — 59,0% de redução** em relação a R$ 112,50).
  - No regime de gratuidade até 80 kWh (excedente de 30 kWh a R$ 0,75): **R$ 22,50/mês** (Economia total de **R$ 90,00/mês — 80,0% de redução** em relação a R$ 112,50).
- **Veredito:** Esta é a **melhor alternativa técnica e financeira** para o cidadão de baixa renda, pois proporciona economia imediata sem custo de instalação.

### 5. Tabelas Comparativas Consolidadas

#### Comparação Direta entre Regra Atual (Lei 15.235/2025) e Regime Histórico (Lei 10.438/2002)

| Cenário de Avaliação | Regra Atual Vigente (Lei 15.235/2025) | Regime Histórico Anterior (Lei 10.438/2002) | Redução Frente à Tarifa Cheia (R$ 112,50) |
|---|:---:|:---:|:---:|
| **Tarifa Social (TSEE), 150 kWh** | **R$ 52,50 / mês** (Economia: R$ 60,00) | **R$ 73,13 / mês** (Economia: R$ 39,37) | **53,3%** (atual) vs. **35,0%** (histórico) |
| **Cenário Combinado (TSEE + Efic.), 110 kWh** | **R$ 22,50 / mês** (Economia: R$ 90,00) | **R$ 46,13 / mês** (Economia: R$ 66,37) | **80,0%** (atual) vs. **59,0%** (histórico) |

#### Matriz Comparativa Consolidada de Todas as Soluções

| Indicador Analisado | Situação Inicial | TSEE Vigente (Lei 15.235) | TSEE Histórica (Lei 10.438) | Solar Residencial (1,5 kWp) | Combinada Vigente (TSEE + Eficiência) | Combinada Histórica (Lei 10.438 + Efic.) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Conta Estimada (R$)** | R$ 112,50 | **R$ 52,50** | R$ 73,13 | R$ 22,50 a R$ 35,00 | **R$ 22,50** | R$ 46,13 |
| **Economia Mensal Estimada** | R$ 0,00 | **R$ 60,00** | R$ 39,37 | R$ 77,50 a R$ 90,00 | **R$ 90,00** | R$ 66,37 |
| **Percentual de Redução** | 0% | **53,3%** | 35,0% | 68,9% a 80,0% | **80,0%** | 59,0% |
| **Investimento Inicial** | R$ 0,00 | R$ 0,00 | R$ 0,00 | R$ 7.500 a R$ 9.500 | R$ 0,00 | R$ 0,00 |
| **Payback (Tarifa Cheia)** | N/A | Imediato | Imediato | 6,9 a 10,2 anos (méd. 8,5) | Imediato | Imediato |
| **Payback (para quem tem TSEE)** | N/A | Imediato | Imediato | 20,8 a 45,2 anos (méd. 29,8) | Imediato | Imediato |
| **CO₂ Evitado Estimado** | 0 kg | Indireto | Indireto | ~6,5 kg CO₂/mês | ~1,5 kg CO₂/mês | ~1,5 kg CO₂/mês |

---

## 🧪 Relatório Completo de Testes com Usuários Reais

Foram conduzidas sessões de teste com **3 participantes externos à equipe** (preservando integralmente o anonimato conforme exigido pelas diretrizes éticas e pela LGPD), totalizando **14 atendimentos registrados** nos arquivos oficiais de auditoria (`data/historico.json` e `data/atendimentos.csv`):

### Perfil Anonimizado dos Participantes

1. **Participante A:** Testou a solicitação da Tarifa Social de Energia Elétrica (TSEE), a busca por redução de consumo no chuveiro elétrico, a consulta de NIS no CadÚnico e avaliou a orientação sobre energia solar para baixa renda.
2. **Participante B:** Testou a emissão do Cartão SUS, postos de vacinação, a emissão da nova Carteira de Identidade Nacional (CIN / RG), o registro de reclamações no PROCON e efetuou uma consulta fora de escopo.
3. **Participante C:** Testou o cálculo de consumo de eletrodomésticos, navegou pelo Estudo Comparativo SERS via menu de categorias, consultou assistência jurídica gratuita na Defensoria Pública, explorou o serviço CAPS na área de Saúde e realizou consulta fora de escopo.

### Tabela de Indicadores Reais Obtidos nos Testes (Cronômetro Oficial Refinado)

| Métrica Avaliada | Dados Reais dos Arquivos | Situação |
|---|:---:|:---:|
| **Total de Atendimentos Realizados** | **14 atendimentos** | ✅ Atende com folga ao mínimo exigido (>= 10) |
| **Respostas Encontradas** | **12 atendimentos (85,7%)** | ✅ Alta taxa de localização |
| **Taxa de Acerto (Orientação Ajudou)** | **12 atendimentos (85,7%)** | ✅ Conteúdo altamente relevante e claro |
| **Tempo Médio de Atendimento do Algoritmo** | **0,0s (< 0,1s)** | ✅ Resposta algorítmica imediata (round a 1 casa decimal conforme enunciado) |
| **Média de Tentativas por Atendimento** | **1,00 tentativa** | ✅ Assertividade imediata na primeira consulta |
| **Avaliações de Facilidade de Uso** | **8 avaliações coletadas \| Média: 4,75 / 5,00** | ✅ Usabilidade de excelência |

### Avaliação Específica de Compreensão e Utilidade (SERS)

A validação do módulo de sustentabilidade energética não se restringiu a números técnicos: foi aplicada uma entrevista semiestruturada de validação conceitual com os 3 participantes logo após a simulação:

1. **Protocolo de Avaliação da Compreensão Teórico-Econômica:**
   - *Pergunta de Verificação:* "Se uma família já é beneficiária da Tarifa Social de Energia, por que a instalação de placas solares no telhado não é a solução financeira prioritária para ela?"
   - *Respostas dos Participantes:*
     - **Participante A:** Respondeu que a conta com Tarifa Social já é muito reduzida (R$ 52,50 na regra atual ou R$ 73,13 no regime histórico), e como a taxa mínima da distribuidora com encargos (R$ 22,50 a R$ 35,00) ainda tem que ser paga todo mês, a economia líquida com o solar seria de apenas R$ 17,50 a R$ 50,63/mês. Como o sistema custa R$ 8.500, a família levaria de 16 a quase 30 anos (e até 45 anos no cenário conservador) para recuperar o dinheiro, o que é inviável para o orçamento vulnerável.
     - **Participante B:** Compreendeu que energia solar para baixa renda só faz sentido se for doada integralmente pelo governo ou em projetos de usinas comunitárias, nunca financiada por conta própria.
     - **Participante C:** Destacou que a demonstração de payback de quase 30 anos (29,8 anos) sob o regime vigente de gratuidade foi o ponto mais revelador do assistente.

2. **Protocolo de Avaliação da Utilidade Prática:**
   - *Pergunta de Verificação:* "As orientações de eficiência propostas (redução de 4 minutos no chuveiro elétrico e desligamento de aparelhos em standby no filtro de linha) são viáveis de serem aplicadas em sua residência?"
   - *Resultado:* 100% dos participantes consideraram as medidas de utilidade imediata, compreendendo que a soma das pequenas ações elimina 40 kWh/mês exatos, permitindo que a conta caia para R$ 22,50/mês (sob a regra vigente da Lei 15.235) ou R$ 46,13/mês (sob o regime histórico) com investimento zero em obras ou equipamentos.

### Dúvidas Sem Solução Registradas no Histórico Real

As 2 dúvidas sem solução registradas propositalmente para teste de limites nos arquivos oficiais foram:
1. *"qual o melhor jogo do ano"* (Consulta de entretenimento fora do escopo de serviços públicos)
2. *"receita de bolo de fuba"* (Consulta culinária fora do escopo de serviços públicos)

Ambas retornaram a mensagem pedagógica instruindo o usuário sobre os 4 eixos atendidos (Documentos, Saúde, Direitos e Energia).

### Comentários Recebidos e Ajustes Realizados

| Situação Testada | Comentário / Observação do Usuário | Ajuste Realizado no Projeto |
|---|---|---|
| **Busca por Vacinação** | Usuário digitou "vacinas" e esperava encontrar orientações de imunização. | Inclusão de "vacinas", "vacina da gripe" e "imunizações" nas palavras-chave da Orientação 7. |
| **Dúvidas Fora de Escopo** | Consultas aleatórias (jogos, receitas) deixavam o usuário sem direcionamento. | Implementação de mensagem didática indicando as 4 categorias atendidas e sugerindo termos válidos. |
| **Calculadora de Energia** | Usuário desejava confirmação visual imediata de que a simulação recalculou. | Criação de pulso visual animado (`calc-pulse`), badge verde de confirmação e timestamp do recálculo. |
| **Busca por Chuveiro e Consumo** | Usuário digitou "meu chuveiro gasta muito como economizar". | Adicionadas palavras-chave específicas nas Orientações 15 e 18 para correspondência direta imediata. |
| **Carrossel da Página Inicial** | O card do slide seguinte ficava minimamente visível na lateral direita em certas larguras. | Inserido `visibility: hidden` e `pointer-events: none` nos slides inativos em `index.html`. |

---

## ⚠️ Limitações do Assistente

1. **Iniciativa Educacional e de Utilidade Pública:** O assistente não emite documentos nem substitui o atendimento oficial prestado pelos órgãos governamentais (Receita Federal, CRAS, UBS, ANEEL).
2. **Escopo Delimitado:** O sistema responde exclusivamente a dúvidas inseridas nos 4 eixos temáticos (Documentos, Saúde, Direitos e Energia). Perguntas fora de escopo são orientadas para os canais competentes.
3. **Estimativas Paramétricas de Energia:** Todas as simulações e paybacks utilizam valores médios referenciais. Os custos reais de conta de luz dependem da concessionária local, tributos (ICMS/PIS/COFINS) e bandeiras tarifárias vigentes.

---

## 📚 Fontes Oficiais e Referências Bibliográficas Específicas

| Órgão / Entidade | Documento, Tabela ou Publicação Oficial de Referência | Detalhamento Metodológico Aplicado | URL Oficial Verificada |
|---|---|---|---|
| **ANEEL** | *Painel de Tarifas de Fornecimento de Energia Elétrica* (Resoluções Homologatórias para o Subgrupo B1 - Residencial Convencional) | Base para a **tarifa paramétrica de R$ 0,75/kWh** (média Brasil). A fatura real inclui ICMS estadual (17-25%), PIS/COFINS (4-9%), bandeiras tarifárias e COSIP municipal. | [gov.br/aneel](https://www.gov.br/aneel/pt-br/assuntos/tarifas/painel-de-tarifas) |
| **ANEEL** | *Resolução Normativa ANEEL nº 1.000/2021* (arts. 177 a 186) e Leis 10.438/2002 e 12.212/2010 | Regulamentação das faixas progressivas e critérios de elegibilidade da Tarifa Social de Energia Elétrica (TSEE). | [gov.br/aneel](https://www.gov.br/aneel/pt-br/assuntos/tarifa-social) |
| **INPE / LABREN** | *Atlas Brasileiro de Energia Solar (2ª Edição, 2017)*, ISBN 978-85-17-00089-8 | **4,80 kWh/m²/dia**: Média anual de irradiação solar global horizontal consolidada para as regiões **Sudeste e Centro-Oeste** (SP, MG e GO). | [labren.ccst.inpe.br](http://labren.ccst.inpe.br/atlas_2017.html) |
| **Greener / ABSOLAR** | *Estudo Estratégico de Geração Distribuída — Mercado Fotovoltaico (Edição 1º Semestre de 2024)* | Tabela de Preço Médio Turnkey Residencial por Faixa de Potência: faixa até 2 kWp com índice entre **R$ 5,00/Wp e R$ 6,33/Wp** (sistema de 1,5 kWp entre R$ 7.500 e R$ 9.500, média R$ 8.500). | [greener.com.br](https://www.greener.com.br) |
| **MCTI / SIRENE** | *Tabela de Fatores Médios de Emissão de CO₂ por Consumo de Energia Elétrica no SIN* (ano-base 2023, consolidado 2024) | Fator oficial médio da matriz elétrica interligada: **0,0385 t CO₂/MWh = 0,0385 kg CO₂/kWh** (utilizado para inventários oficiais de carbono). | [gov.br/mcti](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/dados-e-informacoes/fatores-de-emissao) |
| **EPE / PROCEL** | *Anuário Estatístico de Energia Elétrica 2024* e Metodologias de Consumo Residencial | Referência do consumo médio residencial de 150 kWh/mês para famílias de interesse social. | [epe.gov.br](https://www.epe.gov.br) |
| **Presidência da República** | *Lei Federal nº 14.300/2022* (Marco Legal da Micro e Minigeração Distribuída) | Base legal para o custo de disponibilidade monofásico (30 kWh = R$ 22,50/mês) e transição da TUSD Fio B. | [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm) |
| **Ministério do Desenvolvimento Social** | Diretrizes do Cadastro Único (CadÚnico) e Programa Bolsa Família | Critérios de elegibilidade para a Tarifa Social (renda per capita até 1/2 salário mínimo). | [gov.br/mds](https://www.gov.br/mds/pt-br/acoes-e-programas/bolsa-familia) |
| **Ministério da Saúde** | Meu SUS Digital e Programa Nacional de Imunizações (PNI) | Diretrizes para emissão do Cartão SUS e postos de vacinação. | [gov.br/saude](https://www.gov.br/saude/pt-br) |

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
