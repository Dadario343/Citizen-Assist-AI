# Memorial de Cálculo e Estudo de Sustentabilidade Energética (SERS) ⚡🌿

> **Disciplina:** Soluções em Energias Renováveis e Sustentáveis (SERS)  
> **Global Solution 2026.2 — FIAP**  
> **Projeto:** Citizen Assist AI — Módulo de Eficiência e Transição Energética para Baixa Renda  
> **Integrantes:**  
> - Olavo Dadario Vianna Barreto (RM 569272)  
> - Paulo Henrique Lira Bilac de Araujo (RM 569496)  
> - Pedro Soares de Souza (RM 571285)  

---

## 1. Contexto, Público e Premissas Iniciais

- **Público-alvo:** Famílias brasileiras de baixa renda em vulnerabilidade socioeconômica, inscritas no Cadastro Único (CadÚnico) para Programas Sociais do Governo Federal.
- **Problema Abordado:** **Pobreza energética** — desproporção entre a renda familiar e o custo das faturas de energia elétrica, levando à inadimplência, corte de fornecimento ou comprometimento de gastos com alimentação e saúde.
- **Perfil de Consumo Referencial (Estimativa Paramétrica):**
  - Residência típica: 3 a 4 moradores.
  - Consumo mensal médio adotado: **150 kWh/mês** (estimativa baseada em dados da EPE / Procel para habitações de interesse social).
  - Tarifa média homologada ANEEL (sem bandeiras adicionais): **R$ 0,75 / kWh** (média nacional de distribuidoras urbanas).
  - Custo mensal atual de referência sem benefícios:  
    `Custo Base = 150 kWh/mês x R$ 0,75/kWh = R$ 112,50/mês`

---

## 2. Fator de Emissão Oficial de CO₂ da Matriz Elétrica Nacional

- **Fonte Oficial:** Ministério da Ciência, Tecnologia e Inovação (MCTI / SIRENE) e Empresa de Pesquisa Energética (EPE).
- **Fator Médio do Sistema Interligado Nacional (SIN):**
  - Ano-base 2023/2024: **0,0385 kg CO₂/kWh** (equivalente a 38,5 kg CO₂/MWh).
  - Em períodos de alta geração hidrelétrica e expansão solar/eólica, o SIN atinge marcas entre 28,9 e 38,5 kg CO₂/MWh.
- **Cálculo de Emissões Evitadas:**
  - Sobre a fatura de consumo referencial (150 kWh/mês):  
    `CO₂ evitado = 150 x 0,0385 = 5,78 kg CO₂/mês (~69,3 kg CO₂/ano)`
  - Sobre a geração de um sistema solar de 168,5 kWh/mês:  
    `CO₂ evitado = 168,5 x 0,0385 = 6,49 kg CO₂/mês (~77,8 kg CO₂/ano)`
- **Esclarecimento Técnico sobre o Fator de 0,50 kg CO₂/kWh:**
  O valor de 0,50 kg CO₂/kWh encontrado em algumas literaturas corresponde exclusivamente ao fator de emissão marginal do despacho termelétrico fóssil de ponta (óleo diesel/gás em momentos de escassez hídrica extrema). A matriz elétrica brasileira média é renovável (> 85%), sendo tecnicamente correto utilizar o fator oficial do SIN de **0,0385 kg CO₂/kWh**.

---

## 3. Demonstração Matemática da Redução por Eficiência Energética (150 para 110 kWh/mês)

Abaixo é apresentada a auditoria individual de aparelhos elétricos com memória aritmética rigorosa, fundamentando a redução de **40,0 kWh/mês** sem necessidade de aquisição de placas solares ou obras civis:

| Equipamento Residencial | Potência (W) | Horas/Dia (Antes) | Horas/Dia (Depois) | Consumo Anterior | Consumo Posterior | Economia Mensal Obtida |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Chuveiro Elétrico** | 3.500 W (médio) | 48 min/dia (4 pess. x 12m) = 0,80 h | 32 min/dia (4 pess. x 8m) = 0,533 h | 84,00 kWh/mês | 56,00 kWh/mês | **28,00 kWh/mês** |
| **Iluminação (4 pontos)** | 4x 25 W (fluoresc.) | 4,0 h/dia por lâmpada | 4x 9 W (LED substituído) x 4,0 h/dia | 12,00 kWh/mês | 4,32 kWh/mês | **7,68 kWh/mês** |
| **Aparelhos em Standby** | 10 W (TV + deco) | 14,4 h/dia em standby | 0,0 h/dia (desligados no filtro de linha) | 4,32 kWh/mês | 0,00 kWh/mês | **4,32 kWh/mês** |
| **Demais Aparelhos (Geladeira/Ferro)** | Variável | Uso padrão | Manutenção de borrachas e termostato | 49,68 kWh/mês | 49,68 kWh/mês | 0,00 kWh/mês |
| **TOTAL CONSOLIDADO** | — | — | — | **150,00 kWh/mês** | **110,00 kWh/mês** | **40,00 kWh/mês (26,7%)** |

*Memória de verificação física:*
1. Chuveiro: `3,5 kW x 0,80 h x 30 d = 84,00 kWh` -> `3,5 kW x 0,5333 h x 30 d = 56,00 kWh` (Economia: **28,00 kWh/mês**).
2. Lâmpadas: `4 x 0,025 kW x 4 h x 30 d = 12,00 kWh` -> `4 x 0,009 kW x 4 h x 30 d = 4,32 kWh` (Economia: **7,68 kWh/mês**).
3. Standby: TV (6 W) + receptor de sinal (4 W) somam 10 W em modo de vigília durante 14,4 horas diárias de inatividade (`0,010 kW x 14,4 h x 30 d = 4,32 kWh/mês`). Com o desligamento completo da régua/filtro de linha, o consumo vai a zero absoluto (Economia: **4,32 kWh/mês**).
4. Total economizado: `28,00 + 7,68 + 4,32 = 40,00 kWh/mês`.

---

## 4. Estudo Comparativo das Alternativas

### Alternativa 1: Tarifa Social de Energia Elétrica (TSEE)
- **Marco Legal:** Lei Federal nº 10.438/2002, alterada pela Lei nº 12.212/2010 e regulamentada pela Resolução Normativa ANEEL nº 1.000/2021 (arts. 177 a 186), e proposta de gratuidade do Programa Luz do Povo.
- **Investimento Inicial:** **R$ 0,00** | **Payback:** **Imediato**.
- **Regime Geral Progressivo (Lei 10.438/2002 e Res. ANEEL 1.000):**
  - Faixa 0-30 kWh (65% desc.): `round(30 x 0,75 x 0,35, 2) = R$ 7,88`
  - Faixa 31-100 kWh (40% desc.): `round(70 x 0,75 x 0,60, 2) = R$ 31,50`
  - Faixa 101-150 kWh (10% desc.): `round(50 x 0,75 x 0,90, 2) = R$ 33,75`
  - Nova fatura estimada: **R$ 73,13 / mês** (Economia estimada de **R$ 39,37 / mês** ou **35,0%**).
- **Modelo com Gratuidade até 80 kWh (Luz do Povo, excedente regular a R$ 0,75/kWh):**
  - Parcela 0 a 80 kWh (100% isenção): R$ 0,00
  - Excedente 81 a 150 kWh (70 kWh cobrados pela tarifa normal): `70 x 0,75 = R$ 52,50`
  - Nova fatura estimada: **R$ 52,50 / mês** (Economia estimada de **R$ 60,00 / mês** ou **53,3%**).

---

### Alternativa 2: Microgeração Solar Fotovoltaica Residencial
- **Dimensionamento Técnico do Sistema:**
  - Potência nominal (`P`): **1,5 kWp** (~3 módulos de 500 Wp com microinversor).
  - Irradiação solar de referência (`H`): **4,8 kWh/m²/dia** (média nacional do Atlas Brasileiro de Energia Solar / INPE).
  - Dias no mês (`D`): **30 dias**.
  - Performance Ratio (`PR`): **0,78** (considerando perdas por temperatura, poeira, cabeamento e eficiência do microinversor).
  - **Fórmula de Engenharia:**
    `E = P x H x D x PR = 1,5 x 4,8 x 30 x 0,78 = 168,48 kWh/mês (~168,5 kWh/mês)`
  - *Observação:* A geração mensal calculada (168,5 kWh) cobre 100% da demanda de 150 kWh/mês com excedente de 18,5 kWh/mês injetado na rede.
- **Investimento Instalado (Turnkey):**
  - Faixa de mercado: **R$ 7.500,00 a R$ 9.500,00** (Levantamento Benchmark Greener / ABSOLAR 2024/2025 para sistemas residenciais de até 2 kWp).
- **Limitações Regulatórias e Custo Residual (Lei 14.300/2022):**
  - O sistema fotovoltaico conectado à rede (on-grid) **não zera a fatura**. A conta mínima permanece entre **R$ 20,00 e R$ 35,00 / mês**, composta por:
    1. Custo de disponibilidade monofásico (30 kWh x R$ 0,75 = R$ 22,50/mês).
    2. Transição gradual da remuneração do Fio B da TUSD.
    3. Contribuição para Custeio da Iluminação Pública (COSIP).
- **Payback para Consumidor que Paga Tarifa Cheia (Fatura R$ 112,50):**
  - Economia líquida mensal: **R$ 77,50 a R$ 92,50 / mês** (redução real de 70% a 82%).
  - *Cenário Otimista:* `R$ 7.500 / (R$ 92,50 x 12) = 6,76 anos (~6,8 anos)`
  - *Cenário Moderado:* `R$ 8.500 / (R$ 85,00 x 12) = 8,33 anos (~8,3 anos)`
  - *Cenário Conservador:* `R$ 9.500 / (R$ 77,50 x 12) = 10,22 anos (~10,2 anos)`
  - Faixa consolidada: **6,8 a 10,2 anos** (cenário intermediário: **8,3 anos**).

- **AVALIAÇÃO CRÍTICA DE ENGENHARIA: Viabilidade do Solar para Beneficiários da TSEE:**
  - Se a família de baixa renda já recebe a Tarifa Social, sua fatura já é reduzida:
    - Sob a Lei 10.438: fatura atual de **R$ 73,13 / mês**. A economia mensal gerada pelo solar (fatura mínima de R$ 22,50) seria de apenas:
      `R$ 73,13 - R$ 22,50 = R$ 50,63 / mês` -> **Payback de 14,0 anos** (`R$ 8.500 / (50,63 x 12) = 13,99 anos`).
    - Sob o modelo de gratuidade até 80 kWh: fatura atual de **R$ 52,50 / mês**. A economia mensal gerada pelo solar seria de apenas:
      `R$ 52,50 - R$ 22,50 = R$ 30,00 / mês` -> **Payback de 23,6 anos** (`R$ 8.500 / (30,00 x 12) = 23,61 anos`)!
  - **Conclusão Técnica:** Para famílias de baixa renda no CadÚnico, a aquisição individual de placas solares com recursos próprios é **economicamente desvantajosa e financeiramente inviável** (payback de 14 a 24 anos com investimento inicial proibitivo de R$ 8.500). Placas solares para esse público só fazem sentido em programas sociais de doação pública integral ou cooperativas solares comunitárias.

---

### Alternativa 3: Cenário Combinado (TSEE + Eficiência Energética Residencial)
- Consumo reduzido de 150 para **110 kWh/mês** conforme auditoria da Seção 3.
- **Cálculo da Conta:**
  - *No regime de faixas da Lei 10.438/2002:*
    - 0 a 30 kWh (desc. 65%): R$ 7,88
    - 31 a 100 kWh (desc. 40%): R$ 31,50
    - 101 a 110 kWh (desc. 10%): `round(10 x 0,75 x 0,90, 2) = R$ 6,75`
    - **Fatura estimada: R$ 46,13 / mês** -> **Economia total de R$ 66,37 / mês (59,0% de redução)** em relação aos R$ 112,50.
  - *No regime de gratuidade até 80 kWh (excedente a R$ 0,75):*
    - 0 a 80 kWh = R$ 0,00
    - 81 a 110 kWh (30 kWh x R$ 0,75): `30 x 0,75 = R$ 22,50`
    - **Fatura estimada: R$ 22,50 / mês** -> **Economia total de R$ 90,00 / mês (80,0% de redução)** em relação aos R$ 112,50.
- **Investimento Necessário:** **R$ 0,00** (apenas R$ 30 a R$ 40 na troca gradual das lâmpadas por LED).
- **Veredito:** Esta é comprovadamente a **melhor alternativa técnica, econômica e social** para famílias de baixa renda no Brasil.

---

## 5. Tabela Resumo Consolidada

| Indicador Analisado | Situação Inicial | Alt. 1: TSEE | Alt. 2: Solar 1,5 kWp | Alt. 3: TSEE + Eficiência |
|---|:---:|:---:|:---:|:---:|
| **Conta Estimada (R$/mês)** | R$ 112,50 | R$ 52,50 a R$ 73,13 | R$ 20,00 a R$ 35,00 | **R$ 22,50 a R$ 46,13** |
| **Economia Mensal Estimada** | R$ 0,00 | R$ 39,37 a R$ 60,00 | R$ 77,50 a R$ 92,50 | **R$ 66,37 a R$ 90,00** |
| **Percentual de Redução** | 0% | 35,0% a 53,3% | 70% a 82% | **59,0% a 80,0%** |
| **Investimento Inicial** | R$ 0,00 | R$ 0,00 | R$ 7.500 a R$ 9.500 | **R$ 0,00** |
| **Payback (Consumidor Tarifa Cheia)** | N/A | Imediato | 6,8 a 10,2 anos (méd. 8,3) | **Imediato** |
| **Payback (para quem JÁ TEM TSEE)** | N/A | Imediato | 14,0 a 23,6 anos | **Imediato** |
| **CO₂ Evitado Estimado** | 0 kg | Indireto | ~5,8 a 6,5 kg CO₂/mês | ~1,5 kg CO₂/mês |
| **Viabilidade para Baixa Renda** | Referência | Imediata (CadÚnico) | Inviável sem subsídio | Imediata e Universal |

---

## 6. Referências Normativas e Fontes de Dados

1. **ANEEL:** Resolução Normativa nº 1.000/2021 — Regras de Prestação do Serviço Público de Distribuição de Energia Elétrica. [https://www.gov.br/aneel/pt-br/assuntos/tarifa-social](https://www.gov.br/aneel/pt-br/assuntos/tarifa-social)
2. **Presidência da República:** Lei Federal nº 10.438/2002 e Lei Federal nº 12.212/2010 — Instituem e regulamentam a Tarifa Social de Energia Elétrica (TSEE).
3. **Presidência da República:** Lei Federal nº 14.300/2022 — Marco Legal da Micro e Minigeração Distribuída. [https://www.gov.br/aneel/pt-br/assuntos/geracao-distribuida](https://www.gov.br/aneel/pt-br/assuntos/geracao-distribuida)
4. **MCTI / SIRENE:** Fatores de Emissão de CO₂ do Sistema Interligado Nacional (SIN) — Inventário Nacional de Emissões (Fator médio 2023/2024: 0,0385 kg CO₂/kWh). [https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/dados-e-informacoes/fatores-de-emissao](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/dados-e-informacoes/fatores-de-emissao)
5. **EPE (Empresa de Pesquisa Energética):** Anuário Estatístico de Energia Elétrica e Metodologias de Consumo Residencial. [https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/anuario-estatistico-de-energia-eletrica](https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/anuario-estatistico-de-energia-eletrica)
6. **ABSOLAR / Greener:** Estudo Estratégico de Geração Distribuída e Levantamento de Preços de Sistemas Fotovoltaicos Residenciais (2024/2025). [https://www.absolar.org.br/mercado/geracao-distribuida/](https://www.absolar.org.br/mercado/geracao-distribuida/)
7. **INPE:** Atlas Brasileiro de Energia Solar (2ª Edição) — Dados de irradiação solar média nacional (4,8 kWh/m²/dia). [http://labren.ccst.inpe.br/atlas_2017.html](http://labren.ccst.inpe.br/atlas_2017.html)
