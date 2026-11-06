# Citizen Assist AI - Assistente Digital de Orientação ao Cidadão

> Global Solution 2026.2: Pensamento Computacional e Automação com Python & Soluções em Energias Renováveis e Sustentáveis.  
> Tema: Orientação ao cidadão de baixa renda em documentos, saúde pública, direitos sociais e energia sustentável.

---

## Integrantes

| Nome | RM |
|------|----|
| Olavo Dadario Vianna Barreto | RM 569272 |
| Paulo Henrique Lira Bilac de Araujo | RM 569496 |
| Pedro Soares de Souza | RM 571285 |

---

## Público e Problema Escolhidos

**Público-alvo:** Cidadãos e famílias de baixa renda em situação de vulnerabilidade socioeconômica no Brasil.

Muitas famílias brasileiras encontram barreiras severas para acessar seus direitos e serviços públicos básicos, devido à dispersão das informações, linguagem burocrática/técnica e proliferação de páginas não oficiais que cobram por serviços gratuitos. Os principais eixos atendidos são:

1. **Documentos Básicos:** Emissão da primeira ou segunda via de RG (CIN), regularização de CPF, Carteira de Trabalho Digital (CTPS) e Título de Eleitor.
2. **Saúde Pública:** Utilização do SUS, emissão do Cartão Nacional de Saúde (CNS), acesso a vacinas gratuitas do calendário oficial, retirada de medicamentos gratuitos pelo Farmácia Popular / RENAME e atendimento de saúde mental nos CAPS.
3. **Direitos e Assistência Social:** Entrada em programas como Bolsa Família via CadÚnico, atendimento no CRAS, defesa do consumidor lesado pelo PROCON e defensoria pública para justiça gratuita.
4. **Energia e Sustentabilidade:** Enfrentamento da **pobreza energética**, esclarecendo o acesso à Tarifa Social de Energia Elétrica (TSEE), cálculo real de consumo de eletrodomésticos, dicas práticas de eficiência energética e viabilidade de fontes renováveis (energia solar fotovoltaica residencial).

O **Citizen Assist AI** funciona como um assistente digital em linha de comando (terminal), 100% offline, seguro, transparente, sem coleta de dados pessoais (em conformidade com a LGPD) e fundamentado em fontes oficiais governamentais verificadas.

---

## ODS Relacionados

| ODS | Título | Relação com o projeto |
|-----|--------|----------------------|
| **ODS 1** | Erradicação da Pobreza | Facilita o acesso a benefícios sociais essenciais (Bolsa Família, CadÚnico, CRAS) |
| **ODS 7** | Energia Limpa e Acessível | Orienta sobre descontos na conta de luz (Tarifa Social), eficiência energética e adoção de energia solar |
| **ODS 10** | Redução das Desigualdades | Democratiza o acesso a informações gratuitas de cidadania para populações vulneráveis |
| **ODS 16** | Paz, Justiça e Instituições Eficazes | Guia o cidadão sobre canais de garantia de direitos (PROCON, Defensoria Pública, Consumidor.gov) |

---

## Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado.
- Nenhuma dependência externa necessária (utiliza exclusivamente módulos padrão: `json`, `csv`, `re`, `os`, `datetime`, `time`, `sys`).

### Executando o programa
```bash
# Clone ou acesse o diretório do projeto
cd Citizen-Assist-AI-main

# Execute o assistente
python main.py
```
*(No Linux ou macOS, utilize `python3 main.py`)*

> **Novidade:** A opção **4 — Análise Energética** do menu principal exibe a comparação completa e fundamentada das alternativas para redução da conta de luz, com cálculos em tempo real (SERS — Soluções em Energias Renováveis e Sustentáveis).

### Estrutura do Repositório
```
citizen-assist-ai/
├── main.py                       # Ponto de entrada do programa
├── orientacao.py                 # Classe Orientacao (dados e exibição)
├── base_conhecimento.py          # Classe BaseConhecimento (leitura JSON, normalização e busca)
├── assistente.py                 # Classe Assistente (atendimento, indicadores, histórico e CSV)
├── README.md                     # Documentação completa e resultados dos testes
└── data/
    ├── base_conhecimento.json    # Base com 19 orientações em 4 categorias
    ├── historico.json            # Histórico persistente de atendimentos (JSON)
    ├── atendimentos.csv          # Exportação estruturada para análise (CSV)
    └── avaliacoes.json           # Registro de notas de facilidade de uso (1 a 5)
```

---

## Arquitetura Orientada a Objetos e Composição

O sistema adota estritamente os princípios de Orientação a Objetos por **composição**:

```
Assistente
└── base: BaseConhecimento
    └── orientacoes: [Orientacao, Orientacao, Orientacao, ...]
```

### 1. `Orientacao` (em `orientacao.py`)
- **Atributos:** `id`, `categoria`, `titulo`, `palavras_chave`, `resposta`, `documentos`, `onde`, `fonte`, `verificado_em`.
- **Métodos:**
  - `exibir()`: Formata e imprime na tela o cartão da orientação com quebra de linha harmoniosa, marcadores de documentos, canal oficial, data de verificação e aviso educativo obrigatório de transparência.

### 2. `BaseConhecimento` (em `base_conhecimento.py`)
- **Atributos:** `caminho`, `orientacoes` (lista de instâncias de `Orientacao`).
- **Métodos:**
  - `carregar()`: Lê `data/base_conhecimento.json` com tratamento de arquivos ausentes ou corrompidos (`JSONDecodeError`).
  - `categorias()`: Retorna lista ordenada de categorias únicas disponíveis.
  - `por_categoria(categoria)`: Filtra as orientações da categoria solicitada.
  - `pontuar(pergunta, orientacao)`: Calcula a pontuação com base nas regras do desafio.
  - `buscar(pergunta)`: Retorna tuplas ordenadas `(score, orientacao)` da maior para a menor pontuação.

### 3. `Assistente` (em `assistente.py`)
- **Atributos:** `nome`, `base` (composição com `BaseConhecimento`), `historico` (persistência carregada do `historico.json`), `notas_facilidade`, `nota_facilidade`.
- **Métodos:**
  - `perguntar()`: Conduz o atendimento por texto livre, avalia confiança (ALTA / MÉDIA / Não encontrei), exibe resposta, alternativas e colhe feedback.
  - `navegar()`: Navegação por categorias e tópicos numerados com "0 para voltar".
  - `registrar()`: Grava cada atendimento com `data`, `origem`, `pergunta`, `id_orientacao`, `encontrou`, `ajudou`, `tentativas` e `tempo_segundos` em `data/historico.json`.
  - `indicadores()`: Processa e exibe em tela todos os indicadores estatísticos e lista de dúvidas não solucionadas.
  - `exportar_csv()`: Exporta os atendimentos consolidados para `data/atendimentos.csv` via `csv.DictWriter`.

---

## Regra de Pontuação e Busca Inteligente

A busca adota o algoritmo heurístico definido na especificação da Global Solution:

1. **Normalização (`normalizar`):**
   - Converte o texto para minúsculas;
   - Remove todos os acentos ortográficos (ex.: `á`, `à`, `ã`, `â`, `é`, `ê`, `í`, `ó`, `õ`, `ô`, `ú`, `ç`);
   - Substitui sinais de pontuação (`?!.,;:()[]{}"'/-_`) por espaços;
   - Envolve o texto normalizado em espaços nas extremidades (`' ' + ' '.join(...) + ' '`) para conferência precisa de palavras e expressões compostas completas.

2. **Cálculo da Relevância (`pontuar`):**
   - **+3 pontos** para cada palavra-chave da orientação identificada dentro da pergunta do cidadão;
   - **+1 ponto** para cada palavra da pergunta (com 4 letras ou mais) encontrada no título da orientação.

3. **Níveis de Confiança:**
   - **Pontuação ≥ 6:** Confiança **ALTA** (exibição imediata com alta precisão);
   - **Pontuação de 3 a 5:** Confiança **MÉDIA** (orientação pertinente exibida);
   - **Pontuação < 3 (ou 0):** **Não encontrei** (mensagem amigável orientando o cidadão a reformular, procurar o CRAS ou navegar pelas categorias temáticas).

---

## Análise Energética e Sustentabilidade (GS Soluções em Energias Renováveis)

> **Contribuição Técnica:** Aplicação prática dos conceitos de potência, consumo de energia elétrica, eficiência energética e microgeração renovável fotovoltaica para combater a vulnerabilidade das famílias atendidas.

### 1. Contexto e Necessidade Energética
Famílias de baixa renda comprometem entre 10% e 25% de sua renda mensal exclusivamente com a conta de luz. Muitas desconhecem as tarifas subsidiadas por lei ou como os hábitos diários e aparelhos obsoletos disparam o consumo. O **Citizen Assist AI** capacita o cidadão a:
- Calcular matematicamente o consumo de seus aparelhos em kWh e R\$;
- Acessar a Tarifa Social (TSEE);
- Adotar medidas de eficiência sem custo;
- Avaliar a viabilidade de instalar placas solares fotovoltaicas (fonte renovável).

### 2. Análise de Consumo de Referência
Para uma residência unifamiliar típica de baixa renda (3 a 4 moradores), o consumo médio é de **150 kWh/mês**.

| Aparelho | Potência (W) | Tempo de Uso Diário | Consumo Mensal (kWh) | % da Conta |
|----------|--------------|---------------------|----------------------|------------|
| Geladeira (1 porta / ciclo médio) | 120 W | Compressor ativo ~8,33 h/dia | 90,00 kWh | 60,0% |
| Chuveiro Elétrico | 5.500 W | 15 min/dia (0,25 h) | 41,25 kWh | 27,5% |
| TV LED + Iluminação LED | ~100 W | ~6,25 h/dia | 18,75 kWh | 12,5% |
| **Consumo Médio Real** | — | — | **150,00 kWh/mês** | **100,0%** |

*Tarifa média residencial de referência ANEEL (sem impostos adicionais de bandeira):* **R\$ 0,75 por kWh**.  
*Custo base mensal:* 150 kWh × R\$ 0,75 = **R\$ 112,50 / mês**.

### 3. Comparação de Alternativas

#### Alternativa 1: Tarifa Social de Energia Elétrica (TSEE) — Subsídio Social
- **Como funciona:** Desconto progressivo concedido pelo Governo Federal via CadÚnico:
  - 0 a 30 kWh/mês: **65% de desconto**
  - 31 a 100 kWh/mês: **40% de desconto**
  - 101 a 220 kWh/mês: **10% de desconto**
- **Cálculo para 150 kWh/mês:**
  - Faixa 1 (30 kWh): 30 × R\$ 0,75 × (1 - 0,65) = **R\$ 7,88**
  - Faixa 2 (70 kWh): 70 × R\$ 0,75 × (1 - 0,40) = **R\$ 31,50**
  - Faixa 3 (50 kWh): 50 × R\$ 0,75 × (1 - 0,10) = **R\$ 33,75**
  - **Total da Conta com TSEE:** **R\$ 73,13 / mês**
  - **Economia mensal:** R\$ 112,50 - R\$ 73,13 = **R\$ 39,37 / mês (35% de economia)**
- **Investimento inicial:** **R\$ 0,00** (apenas manter o CadÚnico ativo no CRAS).
- **Payback:** **Imediato**.
- **Impacto ambiental:** Indireto (reduz a inadimplência e garante segurança energética).

#### Alternativa 2: Energia Solar Fotovoltaica Residencial — Fonte Renovável
- **Como funciona:** Painéis solares convertem irradiação em eletricidade; sob o Marco Legal da Microgeração (Lei 14.300/2022), o excedente vira crédito compensatório na distribuidora.
- **Dimensionamento Técnico (para suprir 150 kWh/mês):**
  - Sistema de **1,5 kWp** (~3 a 4 módulos fotovoltaicos de 450W + microinversor).
  - Irradiação média solar no Brasil: 5,0 kWh/m²/dia.
  - Geração estimada: **~180 kWh/mês** (cobre 100% do consumo residencial com margem).
- **Cálculo Econômico:**
  - Investimento estimado: R\$ 7.500 a R\$ 9.500 (com instalação e homologação).
  - Economia mensal na conta: ~R\$ 95,00 a R\$ 112,00 / mês.
  - Payback simples: **5,5 a 7,0 anos** (vida útil dos módulos: 25 anos).
  - Linhas de microcrédito verde acessíveis (Caixa Habitação / Pronaf / Cooperativas de crédito com parcelas que se pagam pela própria economia).
- **Impacto Ambiental:**
  - Fator de emissão da rede elétrica brasileira (SIN - Sistema Interligado Nacional): **~0,50 kg CO₂ / kWh gerado**.
  - **CO₂ evitado:** 150 kWh × 0,50 kg = **75 kg de CO₂ evitados por mês** (quase **1 tonelada de CO₂ evitada por ano** por família!).

#### Tabela Comparativa Consolidada

| Parâmetro | Situação Atual (Rede Padrão) | Alternativa 1: Tarifa Social (TSEE) | Alternativa 2: Energia Solar Fotovoltaica | Alternativa Combinada (TSEE + Solar Comunitária) |
|---|---|---|---|---|
| **Custo Inicial** | R\$ 0 | **R\$ 0** | R\$ 7.500 – R\$ 9.500 | R\$ 0 (assinatura social) |
| **Gasto Mensal** | R\$ 112,50 | **R\$ 73,13** | R\$ 15,00 – R\$ 20,00 (taxa mínima) | R\$ 55,00 |
| **Economia Mensal** | R\$ 0 | **R\$ 39,37 (35%)** | **R\$ 92,50 – R\$ 97,50 (85%)** | R\$ 57,50 (51%) |
| **Payback** | N/A | **Imediato** | **5,5 a 7,0 anos** | Imediato |
| **Fonte Renovável?**| Mista (hidro/térmica) | Mista | **100% Solar Limpa** | **100% Renovável** |
| **Redução de CO₂** | 0 kg/mês | Indireto | **75 kg CO₂/mês evitado** | **75 kg CO₂/mês evitado** |
| **Viabilidade Baixa Renda** | Padrão | **Excelente (imediata)** | Requer financiamento ou modelo comunitário | Alta viabilidade futura |

### 4. Condições e Limitações
- As estimativas não constituem garantia de economia idêntica, pois variam conforme a concessionária regional, impostos locais (ICMS, PIS/COFINS), custo de iluminação pública e sazonalidade climática (dias nublados/chuvosos).
- A Tarifa Social exige manutenção da renda per capita de até meio salário mínimo e atualização bienal no CadÚnico.
- A energia solar residencial exige telhado próprio estruturalmente apto e com boa insolação, limitando o uso imediato por moradores de imóveis alugados (para os quais a eficiência energética e a Tarifa Social são as soluções prioritárias).

### 5. Fundamentação das Premissas e Metodologia

| Premissa | Valor Adotado | Fonte e Justificativa |
|----------|--------------|----------------------|
| Consumo residencial de referência | 150 kWh/mês | Perfil típico 3-4 moradores de baixa renda conforme dados de consumo médio residencial da ANEEL (Resolução Normativa 1000/2021) e relatório de Pobreza Energética do MME (2022): famílias de baixa renda consomem entre 100 e 200 kWh/mês |
| Tarifa média residencial | R$ 0,75/kWh | Tarifa média residencial nacional sem bandeira tarifária (ANEEL — Relatório de Tarifas, 2024); valores regionais variam de R$ 0,56 a R$ 0,99/kWh |
| Irradiação solar média (Brasil) | 5,0 kWh/m²/dia | Atlas Solarimétrico do Brasil (INMET/CRESESB); média nacional válida para dimensionamento conservador em regiões Sudeste/Centro-Oeste/Nordeste |
| Fator de emissão da rede elétrica | 0,50 kg CO₂/kWh | Fator médio de emissão do Sistema Interligado Nacional (SIN) — Relatório de Referência do Inventário Nacional: MCTI/SEEG, edição 2024 |
| Descontos da Tarifa Social (TSEE) | 65% / 40% / 10% | Faixas definidas na Lei 10.438/2002, regulamentadas pelo Decreto 7.583/2011 e pelas Resoluções Normativas ANEEL n.º 1.000/2021 e subsequentes, vigentes em 2026 |
| Custo e dimensionamento solar (1,5 kWp) | R$ 7.500–9.500 | Levantamento de preço médio de mercado ABSOLAR (2024); sistema composto por 3-4 módulos de 450 Wp + microinversor + instalação + homologação distribuidora |

> **Nota metodológica:** Os cálculos foram realizados com Python (módulo `math` não necessário — operações aritméticas diretas) e replicados no método `analise_energetica()` da classe `Assistente` para garantir transparência e reprodutibilidade. Todos os valores podem ser verificados diretamente pelo usuário executando a opção 4 do menu principal.

---

## Resultado dos Testes com Usuários Reais

Seguindo estritamente as diretrizes da seção 9 da GS, foram executadas **4 sessões completas de testes com usuários reais externos à equipe**, totalizando **15 atendimentos registrados**, ultrapassando a meta mínima de 10 atendimentos e 3 pessoas. Os registros foram conduzidos preservando o anonimato dos participantes (sem coleta ou armazenamento de nomes, CPFs ou dados pessoais sensíveis).

### Tabela Geral de Indicadores Consolidados

| Indicador Obrigatório | Valor Obtido nos Testes | Descrição / Metodologia |
|-----------------------|-------------------------|-------------------------|
| **Total de atendimentos realizados** | **15** | 6 perguntas diretas e 9 navegações por categoria |
| **Resposta encontrada (%)** | **73,3% (11 de 15)** | Atendimentos com orientação localizada na base |
| **Taxa de acerto ("ajudou") (%)** | **66,7% (10 de 15)** | 90,9% de satisfação entre as respostas encontradas |
| **Tempo médio de atendimento (busca/leitura)** | **4,6 s** | Medição em segundos (`time.time()`) |
| **Tentativas médias por atendimento** | **1,0 tentativa** | Eficiência na recuperação da orientação |
| **Facilidade de uso média (escala 1 a 5)** | **4,0 / 5,0** | Avaliações coletadas: [5, 3, 3, 5] |

### Detalhamento das Sessões de Teste

1. **Sessão 1 (Usuário Externo 1 — 5 atendimentos):**
   - *Atendimento 1:* Pergunta: *"quais são os tipos de energia limpa no Brasil?"* → Não encontrada inicialmente (palavra-chave não cadastrada).
   - *Atendimentos 2 a 5:* Navegação com sucesso em *"Como calcular consumo de eletrodomésticos"*, *"CAPS"*, *"Cartão SUS"* e *"Bolsa Família"*. Todas ajudaram o usuário (`ajudou = True`).
   - *Avaliação de facilidade de uso:* **5/5**.

2. **Sessão 2 (Usuário Externo 2 — 3 atendimentos):**
   - *Atendimento 1:* Pergunta fora de escopo: *"Qual a data de lançamento de Zelda Ocarina of time?"* → Corretamente identificada como não encontrada com sugestão de categorias.
   - *Entrada inválida testada:* No menu de categorias, digitou *"Qual o valor energético da banana?"*, tratada pelo sistema com aviso amigável sem interromper a execução.
   - *Atendimentos 2 e 3:* Navegação com sucesso em *"Vacinação gratuita"* e *"PROCON"*. Ambas ajudaram (`ajudou = True`).
   - *Avaliação de facilidade de uso:* **3/5**.

3. **Sessão 3 (Usuário Externo 3 — 4 atendimentos):**
   - *Atendimento 1:* Pergunta direta: *"procon"* → Encontrada com Confiança MÉDIA (4 pontos), ajudou o usuário.
   - *Atendimento 2:* Pergunta direta: *"sus"* → Encontrada com Confiança MÉDIA (3 pontos), ajudou o usuário.
   - *Atendimento 3:* Pergunta direta: *"vacinas"* → Não encontrada inicialmente (base possuía apenas *"vacina"* no singular).
   - *Atendimento 4 (reteste pós-melhoria de palavra-chave):* Pergunta direta: *"vacinas"* → Encontrada com sucesso na orientação 7 (Vacinação gratuita pelo SUS), respondendo à dúvida do cidadão (`ajudou = True`, tempo: 10.0s).
   - *Avaliação de facilidade de uso:* **3/5**.

4. **Sessão 4 (Usuário Externo 4 — 3 atendimentos):**
   - *Atendimento 1:* Pergunta: *"que dia é hoje"* → Não encontrada (fora de escopo).
   - *Entrada inválida testada:* Digitou texto no menu de categorias (*"quais saos as 4 orientaçoes dentro de direitos?"*), tratada pelo assistente com instrução numérica.
   - *Atendimentos 2 e 3:* Navegação por *"Bolsa Família"* (ajudou) e *"Tirar o RG"* (não ajudou para o caso específico daquele cidadão).
   - *Avaliação de facilidade de uso:* **5/5**.

### Dúvidas Sem Solução Encontrada Identificadas nos Testes

| Pergunta Registrada | Tipo | Diagnóstico do Teste |
|---------------------|------|----------------------|
| `quais são os tipos de energia limpa no Brasil?` | Pertinente (Energia) | A base possuía informações de energia solar, mas faltavam sinônimos como *"energia limpa"* e *"fontes renováveis"*. |
| `vacinas` | Pertinente (Saúde) | A base possuía apenas o termo no singular (*"vacina"*). Pela regra de correspondência exata de palavras, a flexão no plural gerou score 0. |
| `estou com dor de garganta o que preciso fazer` | Pertinente (Saúde) | Digitada durante a pausa de tela. Revelou que cidadãos buscam orientação por sintomas comuns para saber quando e onde ir na UBS. |
| `Qual a data de lançamento de Zelda Ocarina of time?` | Fora de escopo | Pergunta sobre games. O assistente agiu perfeitamente sugerindo as áreas oficiais atendidas. |
| `que dia é hoje` | Fora de escopo | Consulta utilitária de relógio/calendário. Recusada amigavelmente pelo assistente. |

---

## Melhorias Implementadas Após os Testes

Com base nas evidências coletadas, realizamos melhorias estruturais no código e na base de dados:

1. **Expansão de Palavras-Chave no JSON (`data/base_conhecimento.json`):**
   - **Vacinação (ID 7):** Inclusão de flexões e termos populares: `"vacinas"`, `"tomar vacina"`, `"vacinar"`, `"posto de vacina"`, `"gotinha"`, `"caderneta de vacinacao"`. Após a alteração, a busca por *"vacinas"* passa a pontuar e ser localizada com sucesso!
   - **Energia Renovável (ID 16):** Adicionadas as expressões `"energia limpa"`, `"energias limpas"`, `"energia renovavel"`, `"energias renovaveis"`, `"fontes renovaveis"`, `"tipos de energia"`, `"tipos de energia limpa"`. A pergunta *"quais são os tipos de energia limpa no Brasil?"* agora atinge **11 pontos** (Confiança ALTA) e exibe as orientações de energia solar e fontes renováveis!
   - **Atendimento de Saúde e Sintomas (ID 6):** Inclusão de termos como `"dor"`, `"dor de garganta"`, `"doente"`, `"sintomas"`, `"consulta medica"`, `"posto de saude"`, `"ubs"`, orientando o cidadão doente a se dirigir à UBS portando RG e Cartão SUS.
   - **Revisão Integral das 19 Orientações:** Adicionadas formas plurais e termos populares em todas as orientações (ex: *"documentos"*, *"segunda via"*, *"remedios"*, *"desconto luz"*).

2. **Correção do Contador de Tentativas (`tentativas`) em `assistente.py`:**
   - *Problema detectado:* O contador não era reiniciado entre dúvidas resolvidas sucessivas no mesmo loop, acumulando tentativas indevidas.
   - *Solução:* Reset explícito (`tentativas = 0`) após a conclusão bem-sucedida de cada atendimento.

3. **Correção e Ajuste da Medição de Tempo (`tempo_segundos`):**
   - *Problema detectado:* O timer original capturava apenas os milissegundos da busca em memória, arredondando sempre para `0.0s`.
   - *Solução:* O temporizador `inicio = time.time()` passou a registrar a duração completa do atendimento e leitura da orientação até o feedback do cidadão, gerando tempos reais (ex.: 3.2s a 5.1s) e arredondando com `round(..., 1)` conforme especificado no item 8 da GS.

4. **Persistência de Histórico e Indicadores:**
   - O assistente agora carrega os atendimentos de `data/historico.json` e notas de `data/avaliacoes.json` na inicialização, permitindo visualizar os indicadores consolidados a qualquer momento no menu principal.

---

## Fontes Consultadas

| Órgão / Plataforma | Descrição do Conteúdo | URL Oficial |
|-------------------|----------------------|-------------|
| **Portal Gov.br** | Carteira de Identidade Nacional (CIN) | https://www.gov.br/pt-br/servicos/emitir-carteira-de-identidade |
| **Receita Federal** | Inscrição e Regularização de CPF | https://www.gov.br/receitafederal/pt-br/assuntos/cpf |
| **Ministério do Trabalho e Emprego** | Carteira de Trabalho Digital (CTPS) | https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/trabalhador/carteira-de-trabalho |
| **TSE** | Autoatendimento Eleitoral e e-Título | https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral |
| **Ministério da Saúde** | Aplicativo Meu SUS Digital e CNS | https://www.gov.br/saude/pt-br/assuntos/saude-digital/meu-sus-digital |
| **Ministério da Saúde** | Calendário Nacional de Vacinação | https://www.gov.br/saude/pt-br/vacinacao |
| **Ministério da Saúde** | Programa Farmácia Popular do Brasil | https://www.gov.br/saude/pt-br/assuntos/farmacia-popular |
| **Ministério da Saúde** | Política Nacional de Saúde Mental e CAPS | https://www.gov.br/saude/pt-br/assuntos/saude-mental/sobre-a-politica-nacional-de-saude-mental/caps |
| **Ministério do Desenvolvimento Social** | CRAS e Rede Socioassistencial | https://www.mds.gov.br/webarq/vmc/webarquivos/CRAS/index.html |
| **Ministério do Desenvolvimento Social** | Bolsa Família e Cadastro Único (CadÚnico) | https://www.gov.br/mds/pt-br/acoes-e-programas/bolsa-familia |
| **Secretaria Nacional do Consumidor** | Defesa do Consumidor e PROCON | https://www.consumidor.gov.br |
| **Defensoria Pública da União** | Assistência Jurídica Gratuita | https://www.dpu.def.br/ |
| **ANEEL** | Tarifa Social de Energia Elétrica (TSEE) | https://www.gov.br/aneel/pt-br/assuntos/tarifa-social |
| **ANEEL** | Marco Legal da Microgeração Solar (Lei 14.300/2022) | https://www.gov.br/aneel/pt-br/assuntos/geracao-distribuida |
| **Ministério de Minas e Energia** | Eficiência Energética e Programa Procel | https://www.gov.br/mme/pt-br/assuntos/secretarias/sntep/eficiencia-energetica |
| **Ministério de Minas e Energia** | Programa Nacional Luz para Todos | https://www.gov.br/mme/pt-br/assuntos/secretarias/sntep/luz-para-todos |
| **ANEEL** | Metodologia e Calculadora de Consumo Elétrico | https://www.aneel.gov.br/calculo-do-consumo |
| **EPE / ABSOLAR** | Dados de Irradiação Solar e Emissões do SIN | https://www.epe.gov.br e https://www.absolar.org.br |

---

## Limitações do Assistente

1. **Canal Informativo Educacional:** O assistente não é um canal de atendimento oficial da administração pública e não realiza agendamentos, inscrições nem expedição de documentos por si só.
2. **Base de Conhecimento Offline:** A base conta com 19 orientações essenciais estruturadas localmente. Alterações legislativas ou administrativas posteriores à data de verificação exigem atualização do arquivo JSON.
3. **Escopo Focado:** Dúvidas fora dos 4 eixos temáticos (como curiosidades gerais ou serviços de terceiros) não são respondidas.
4. **Sem Tratamento Fonético Profundo:** A busca baseia-se em normalização (remoção de acentos e pontuação) e regras exatas de palavras-chave. Erros severos de digitação (ex: *"vassina"* ou *"remedyu"*) dependem da ampliação constante do dicionário de palavras-chave.

---

## Link do Vídeo Técnico

- **Link no YouTube (Vídeo Não Listado):** `[A ser inserido após a gravação pela equipe]`
- **Duração prevista:** Entre 5 e 8 minutos (cumprindo todos os 8 itens obrigatórios do roteiro da GS).

---

## Entrega Acadêmica (.txt para o Portal FIAP)

```text
Nome do assistente: Citizen Assist AI
Público atendido: Moradores de baixa renda no Brasil (orientação em documentos, saúde, direitos e sustentabilidade energética)
Integrantes e RM:
- Olavo Dadario Vianna Barreto (RM 569272)
- Paulo Henrique Lira Bilac de Araujo (RM 569496)
- Pedro Soares de Souza (RM 571285)
Link do repositório GitHub: https://github.com/Dadario343/Citizen-Assist-AI
Link do vídeo técnico no YouTube: [Inserir URL do vídeo não listado]
```
