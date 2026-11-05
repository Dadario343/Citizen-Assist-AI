# Citizen Assist AI - Assistente Digital de Orientação ao Cidadão

> Projeto de programação para a disciplina de tecnologia e sustentabilidade.
> Tema: orientação ao cidadão de baixa renda em documentos, saúde, direitos e energia.

---

## Integrantes

| Nome | RM |
|------|----|
| Olavo Dadario Vianna Barreto | RM 569272 |
| Paulo Henrique Lira Bilac de Araujo | RM 569496 |
| Pedro Soares de Souza | RM 571285 |

---

## Público e Problema Escolhidos

**Público-alvo:** Moradores de baixa renda no Brasil.

Muitas famílias em situação de vulnerabilidade social enfrentam dificuldades para acessar informações sobre:
- **Documentos básicos** (RG, CPF, Carteira de Trabalho) por desconhecimento do processo ou da gratuidade.
- **Saúde pública** (como usar o SUS, onde obter remédios gratuitos, serviços de saúde mental).
- **Direitos sociais** (Bolsa Família, CadÚnico, Defensoria Pública, PROCON).
- **Conta de luz e energia** (Tarifa Social, como economizar, programas de acesso à energia).

A falta de informação clara e acessível resulta em pessoas que pagam por serviços gratuitos, não acessam benefícios aos quais têm direito ou são vulneráveis a cobranças indevidas.

O **Citizen Assist AI** oferece um canal de consulta simples, em linguagem popular, disponível offline, que orienta o cidadão e indica sempre as fontes oficiais.

---

## ODS Relacionados

| ODS | Título | Relação com o projeto |
|-----|--------|----------------------|
| **ODS 1** | Erradicação da Pobreza | Orienta sobre benefícios sociais (Bolsa Família, CadÚnico, CRAS) |
| **ODS 7** | Energia Limpa e Acessível | Informa sobre Tarifa Social, eficiência energética e energia solar |
| **ODS 10** | Redução das Desigualdades | Facilita o acesso à informação para populações vulneráveis |
| **ODS 16** | Paz, Justiça e Instituições Eficazes | Orienta sobre direitos (PROCON, Defensoria Pública, Juizados) |

---

## Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado

### Verificar versão do Python
```bash
python --version
```
ou
```bash
python3 --version
```

### Executar o projeto
```bash
# Entre na pasta do projeto
cd citizen-assist-ai

# Execute o programa principal
python main.py
```

> **Nota:** O programa funciona 100% offline. Nenhuma biblioteca externa é necessária — usa apenas módulos da biblioteca padrão do Python (`json`, `csv`, `re`, `os`, `datetime`, `time`).

### Estrutura de arquivos
```
citizen-assist-ai/
├── main.py                       # Ponto de entrada
├── orientacao.py                 # Classe Orientacao
├── base_conhecimento.py          # Classe BaseConhecimento (carga e busca)
├── assistente.py                 # Classe Assistente (menus e interação)
├── README.md                     # Este arquivo
└── data/
    ├── base_conhecimento.json    # Base com 18 orientações
    ├── historico.json            # Histórico persistente de atendimentos
    └── atendimentos.csv          # Exportação CSV para análise
```

---

## Regra de Pontuação (Sistema de Busca)

O assistente usa um sistema de pontuação para encontrar a orientação mais relevante para cada pergunta:

| Critério | Pontos |
|----------|--------|
| Palavra-chave da orientação encontrada na pergunta | **+3 pontos** por palavra-chave |
| Palavra da pergunta (4+ letras) encontrada no título | **+1 ponto** por palavra |

### Níveis de confiança

| Pontuação | Nível | Significado |
|-----------|-------|-------------|
| ≥ 6 pontos | **ALTA** | Resposta muito provavelmente correta |
| 3 a 5 pontos | **MÉDIA** | Resposta pode ser relevante, verifique |
| < 3 pontos | **BAIXA** | Poucos indícios de relação — tente reformular |
| 0 pontos | — | Não encontrado — sugestão de busca alternativa |

### Normalização
Antes da comparação, o texto é normalizado: convertido para minúsculas, acentos removidos (ex.: "ã" → "a"), pontuação substituída por espaço. Isso garante que "Cartão SUS", "cartao sus" ou "CARTAO SUS" produzam o mesmo resultado.

---

## Análise Energética

> Esta seção integra a disciplina de sustentabilidade energética e cumpre o requisito de análise de alternativas de energia para o público-alvo.

### Contexto

Famílias de baixa renda no Brasil gastam proporcionalmente mais de sua renda com energia elétrica do que famílias de maior renda — fenômeno chamado de **pobreza energética**. Segundo a ANEEL, milhões de famílias elegíveis à Tarifa Social de Energia Elétrica (TSEE) não utilizam o benefício por desconhecimento.

### Consumo de Referência

Uma residência de baixa renda típica (3-4 pessoas) consome aproximadamente **150 kWh/mês**.

| Item | Potência | Uso estimado | Consumo/mês |
|------|----------|-------------|-------------|
| Geladeira antiga | 150 W | 24h/dia | 108 kWh |
| Chuveiro elétrico | 5.500 W | 15 min/dia | 41 kWh |
| TV + iluminação + outros | ~100 W | 6h a 8h/dia | 55 kWh |
| **Total estimado** | | | **~150 kWh/mês** |

**Custo sem desconto:** 150 kWh × R\$0,75/kWh (tarifa média residencial, fonte ANEEL 2024) = **R\$112,50/mês**

---

### Alternativa 1 — Tarifa Social de Energia Elétrica (TSEE)

A TSEE é um subsídio governamental que reduz a conta de luz de famílias inscritas no CadÚnico.

| Faixa de consumo | Desconto |
|-----------------|---------|
| Primeiros 30 kWh | **65%** |
| 31 a 100 kWh | **40%** |
| 101 a 220 kWh | **10%** |
| Acima de 220 kWh | 0% |

**Simulação para 150 kWh/mês:**

| Faixa | kWh | Tarifa original | Desconto | Tarifa com TSEE |
|-------|-----|----------------|----------|----------------|
| 0–30 kWh | 30 | R\$22,50 | 65% | R\$7,88 |
| 31–100 kWh | 70 | R\$52,50 | 40% | R\$31,50 |
| 101–150 kWh | 50 | R\$37,50 | 10% | R\$33,75 |
| **Total** | **150** | **R\$112,50** | | **R\$73,13** |

**Economia estimada: ~R\$39,37/mês (≈35% de redução)**

- **Custo inicial:** R\$0 (apenas inscrição no CadÚnico)
- **Payback:** Imediato
- **Impacto ambiental:** Indireto (não reduz consumo, mas evita inadimplência e corte de energia)
- **Limitação:** Requer inscrição ativa no CadÚnico com renda per capita ≤ ½ salário mínimo

---

### Alternativa 2 — Energia Solar Fotovoltaica Residencial

A geração solar transforma a luz do sol em eletricidade pelos painéis fotovoltaicos instalados no telhado. Com a **Lei 14.300/2022** (Marco Legal da Microgeração Distribuída), o excedente gerado é injetado na rede e creditado na conta de luz.

**Dados técnicos (sistema de 1,5 kWp — adequado para 150 kWh/mês):**

| Parâmetro | Valor |
|-----------|-------|
| Geração estimada | ~180 kWh/mês (Brasil, irradiação média 5,0 kWh/kWp/dia) |
| Custo de instalação (estimado) | R\$7.500 a R\$12.000 |
| Economia mensal na conta | ~R\$90 a R\$112/mês |
| Payback simples | 5 a 7 anos |
| Vida útil dos painéis | 25 anos |
| Redução de CO₂ | ~75 kg CO₂/mês evitados* |

> *Fator de emissão da rede elétrica brasileira: 0,5 kgCO₂/kWh (fonte: ANEEL/EPE, 2024)
> Cálculo: 150 kWh × 0,5 = 75 kg CO₂/mês evitados

**Programas de acesso e financiamento:**
- **Programa Luz para Todos** — para zonas rurais sem acesso à rede
- **Caixa Econômica Federal** — Linha de Crédito para Eficiência Energética e Energia Solar
- **BNDES Finem / FINAME** — financiamento para instaladoras e cooperativas
- **Financiamento direto** com instaladoras credenciadas pela ABSOLAR (parcelas a partir de R\$150/mês)

---

### Tabela Comparativa das Alternativas

| Alternativa | Custo inicial | Economia mensal | Payback | Impacto ambiental | Complexidade |
|-------------|--------------|----------------|---------|------------------|-------------|
| **Tarifa Social (TSEE)** | R\$0 | R\$30–50 | Imediato | Baixo (indireto) | Baixa |
| **Eficiência energética** (LEDs, hábitos) | R\$50–200 | R\$15–30 | 1–6 meses | Médio | Baixa |
| **Energia solar fotovoltaica** | R\$7.500–12.000 | R\$90–112 | 5–7 anos | Alto (direto) | Alta |

---

### Limitações das Alternativas

**Tarifa Social:**
- Requer cadastro ativo no CadÚnico (atualizado há menos de 2 anos)
- Não é automático: o consumidor deve solicitar à distribuidora
- Famílias com consumo > 220 kWh/mês perdem parte do benefício

**Energia Solar:**
- Requer telhado próprio em bom estado (exclui a maioria dos inquilinos)
- Custo inicial elevado, inacessível sem financiamento
- Condomínios exigem aprovação da assembleia
- Produção reduzida em dias nublados/chuvosos

---

### Fontes de Dados — Análise Energética

- ANEEL — Tarifa Social: https://www.gov.br/aneel/pt-br/assuntos/tarifa-social
- ANEEL — Fator de emissão da rede elétrica: https://www.gov.br/aneel/pt-br/centrais-de-conteudos/relatorios-e-indicadores
- EPE — Empresa de Pesquisa Energética: https://www.epe.gov.br
- MME — Ministério de Minas e Energia: https://www.gov.br/mme
- ABSOLAR — Associação Brasileira de Energia Solar: https://www.absolar.org.br
- Lei 14.300/2022 — Marco Legal da Microgeração: https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm

---

## Integração com Outras Disciplinas

Este projeto integra:

1. **Programação em Python** — uso de classes (OOP), manipulação de arquivos JSON e CSV, busca por pontuação, tratamento de exceções.
2. **Sustentabilidade Energética** — análise de consumo residencial, Tarifa Social de Energia Elétrica, geração solar fotovoltaica, cálculo de CO₂ evitado.
3. **Cidadania e Direitos** — base de conhecimento sobre documentos, saúde pública e assistência social, todas com fontes oficiais do governo federal.

---

## Fontes Consultadas

| Fonte | URL |
|-------|-----|
| Portal Gov.br — Emitir Carteira de Identidade (CIN) | https://www.gov.br/pt-br/servicos/emitir-carteira-de-identidade |
| Receita Federal — CPF | https://www.gov.br/receitafederal/pt-br/assuntos/cpf |
| MTE — Carteira de Trabalho Digital | https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/trabalhador/carteira-de-trabalho |
| TSE — e-Título | https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral |
| Gov.br — Certidão de Nascimento | https://www.gov.br/pt-br/servicos/registrar-nascimento |
| Meu SUS Digital | https://www.gov.br/saude/pt-br/assuntos/saude-digital/meu-sus-digital |
| Gov.br — Vacinação | https://www.gov.br/saude/pt-br/vacinacao |
| Farmácia Popular | https://www.gov.br/saude/pt-br/assuntos/farmacia-popular |
| CAPS — Saúde Mental | https://www.gov.br/saude/pt-br/assuntos/saude-mental |
| CRAS | https://www.mds.gov.br |
| Bolsa Família / CadÚnico | https://www.gov.br/mds/pt-br/acoes-e-programas/bolsa-familia |
| Consumidor.gov.br (PROCON) | https://www.consumidor.gov.br |
| Defensoria Pública da União | https://www.dpu.def.br/ |
| ANEEL — Tarifa Social | https://www.gov.br/aneel/pt-br/assuntos/tarifa-social |
| MME — Eficiência Energética | https://www.gov.br/mme/pt-br/assuntos/secretarias/sntep/eficiencia-energetica |
| ANEEL — Geração Distribuída (Solar) | https://www.gov.br/aneel/pt-br/assuntos/geracao-distribuida |
| MME — Luz para Todos | https://www.gov.br/mme/pt-br/assuntos/secretarias/sntep/luz-para-todos |
| ANEEL — Calculadora de Consumo | https://www.aneel.gov.br/calculo-do-consumo |

---

## Resultado dos Testes com Usuários

> *Esta seção deve ser preenchida após a realização dos testes de usabilidade.*

### Indicadores (a preencher após testes)

### Indicadores

| Indicador | Valor |
|-----------|-------|
| Total de atendimentos realizados | 3 |
| Taxa de resposta encontrada (%) | 66,7% (2 de 3) |
| Taxa de satisfação — "ajudou" (%) | 66,7% (2 de 3 / 100% dos que encontraram)|
| Tempo médio de busca (segundos) | 0,15s |
| Nota média de facilidade de uso (1–5) | 4,7 / 5,0 |
| Dúvidas sem solução encontrada | 1 (listada abaixo) |

Dúvida sem solução encontrada:
como dar entrada no seguro desemprego pelo celular (Serviço federal do Ministério do Trabalho e Emprego — fora do escopo inicial de 18 temas).

### Melhorias realizadas após testes

Mensagem Didática para Temas Fora do Escopo:
No caso de dúvidas não cobertas (como seguro-desemprego), além de avisar que o tema não consta na base local, o assistente indica canais oficiais pertinentes (portal gov.br/trabalho e aplicativo da Carteira de Trabalho Digital).
Reconhecimento de Linguagem Popular:
Confirmada a eficácia de sinônimos populares como "desconto na conta de luz" associados ao termo técnico "Tarifa Social de Energia Elétrica (TSEE)".
Estruturação Clara dos Próximos Passos:
A divisão entre "Documentos necessários", "Onde ir/como acessar" e "Fonte oficial" evitou confusão e garantiu que o usuário soubesse exatamente onde buscar o serviço gratuito.
Persistência dos Indicadores:
Os 3 atendimentos já estão salvos e sincronizados nos arquivos data/historico.json e data/atendimentos.csv.

---

## Limitações do Assistente

1. **Não é um canal oficial:** As orientações são educacionais e informativas. Para serviços reais, o cidadão deve sempre acessar os órgãos oficiais indicados.
2. **Base de conhecimento estática:** A base tem 18 orientações fixas. Situações muito específicas ou casos excepcionais podem não ser cobertos.
3. **Sem acesso à internet:** O assistente não consulta sites em tempo real. As informações podem desatualizar com mudanças em legislação ou programas.
4. **Linguagem textual apenas:** Não há suporte a áudio, imagens ou interface gráfica — pode ser uma barreira para pessoas com baixa alfabetização.
5. **Sem personalização geográfica:** As orientações são genéricas para o Brasil. Procedimentos específicos de cada estado ou município não estão cobertos.
6. **Sem integração com sistemas:** O assistente não consegue fazer cadastros, verificar status de benefícios ou agendar serviços — apenas informa onde e como fazê-lo.

---

## Link do Vídeo

[a ser inserido]

---

*Projeto desenvolvido para fins acadêmicos. Todas as informações têm fontes oficiais do governo federal brasileiro (gov.br) e foram verificadas em 05/11/2026.*
#
