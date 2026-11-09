# Citizen Assist AI — Portal Web de Orientação ao Cidadão 🌐

> **Global Solution 2026.2:** Pensamento Computacional & Soluções em Energias Renováveis e Sustentáveis (SERS).  
> **Tema:** Orientação ao cidadão de baixa renda em documentos, saúde pública, direitos sociais e alternativas sustentáveis na conta de luz.

---

## Integrantes

| Nome | RM |
|------|----|
| Olavo Dadario Vianna Barreto | RM 569272 |
| Paulo Henrique Lira Bilac de Araujo | RM 569496 |
| Pedro Soares de Souza | RM 571285 |

---

## 🚀 Acesso Online (GitHub Pages)

A aplicação web está pronta para execução online sem necessidade de instalação:

👉 **[Acessar Citizen Assist AI Web](https://dadario343.github.io/Citizen-Assist-AI/)**

---

## Público e Problema Escolhidos

**Público-alvo:** Cidadãos e famílias de baixa renda em situação de vulnerabilidade socioeconômica no Brasil.

Milhões de famílias brasileiras enfrentam severas barreiras para exercer sua cidadania e usufruir de direitos essenciais por conta de informações dispersas, linguagem técnica burocrática e proliferação de intermediários não oficiais que cobram por serviços que são 100% gratuitos.

O **Citizen Assist AI** resolve esse desafio por meio de uma aplicação web moderna, responsiva, ágil e segura, estruturada em **4 eixos fundamentais**:

1. **📄 Documentos Básicos:** Emissão da primeira via e segunda via de RG (CIN – Carteira de Identidade Nacional), inscrição e regularização de CPF, Carteira de Trabalho Digital (CTPS) e Título de Eleitor.
2. **🏥 Saúde Pública (SUS):** Emissão do Cartão Nacional de Saúde (CNS / Meu SUS Digital), agendamento em UBS, calendário de vacinação gratuita, medicamentos gratuitos pela Farmácia Popular / RENAME e atendimento especializado de saúde mental nos CAPS.
3. **⚖️ Direitos & Cidadania:** Entrada no Cadastro Único (CadÚnico), concessão do Bolsa Família, assistência social nos CRAS, abertura de reclamações de consumo no PROCON/Consumidor.gov e assistência jurídica gratuita pela Defensoria Pública.
4. **💡 Energia Sustentável & Eficiência:** Combate direto à **pobreza energética**, orientando sobre o desconto de até 65% na Tarifa Social de Energia Elétrica (TSEE), cálculo real de consumo de eletrodomésticos em kWh e viabilidade de energia solar fotovoltaica residencial.

---

## ODS Relacionados (Objetivos de Desenvolvimento Sustentável da ONU)

| ODS | Título | Relação Direta com o Projeto |
|-----|--------|------------------------------|
| **ODS 1** | Erradicação da Pobreza | Facilita a entrada em benefícios sociais de transferência de renda (Bolsa Família, CadÚnico, CRAS). |
| **ODS 7** | Energia Limpa e Acessível | Orienta sobre descontos na conta de luz (Tarifa Social), eficiência energética e microgeração solar residencial. |
| **ODS 10** | Redução das Desigualdades | Democratiza o acesso a orientações confiáveis e gratuitas para populações em vulnerabilidade socioeconômica. |
| **ODS 16** | Paz, Justiça e Instituições Eficazes | Guia o cidadão até os canais formais de garantia de direitos (PROCON, Defensoria Pública, Juizados Especiais). |

---

## Funcionalidades da Aplicação Web

### 1. 📢 Carrossel Integrado de Destaque (Hero Banner)
- **Slide 1 (Boas-vindas):** Apresentação clara do assistente, identificação segura de utilidade pública e atalhos rápidos para tirar dúvidas ou simular energia.
- **Slide 2 (Atendimento em Destaque):** Prova social e transparência com indicadores em tempo real (Total de atendimentos resolvidos, tempo médio de resposta de ~4.6s, 100% de disponibilidade e índice de satisfação do cidadão).
- **Slide 3 (Informação Segura, Sempre):** Compromissos éticos e de segurança (100% gratuito, conformidade total com a LGPD sem coleta de dados sensíveis, fundamentação em fontes regulamentadas e relatórios para acompanhamento).
- **Controles Intuitivos:** Navegação por setas, paginação por pontos com indicador ativo e transição automática suave a cada 7 segundos.

### 2. 💬 Chat Inteligente de Orientação
- **Algoritmo Heurístico de Pontuação:** Processa dúvidas em linguagem natural pontuando palavras-chave (+3 pontos) e termos de título (+1 ponto), com normalização de texto (remoção de acentos e caracteres especiais).
- **Diferenciação Clara de Respostas:**
  - *Correspondência direta (Confiança Alta — score ≥ 6):* "Encontrei essa informação referente à sua pergunta:".
  - *Informação relacionada (Confiança Média — score 3 a 5):* "Não encontrei a informação exata sobre o assunto, mas encontrei essa informação relacionada:".
  - *Sem correspondência (score < 3):* Guia didaticamente o usuário sobre as categorias e sugere termos válidos.
- **Feedback Visual (Fade-out):** Efeito de contraste suave na bolha de resposta para confirmar instantaneamente a entrega da informação.
- **Coleta de Satisfação:** Botões de avaliação interativa (*"Essa orientação respondeu sua dúvida? 👍 Sim / 👎 Não"*).
- **Proteção de Privacidade (LGPD):** Bloqueio preventivo automático para mensagens contendo 8 ou mais dígitos (como CPF ou telefone) ou `@` (e-mail), protegendo o cidadão sem registrar dados pessoais.

### 3. 🗂️ Navegação Direta por Categorias
- Abas para explorar os 19 tópicos sem digitação livre, divididos entre **Documentos**, **Saúde**, **Direitos** e **Energia**.
- Exibição de cartões detalhados com lista de documentos exigidos, locais de atendimento presencial e links diretos para canais de serviço.

### 4. ⚡ Calculadora de Consumo e Tarifa Social (SERS)
- Adição dinâmica de eletrodomésticos com potência em Watts (W), horas diárias de uso e quantidade.
- **Cálculo de Consumo Mensal (kWh/mês)** pela metodologia oficial da ANEEL.
- **Simulação da Tarifa Social (TSEE):** Aplicação das faixas progressivas de desconto por lei (65% até 30 kWh, 40% de 31 a 100 kWh e 10% de 101 a 220 kWh) e valor final da conta.
- **Indicador Visual de Atualização:** Feedback instantâneo com animação pulsante (`calc-pulse`), badge verde de confirmação e timestamp com a hora exata do recálculo.
- **Impacto Ambiental:** Estimativa de emissões de CO₂ geradas/evitadas com base no fator de emissão do Sistema Interligado Nacional (0,50 kg CO₂/kWh — MCTI/EPE).

### 5. 📊 Painel Completo de Transparência & Indicadores
- Métricas consolidadas da sessão: total de atendimentos, taxa de encontro, taxa de acerto e tempo médio de resposta.
- Tabela detalhada de histórico com data, origem, pergunta e resultado.
- **Exportação para CSV:** Download em 1 clique do relatório estruturado com suporte a caracteres especiais UTF-8 (`atendimentos_citizen_assist_ai.csv`).

---

## Como Executar Localmente

### Opção 1: Direto no Navegador (Sem Instalação)
Basta dar um duplo clique no arquivo **[`index.html`](file:///index.html)**.  
A aplicação é uma Single Page Application (SPA) 100% autossuficiente e funciona em qualquer navegador moderno (Chrome, Edge, Firefox, Safari) em computadores ou celulares, inclusive offline.

### Opção 2: Servidor Local via Python
Caso deseje rodar a partir de um servidor HTTP local:
```bash
python server.py
```
O script iniciará o servidor na porta `8000` e abrirá a página automaticamente no navegador em `http://localhost:8000`.

---

## Estrutura do Repositório

```
Citizen-Assist-AI/
├── index.html       # Aplicação Web completa (HTML5 + CSS3 + Vanilla JavaScript)
├── server.py        # Servidor web local opcional com abertura automática no navegador
├── README.md        # Documentação completa do projeto
├── .gitignore       # Arquivos e diretórios ignorados pelo Git
└── data/            # Bases de referência e suporte de dados
    ├── base_conhecimento.json  # 19 serviços essenciais cadastrados
    ├── historico.json          # Histórico com registros de atendimentos de teste
    └── atendimentos.csv        # Exportação estruturada para auditoria
```

---

## Tecnologias Empregadas

- **HTML5 Semântico:** Estrutura acessível, otimizada para navegadores móveis e leitores de tela.
- **CSS3 Moderno:** Design responsivo com CSS Grid e Flexbox, animações de transição suaves, variáveis CSS padronizadas e suporte automático ao **Dark Mode** via `prefers-color-scheme`.
- **Vanilla JavaScript (ES6+):** Código limpo sem dependência de bibliotecas externas (React, Vue, jQuery). Motor de busca com normalização de texto, calculadora energética e gerenciamento de estado local (`localStorage`).

---

## Fontes Oficiais e Regulatórias Consultadas

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
| **ANEEL** | Metodologia e Calculadora de Consumo Elétrico | https://www.aneel.gov.br/calculo-do-consumo |
| **EPE / ABSOLAR** | Dados de Irradiação Solar e Fator de Emissão SIN | https://www.epe.gov.br e https://www.absolar.org.br |

---

## Limitações e Transparência

1. **Iniciativa Independente de Utilidade Pública:** O assistente não é um órgão governamental oficial nem realiza a expedição de documentos por si só. Seu objetivo é orientar e direcionar o cidadão com transparência.
2. **Atualização da Base:** A base contém 19 orientações essenciais verificadas. Mudanças legislativas ou administrativas posteriores devem ser refletidas nos arquivos de dados.
3. **Escopo Focado:** Dúvidas fora dos 4 eixos temáticos não são respondidas para evitar desinformação.


