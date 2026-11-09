# Memorial de Cálculo e Estudo de Sustentabilidade Energética (SERS) ⚡🌿

> **Disciplina:** Soluções em Energias Renováveis e Sustentáveis (SERS)  
> **Global Solution 2026.2 — FIAP**  
> **Projeto:** Citizen Assist AI — Módulo de Transição Energética e Combate à Pobreza Energética  
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
  - Consumo mensal médio adotado: **150 kWh/mês** (estimativa baseada em dados históricos da EPE / Procel para habitações de interesse social).
  - Tarifa média homologada ANEEL (sem bandeiras adicionais): **R$ 0,75 / kWh** (média nacional de distribuidoras urbanas).
  - Custo mensal atual de referência sem benefícios:  
    $$\text{Custo Base} = 150\text{ kWh/mês} \times \text{R\$ } 0,75\text{/kWh} = \mathbf{\text{R\$ } 112,50\text{/mês}}$$

---

## 2. Fator de Emissão Oficial de CO₂ da Matriz Elétrica Nacional

- **Fonte Oficial:** Ministério da Ciência, Tecnologia e Inovação (MCTI / SIRENE) e Empresa de Pesquisa Energética (EPE).
- **Fator Médio do Sistema Interligado Nacional (SIN):**
  - Ano-base 2023/2024: **0,0385 kg CO₂/kWh** (equivalente a 38,5 kg CO₂/MWh).
  - Em períodos de alta geração hidrelétrica e expansão solar/eólica, o SIN atinge marcas entre 28,9 e 38,5 kg CO₂/MWh.
- **Cálculo de Emissões Evitadas:**
  - Sobre a fatura de consumo referencial (150 kWh/mês):  
    $$\text{CO}_2\text{ evitado} = 150 \times 0,0385 = \mathbf{5,78\text{ kg CO}_2\text{/mês}} \quad (\approx \mathbf{69,3\text{ kg CO}_2\text{/ano}})$$
  - Sobre a geração de um sistema solar de 168,5 kWh/mês:  
    $$\text{CO}_2\text{ evitado} = 168,5 \times 0,0385 = \mathbf{6,49\text{ kg CO}_2\text{/mês}} \quad (\approx \mathbf{77,8\text{ kg CO}_2\text{/ano}})$$
- **Esclarecimento Técnico sobre o Fator de 0,50 kg CO₂/kWh:**
  O valor de 0,50 kg CO₂/kWh encontrado em algumas literaturas corresponde exclusivamente ao fator de emissão marginal do despacho termelétrico fóssil de ponta (óleo diesel/gás em momentos de escassez hídrica extrema). A matriz elétrica brasileira média é renovável (> 85%), sendo tecnicamente correto utilizar o fator oficial de **0,0385 kg CO₂/kWh**.

---

## 3. Demonstração Matemática da Redução por Eficiência Energética (150 para 110 kWh/mês)

Abaixo é apresentada a auditoria individual de aparelhos elétricos para fundamentar tecnicamente a redução de **40,0 kWh/mês** sem necessidade de aquisição de placas solares ou obras civis:

| Equipamento Residencial | Potência (W) | Horas/Dia (Antes) | Horas/Dia (Depois) | Consumo Anterior | Consumo Posterior | Economia Mensal Obtida |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Chuveiro Elétrico** | 3.800 W (médio) | 48 min/dia (4 pess. x 12m) = 0,80 h | 32 min/dia (4 pess. x 8m) = 0,533 h | 91,2 kWh/mês | 60,8 kWh/mês | **30,4 kWh/mês** |
| **Iluminação (4 pontos)** | 4x 25 W (fluoresc.) | 4,0 h/dia por lâmpada | 4x 9 W (LED substituído) x 4,0 h/dia | 12,0 kWh/mês | 4,3 kWh/mês | **7,7 kWh/mês** |
| **Aparelhos em Standby** | 20 W contínuos | 24 h/dia (standby) | Tomada desligada / filtro de linha | 4,3 kWh/mês | 2,4 kWh/mês | **1,9 kWh/mês** |
| **Outros (Geladeira/Ferro)** | Variável | Uso padrão | Manutenção de borrachas e termostato | 42,5 kWh/mês | 42,5 kWh/mês | 0,0 kWh/mês |
| **TOTAL CONSOLIDADO** | — | — | — | **150,0 kWh/mês** | **110,0 kWh/mês** | **40,0 kWh/mês (26,7%)** |

---

## 4. Estudo Comparativo das Alternativas

### Alternativa 1: Tarifa Social de Energia Elétrica (TSEE)
- **Marco Legal:** Lei Federal nº 10.438/2002, regulamentada pela Resolução Normativa ANEEL nº 1.000/2021 e diretrizes do Programa Luz do Povo.
- **Investimento Inicial:** **R$ 0,00** | **Payback:** **Imediato**.
- **Regime Atualizado (Gratuidade até 80 kWh/mês):**
  - Parcela 0 a 80 kWh (100% isenção): R$ 0,00
  - Parcela 81 a 150 kWh (70 kWh com 40% desc.): $70 \times 0,75 \times 0,60 = \text{R\$ } 31,50$
  - Nova fatura estimada: **R$ 31,50 / mês** (Economia de **R$ 81,00 / mês** ou **72,0%**).
- **Regime Geral Progressivo (Lei 10.438/2002):**
  - Faixa 0-30 kWh (65% desc.): $30 \times 0,75 \times 0,35 = \text{R\$ } 7,88$
  - Faixa 31-100 kWh (40% desc.): $70 \times 0,75 \times 0,60 = \text{R\$ } 31,50$
  - Faixa 101-150 kWh (10% desc.): $50 \times 0,75 \times 0,90 = \text{R\$ } 33,75$
  - Nova fatura estimada: **R$ 73,13 / mês** (Economia de **R$ 39,37 / mês** ou **35,0%**).

---

### Alternativa 2: Microgeração Solar Fotovoltaica Residencial
- **Dimensionamento Técnico do Sistema:**
  - Potência nominal ($P$): **1,5 kWp** (~3 módulos de 500 Wp com microinversor).
  - Irradiação solar de referência ($H$): **4,8 kWh/m²/dia** (média nacional do Atlas Brasileiro de Energia Solar / INPE).
  - Dias no mês ($D$): **30 dias**.
  - Taxa de desempenho ou Performance Ratio ($PR$): **0,78** (considerando perdas por temperatura, poeira, cabeamento CA/CC e eficiência do inversor).
  - **Fórmula de Engenharia:**
    $$E = P \times H \times D \times PR = 1,5 \times 4,8 \times 30 \times 0,78 = \mathbf{168,48\text{ kWh/mês}} \approx \mathbf{168,5\text{ kWh/mês}}$$
  - *Observação:* A geração mensal calculada (168,5 kWh) cobre 100% do consumo do perfil de 150 kWh/mês com excedente de 18,5 kWh/mês injetado na rede. A produção varia conforme orientação azimutal, inclinação do telhado e sazonalidade climática.
- **Investimento Instalado (Turnkey):**
  - Faixa de mercado: **R$ 7.500,00 a R$ 9.500,00** (Levantamento Benchmark Greener / ABSOLAR 2024/2025 para sistemas residenciais de até 2 kWp).
- **Limitações Regulatórias e Custo Residual (Lei 14.300/2022):**
  - O sistema fotovoltaico conectado à rede (on-grid) **não zera a fatura**. A conta mínima permanece entre **R$ 20,00 e R$ 35,00 / mês**, composta por:
    1. Custo de disponibilidade monofásico (30 kWh x R$ 0,75 = R$ 22,50/mês).
    2. Transição gradual da remuneração do Fio B da TUSD.
    3. Contribuição para Custeio da Iluminação Pública (COSIP).
- **Economia Líquida Mensal:** **R$ 77,50 a R$ 92,50 / mês** (redução real de 70% a 82% sobre a fatura original de R$ 112,50).
- **Memória de Cálculo do Payback Simples:**
  - *Cenário Otimista:* $\frac{\text{R\$ } 7.500}{\text{R\$ } 92,50 \times 12} = \mathbf{6,76\text{ anos}} \approx \mathbf{6,8\text{ anos}}$
  - *Cenário Moderado:* $\frac{\text{R\$ } 8.500}{\text{R\$ } 85,00 \times 12} = \mathbf{8,33\text{ anos}} \approx \mathbf{8,3\text{ anos}}$
  - *Cenário Conservador:* $\frac{\text{R\$ } 9.500}{\text{R\$ } 77,50 \times 12} = \mathbf{10,22\text{ anos}} \approx \mathbf{10,2\text{ anos}}$
  - **Faixa Consolidada:** **6,8 a 10,2 anos** (média ponderada: **8,3 anos**). Vida útil dos módulos com garantia linear de fábrica: **25 anos**.

---

### Alternativa 3: Cenário Combinado (TSEE + Eficiência Energética Residencial)
- Consumo reduzido de 150 para **110 kWh/mês** conforme tabela da Seção 3.
- **Cálculo da Conta:**
  - *No regime atualizado de gratuidade até 80 kWh:*
    - 0 a 80 kWh = R$ 0,00
    - 81 a 110 kWh (30 kWh com 40% desc.): $30 \times 0,75 \times 0,60 = \text{R\$ } 13,50$
    - **Conta: R$ 13,50 / mês** $\rightarrow$ **Economia de R$ 99,00 / mês (88% de redução)**.
  - *No regime geral de faixas da Lei 10.438/2002:*
    - 0 a 30 kWh (desc. 65%): R$ 7,88
    - 31 a 100 kWh (desc. 40%): R$ 31,50
    - 101 a 110 kWh (desc. 10%): $10 \times 0,75 \times 0,90 = \text{R\$ } 6,75$
    - **Conta: R$ 46,13 / mês** $\rightarrow$ **Economia de R$ 66,37 / mês (59% de redução)**.
- **Investimento Necessário:** **R$ 0,00** (ou apenas R$ 30 a R$ 40 na troca gradual das lâmpadas).

---

## 5. Tabela Resumo Consolidada

| Indicador Analisado | Situação Inicial | Alt. 1: TSEE | Alt. 2: Solar 1,5 kWp | Alt. 3: TSEE + Eficiência |
|---|:---:|:---:|:---:|:---:|
| **Conta Estimada (R$/mês)** | R$ 112,50 | R$ 31,50 a R$ 73,13 | R$ 20,00 a R$ 35,00 | **R$ 13,50 a R$ 46,13** |
| **Economia Mensal Estimada** | R$ 0,00 | R$ 39,37 a R$ 81,00 | R$ 77,50 a R$ 92,50 | **R$ 66,37 a R$ 99,00** |
| **Percentual de Redução** | 0% | 35,0% a 72,0% | 70% a 82% | **59,0% a 88,0%** |
| **Investimento Inicial** | R$ 0,00 | R$ 0,00 | R$ 7.500 a R$ 9.500 | **R$ 0,00** |
| **Payback Simples** | N/A | Imediato | 6,8 a 10,2 anos (méd. 8,3) | **Imediato** |
| **CO₂ Evitado Estimado** | 0 kg | Indireto | ~5,8 a 6,5 kg CO₂/mês | ~1,5 kg CO₂/mês |
| **Viabilidade Prática** | Referência | Imediata (CadÚnico) | Requer telhado e crédito | Imediata e Universal |

---

## 6. Referências Normativas e Fontes de Dados

1. **ANEEL:** Resolução Normativa nº 1.000/2021 — Regras de Prestação do Serviço Público de Distribuição de Energia Elétrica. [https://www.gov.br/aneel](https://www.gov.br/aneel)
2. **Presidência da República:** Lei Federal nº 10.438/2002 — Institui a Tarifa Social de Energia Elétrica (TSEE).
3. **Presidência da República:** Lei Federal nº 14.300/2022 — Marco Legal da Micro e Minigeracão Distribuída.
4. **MCTI / SIRENE:** Fatores de Emissão de CO₂ do Sistema Interligado Nacional (SIN) — Inventário Nacional de Emissões (2023/2024: 0,0385 kg CO₂/kWh). [https://www.gov.br/mcti](https://www.gov.br/mcti)
5. **EPE (Empresa de Pesquisa Energética):** Anuário Estatístico de Energia Elétrica e Nota Técnica de Consumo Residencial. [https://www.epe.gov.br](https://www.epe.gov.br)
6. **ABSOLAR / Greener:** Estudo Estratégico de Geração Distribuída e Levantamento de Preços de Sistemas Fotovoltaicos Residenciais (2024/2025). [https://www.absolar.org.br](https://www.absolar.org.br)
7. **INPE:** Atlas Brasileiro de Energia Solar (2ª Edição) — Dados de irradiação solar média nacional.
