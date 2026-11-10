# Memorial de Cálculo e Estudo de Sustentabilidade Energética (SERS) ⚡🌿

> **Disciplina:** Soluções em Energias Renováveis e Sustentáveis (SERS)  
> **Global Solution 2026.2 — FIAP**  
> **Projeto:** Citizen Assist AI — Módulo de Eficiência e Transição Energética para Baixa Renda  
> **Integrantes:**  
> - Olavo Dadario Vianna Barreto (RM 569272)  
> - Paulo Henrique Lira Bilac de Araujo (RM 569496)  
> - Pedro Soares de Souza (RM 571285)  

---

## 1. Contexto, Público e Premissas Metodológicas

- **Público-alvo:** Famílias brasileiras em situação de vulnerabilidade socioeconômica, elegíveis ou inscritas no Cadastro Único (CadÚnico) para Programas Sociais do Governo Federal.
- **Problema Abordado:** **Pobreza energética** — desproporção crítica entre a renda familiar disponível e os custos de acesso à eletricidade essencial, acarretando riscos de corte de fornecimento, inadimplência e supressão de necessidades vitais como alimentação e medicamentos.
- **Perfil de Consumo Paramétrico de Referência:**
  - Residência padrão: 3 a 4 moradores.
  - Consumo mensal adotado: **150 kWh/mês** (estimativa paramétrica alinhada ao consumo residencial médio de famílias de interesse social segundo a EPE - Empresa de Pesquisa Energética e dados do PROCEL).
  - Tarifa referencial adotada: **R$ 0,75 / kWh**.

> [!IMPORTANT]
> **Esclarecimento Técnico sobre a Premissa Tarifária (R$ 0,75/kWh):**  
> O valor de R$ 0,75/kWh é uma **premissa de simulação paramétrica**, e **não uma tarifa universal**.  
> Ele é fundamentado no *Painel de Tarifas de Fornecimento de Energia Elétrica da ANEEL* (Subgrupo Tarifário B1 - Residencial Convencional, média ponderada das distribuidoras brasileiras).  
> A fatura real varia consideravelmente de acordo com a área de concessão (concessionária local) e inclui componentes regulatórios e tributários não uniformes:
> 1. **Tributos Incidentes:** ICMS estadual (alíquotas de 17% a 25%), PIS/PASEP e COFINS federais (alíquotas efetivas de ~4% a 9%);
> 2. **Bandeiras Tarifárias:** Sistema de Bandeiras Tarifárias da ANEEL (Bandeira Verde sem acréscimo; Amarela ou Vermelha Patamares 1 e 2 gerando acréscimos a cada 100 kWh);
> 3. **Encargos Municipais:** Contribuição de Iluminação Pública (CIP / COSIP), instituída por legislações de cada município e cobrada diretamente na fatura de energia;
> 4. **Custo de Disponibilidade:** Valor mínimo faturável conforme o padrão de ligação (30 kWh monofásico, 50 kWh bifásico, 100 kWh trifásico).  
> 
> *Custo mensal base da simulação:* `150 kWh/mês x R$ 0,75/kWh = R$ 112,50/mês`.

---

## 2. Fator de Emissão Oficial de CO₂ da Matriz Elétrica Nacional

- **Fonte Oficial Específica:** Ministério da Ciência, Tecnologia e Inovação (MCTI / SIRENE) — *Tabela de Fatores Médios Mensais e Anuais de Emissão de CO₂ por Consumo de Energia Elétrica no Sistema Interligado Nacional (SIN)*.
- **Fator Consolidado Adotado:**
  - Ano-base 2023 (publicação consolidada 2024 do MCTI para inventários do GHG Protocol): **0,0385 t CO₂/MWh**, correspondente a **0,0385 kg CO₂/kWh** (ou 38,5 g CO₂/kWh).
- **Cálculo Rigoroso de Emissões Evitadas:**
  - **Sobre a demanda evitada por eficiência (40 kWh/mês):**  
    `CO₂ evitado = 40,0 kWh/mês x 0,0385 kg CO₂/kWh = 1,54 kg CO₂/mês (~18,5 kg CO₂/ano)`
  - **Sobre o consumo mensal total de 150 kWh/mês:**  
    `CO₂ associado = 150 kWh/mês x 0,0385 kg CO₂/kWh = 5,78 kg CO₂/mês (~69,3 kg CO₂/ano)`
  - **Sobre a geração solar de 168,5 kWh/mês injetada:**  
    `CO₂ evitado = 168,48 kWh/mês x 0,0385 kg CO₂/kWh = 6,49 kg CO₂/mês (~77,8 kg CO₂/ano)`
- **Esclarecimento Técnico sobre Literatura Divergente (Fator de 0,50 kg CO₂/kWh):**  
  Em trabalhos acadêmicos genéricos é comum encontrar o valor de 0,50 kg CO₂/kWh. Esse índice representa o fator de emissão marginal do despacho termelétrico fóssil de ponta (óleo/carvão em bandeiras de escassez hídrica severa). Como o SIN brasileiro possui mais de 85% de geração renovável média anual (hidráulica, eólica, solar e biomassa), utilizar 0,50 kg CO₂/kWh superestimaria o benefício ecológico em mais de 12 vezes. A métrica tecnicamente legítima é o fator oficial do SIRENE/MCTI de **0,0385 kg CO₂/kWh**.

---

## 3. Demonstração Matemática da Eficiência Energética (150 para 110 kWh/mês)

Abaixo é apresentada a auditoria individual de equipamentos com rigor aritmético, justificando a meta de economia de **40,0 kWh/mês** sem exigir reformas prediais nem instalação de módulos solares:

| Equipamento Residencial | Potência (W) | Horas/Dia (Antes) | Horas/Dia (Depois) | Consumo Anterior | Consumo Posterior | Economia Mensal Obtida |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Chuveiro Elétrico** | 3.500 W (potência média na chave morna/verão) | 48 min/dia (4 pess. x 12m) = 0,80 h | 32 min/dia (4 pess. x 8m) = 0,533 h | 84,00 kWh/mês | 56,00 kWh/mês | **28,00 kWh/mês** |
| **Iluminação (4 lâmpadas)** | 4x 25 W (fluorescentes compactas) | 4,0 h/dia por lâmpada | 4x 9 W (LED substituído) x 4,0 h/dia | 12,00 kWh/mês | 4,32 kWh/mês | **7,68 kWh/mês** |
| **Aparelhos em Standby** | 10 W (TV 6 W + decodificador 4 W) | 14,4 h/dia em standby ocioso | 0,0 h/dia (desligados no interruptor de filtro de linha) | 4,32 kWh/mês | 0,00 kWh/mês | **4,32 kWh/mês** |
| **Demais Cargas (Geladeira/Ferro)** | Variável | Padrão Procel | Otimização de termostato e vedação | 49,68 kWh/mês | 49,68 kWh/mês | 0,00 kWh/mês |
| **TOTAL CONSOLIDADO** | — | — | — | **150,00 kWh/mês** | **110,00 kWh/mês** | **40,00 kWh/mês (26,7%)** |

*Memória de verificação física:*
1. **Chuveiro elétrico:** `3,5 kW x 0,80 h x 30 d = 84,00 kWh` reduziu para `3,5 kW x 0,5333 h x 30 d = 56,00 kWh` -> Economia: **28,00 kWh/mês**.
2. **Lâmpadas:** `4 x 0,025 kW x 4 h x 30 d = 12,00 kWh` reduziu para `4 x 0,009 kW x 4 h x 30 d = 4,32 kWh` -> Economia: **7,68 kWh/mês**.
3. **Consumo Vampiro (Standby):** TV moderna em espera consome ~6 W; receptor de TV a cabo/satélite consome ~4 W. Somados totalizam 10 W durante 14,4 horas por dia em que a família está dormindo ou fora de casa:  
   `0,010 kW x 14,4 h/dia x 30 dias = 4,32 kWh/mês`.  
   Ao desligar os equipamentos em um filtro de linha/régua com interruptor, o consumo cai a zero absoluto -> Economia: **4,32 kWh/mês**.
4. **Soma Consolidada:** `28,00 + 7,68 + 4,32 = 40,00 kWh/mês exatos`.

---

## 4. Estudo Comparativo das Alternativas

### Alternativa 1: Tarifa Social de Energia Elétrica (TSEE)
- **Investimento Inicial:** **R$ 0,00** | **Payback:** **Imediato**.

#### A. Regra Atual Vigente (Lei Federal nº 15.235/2025 — Gratuidade até 80 kWh/mês)
- **Marco Legal:** Em vigor desde 5 de julho de 2025 e consolidada pela **Lei Federal nº 15.235/2025**, a nova regulamentação da TSEE estabeleceu gratuidade plena sobre a faixa de consumo básico de eletricidade para famílias vulneráveis.
- **Estrutura de Faturamento:**
  - Parcela de 0 a 80 kWh (100% de isenção de TE e TUSD): **R$ 0,00 (gratuita)**.
  - Parcela excedente de 81 a 150 kWh (70 kWh faturados pela tarifa cheia a R$ 0,75/kWh): `70 x R$ 0,75 = R$ 52,50 / mês`.
  - **Fatura mensal estimada:** **R$ 52,50 / mês**.
  - **Economia obtida:** `R$ 112,50 - R$ 52,50 = R$ 60,00 / mês` (redução de **53,3%**).
- **Critérios Obrigatórios de Elegibilidade:**
  1. Família inscrita no Cadastro Único com renda familiar mensal per capita de até meio salário mínimo nacional;
  2. Idosos com 65 anos ou mais ou pessoas com deficiência que recebam o Benefício de Prestação Continuada (BPC/LOAS);
  3. Famílias no CadÚnico com renda de até 3 salários mínimos com pessoa dependente de aparelhos médicos elétricos contínuos de suporte à vida.
- **Nova Modalidade Adicional (Vigência a partir de Janeiro de 2026) — "Desconto Social":**
  - Instituído pelas novas diretrizes do Ministério de Minas e Energia (MME), o **Desconto Social** contempla famílias inscritas no CadÚnico com renda familiar per capita **entre meio e um salário mínimo** (> 1/2 e <= 1 SM).
  - Garante a isenção dos encargos da Conta de Desenvolvimento Energético (CDE) para consumo até **120 kWh/mês**, proporcionando uma redução média de 15% a 20% na fatura para famílias que antes não eram atendidas pela TSEE tradicional.
- **Ressalva Metodológica sobre Encargos:** A gratuidade recai sobre o consumo faturado de energia ativa (TE/TUSD); faturas reais continuam sujeitas à cobrança municipal da Contribuição de Iluminação Pública (CIP/COSIP).

#### B. Regime Histórico Anterior (Lei Federal nº 10.438/2002 e Resolução ANEEL nº 1.000/2021)
- **Status:** *Mantido exclusivamente para fins de análise comparativa retrospectiva com o regime anterior a julho de 2025.*
- **Memória de Cálculo das Faixas de Desconto:**
  - Faixa 0 a 30 kWh (desconto de 65%): `round(30 x 0,75 x 0,35, 2) = R$ 7,88`
  - Faixa 31 a 100 kWh (desconto de 40%): `round(70 x 0,75 x 0,60, 2) = R$ 31,50`
  - Faixa 101 a 150 kWh (desconto de 10%): `round(50 x 0,75 x 0,90, 2) = R$ 33,75`
  - **Fatura mensal histórica:** `7,88 + 31,50 + 33,75 = R$ 73,13 / mês`.
  - **Economia histórica obtida:** `R$ 112,50 - R$ 73,13 = R$ 39,37 / mês` (redução de **35,0%**).

---

### Alternativa 2: Microgeração Solar Fotovoltaica Residencial
- **Dimensionamento Técnico de Engenharia:**
  - Potência nominal (`P`): **1,5 kWp** (~3 módulos fotovoltaicos de 500 Wp com microinversor centralizado).
  - Irradiação solar diária média (`H`): **4,8 kWh/m²/dia**.
    - *Região de Referência do INPE:* Adotou-se a média anual consolidada do plano horizontal para as regiões **Sudeste e Centro-Oeste** (faixa de latitudes entre -19° e -23°, representativa dos estados de São Paulo, Minas Gerais e Goiás segundo o *Atlas Brasileiro de Energia Solar - 2ª Edição, INPE/LABREN, 2017*).
  - Dias no período (`D`): **30 dias**.
  - Performance Ratio / Taxa de Desempenho Global (`PR`): **0,78** (considerando perdas térmicas nos módulos, poeira/sujidade, cabeamento CC/CA e rendimento do inversor).
  - **Fórmula de Engenharia:**  
    `E = P x H x D x PR = 1,5 kWp x 4,8 kWh/m²/dia x 30 dias x 0,78 = 168,48 kWh/mes (~168,5 kWh/mês)`  
    *(Atende 100% dos 150 kWh/mês de consumo com excedente de 18,5 kWh/mês injetado na rede).*

- **Investimento Turnkey de Instalação:**
  - **Fonte Específica:** *Estudo Estratégico de Geração Distribuída — Mercado Fotovoltaico (Greener, Edição 1º Semestre de 2024)*, em parceria com a ABSOLAR.
  - **Tabela de Referência:** Tabela de Preço Médio de Integração Residencial por Faixa de Potência (R$/Wp). Para sistemas de até 2 kWp, o preço médio turnkey varia de **R$ 5,00/Wp a R$ 6,33/Wp**:
    - Cenário Otimista: `1.500 Wp x R$ 5,00/Wp = R$ 7.500,00`
    - Cenário Moderado: `1.500 Wp x R$ 5,67/Wp = R$ 8.500,00`
    - Cenário Conservador: `1.500 Wp x R$ 6,33/Wp = R$ 9.500,00`

- **Limitações Regulatórias e Custo Residual (Lei nº 14.300/2022):**
  - O sistema fotovoltaico on-grid **não zera a conta do consumidor**. O custo residual mensal varia entre **R$ 20,00 e R$ 35,00/mês**, composto obrigatoriamente por:
    1. Custo de disponibilidade monofásico (30 kWh x R$ 0,75 = R$ 22,50/mês);
    2. Transição gradual da remuneração do Fio B da TUSD (Art. 27 da Lei 14.300/2022);
    3. Contribuição de Iluminação Pública (COSIP).

- **Payback para Consumidor Comum que Paga Tarifa Plena (Fatura de R$ 112,50):**
  - Economia mensal líquida: **R$ 77,50 a R$ 92,50 / mês** (redução de 70% a 82%).
  - *Cenário Otimista:* `R$ 7.500 / (R$ 92,50 x 12) = 6,76 anos (~6,8 anos)`
  - *Cenário Moderado:* `R$ 8.500 / (R$ 85,00 x 12) = 8,33 anos (~8,3 anos)`
  - *Cenário Conservador:* `R$ 9.500 / (R$ 77,50 x 12) = 10,22 anos (~10,2 anos)`
  - Média de retorno simples: **8,3 anos** (vida útil dos módulos de 25 anos com garantia de 80% de potência residual).

- **AVALIAÇÃO CRÍTICA DE ENGENHARIA: Inviabilidade do Solar para Beneficiários da TSEE:**
  - Se a família de baixa renda já está cadastrada na Tarifa Social, sua conta já é subsidiada. Ao instalar o sistema solar, a fatura mínima residual continua sendo a taxa de disponibilidade (30 kWh = R$ 22,50/mês):
    - **No regime da Lei 10.438 (fatura de R$ 73,13):**  
      A economia gerada pelo sistema solar é apenas: `R$ 73,13 - R$ 22,50 = R$ 50,63 / mês`.  
      `Payback = R$ 8.500 / (50,63 x 12) = 13,99 anos (~14,0 anos)`.
    - **No modelo com gratuidade até 80 kWh (fatura de R$ 52,50):**  
      A economia gerada pelo sistema solar é apenas: `R$ 52,50 - R$ 22,50 = R$ 30,00 / mês`.  
      `Payback = R$ 8.500 / (30,00 x 12) = 23,61 anos (~23,6 anos)`!
  - **Diagnóstico Técnico Conclusivo:**  
    O investimento individual em energia solar por famílias vulneráveis é **antieconômico e inviável**. O payback ultrapassa uma década e meia (e atinge praticamente a vida útil dos módulos sob a gratuidade), com desembolso imediato de R$ 8.500 que inexiste no orçamento de baixa renda. A transição energética desse público deve ocorrer por políticas de estado (ex: programa federal Luz para Todos Solar, miniusinas comunitárias compartilhadas), nunca por endividamento privado.

---

### Alternativa 3: Cenário Combinado (TSEE + Eficiência Energética Residencial)
- Consumo reduzido de 150 para **110 kWh/mês** com as ações de R$ 0 de investimento da Seção 3.
- **Fatura Resultante:**
  - **No regime geral da Lei 10.438/2002:**
    - Faixa 0-30 kWh (desc. 65%): R$ 7,88
    - Faixa 31-100 kWh (desc. 40%): R$ 31,50
    - Faixa 101-110 kWh (desc. 10%): `round(10 x 0,75 x 0,90, 2) = R$ 6,75`
    - **Fatura mensal estimada: R$ 46,13 / mês** -> **Economia total de R$ 66,37 / mês (59,0% de redução)** frente aos R$ 112,50 iniciais.
  - **No regime de gratuidade até 80 kWh (excedente a R$ 0,75):**
    - 0 a 80 kWh (isenção integral): R$ 0,00
    - 81 a 110 kWh (30 kWh excedentes a R$ 0,75): `30 x 0,75 = R$ 22,50`
    - **Fatura mensal estimada: R$ 22,50 / mês** -> **Economia total de R$ 90,00 / mês (80,0% de redução)** frente aos R$ 112,50 iniciais.
- **Investimento:** **R$ 0,00** (apenas R$ 30 a R$ 40 na troca gradual das lâmpadas por LED).
- **Veredito:** O Cenário Combinado é a melhor solução imediata para a cidadania: resolve a vulnerabilidade da conta no curto prazo sem gerar endividamento.

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
| **CO₂ Evitado Estimado** | 0 kg | Indireto | ~6,5 kg CO₂/mês | ~1,5 kg CO₂/mês |
| **Viabilidade para Baixa Renda** | Referência | Imediata (CadÚnico) | Inviável sem subsídio | Imediata e Universal |

---

## 6. Referências Normativas e Bibliográficas Específicas

1. **Legislação Federal e ANEEL — Tarifa Social e Desconto Social:**
   - *Lei Federal nº 15.235, de 2025*: Consolida a gratuidade da Tarifa Social de Energia Elétrica sobre os primeiros 80 kWh/mês para famílias de baixa renda (em vigor desde julho de 2025).
   - *Diretrizes MME / ANEEL (Janeiro de 2026)*: Regulamentação da modalidade Desconto Social com isenção da CDE até 120 kWh/mês para renda entre 1/2 e 1 salário mínimo.
   - *Resolução Normativa ANEEL nº 1.000, de 7 de dezembro de 2021*: Estabelece as regras de prestação do serviço público de distribuição de energia elétrica (artigos 177 a 186 dedicados à TSEE).
   - *Painel de Tarifas de Fornecimento de Energia Elétrica da ANEEL*: Tabela de Tarifas Médias Homologadas para Distribuidoras de Energia Elétrica - Subgrupo B1 (Residencial Convencional, média Brasil adotada como premissa paramétrica de R$ 0,75/kWh). [https://www.gov.br/aneel/pt-br/assuntos/tarifas/painel-de-tarifas](https://www.gov.br/aneel/pt-br/assuntos/tarifas/painel-de-tarifas)
2. **Presidência da República — Legislação Federal:**
   - *Lei Federal nº 10.438, de 26 de abril de 2002*: Dispõe sobre a expansão da oferta de energia elétrica emergencial e cria a Tarifa Social de Energia Elétrica.
   - *Lei Federal nº 12.212, de 20 de janeiro de 2010*: Modifica a Lei nº 10.438/2002 e redefine os critérios de elegibilidade socioeconômica da TSEE.
   - *Lei Federal nº 14.300, de 6 de janeiro de 2022*: Institui o Marco Legal da Microgeração e Minigeração Distribuída e o Sistema de Compensação de Energia Elétrica (SCEE).
3. **INPE — Instituto Nacional de Pesquisas Espaciais / LABREN:**
   - PEREIRA, E. B. et al. *Atlas Brasileiro de Energia Solar*, 2ª Edição. São José dos Campos: INPE, 2017. ISBN 978-85-17-00089-8.
   - Dados de irradiação solar global horizontal média diária anual: 4,80 kWh/m²/dia, correspondente à média histórica da faixa geográfica das regiões **Sudeste e Centro-Oeste** (SP/MG/GO). [http://labren.ccst.inpe.br/atlas_2017.html](http://labren.ccst.inpe.br/atlas_2017.html)
4. **MCTI / SIRENE — Ministério da Ciência, Tecnologia e Inovação:**
   - *Tabela de Fatores Médios Mensais e Anuais de Emissão de CO₂ por Consumo de Energia Elétrica no Sistema Interligado Nacional (SIN)*. Coordenação-Geral de Ciência do Clima e Sustentabilidade / SIRENE. Brasília: MCTI, ano-base 2023 (publicação consolidada 2024 para cálculo de inventários de emissões). Fator médio do SIN: **0,0385 t CO₂/MWh (0,0385 kg CO₂/kWh)**. [https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/dados-e-informacoes/fatores-de-emissao](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/dados-e-informacoes/fatores-de-emissao)
5. **Greener & ABSOLAR — Associação Brasileira de Energia Solar Fotovoltaica:**
   - *Estudo Estratégico de Geração Distribuída — Mercado Fotovoltaico (Edição 1º Semestre de 2024)*. São Paulo: Greener, 2024.
   - Tabela de Preço Médio de Integração Turnkey Residencial por Faixa de Potência: faixa até 2 kWp com índice entre R$ 5,00/Wp e R$ 6,33/Wp (sistemas de 1,5 kWp orçados entre R$ 7.500 e R$ 9.500, média R$ 8.500). [https://www.greener.com.br](https://www.greener.com.br) | [https://www.absolar.org.br](https://www.absolar.org.br)
6. **EPE — Empresa de Pesquisa Energética:**
   - *Anuário Estatístico de Energia Elétrica 2024* (ano-base 2023) e *Balanço Energético Nacional (BEN)*. Rio de Janeiro: EPE/MME, 2024. Dados de perfil de consumo por classe residencial e composição da matriz elétrica nacional. [https://www.epe.gov.br](https://www.epe.gov.br)
