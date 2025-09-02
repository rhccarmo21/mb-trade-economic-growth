# 📊 Análise de Comércio Internacional e Crescimento Econômico

[![Status](https://img.shields.io/badge/status-yellow)]()
[![Python](https://img.shields.io/badge/python-3.11-blue)]()
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange)]()
[![LaTeX](https://img.shields.io/badge/LaTeX-Report-success)]()

---

## 📌 Sobre o Projeto
Este projeto realiza uma análise econométrica da relação entre comércio internacional (exportações, importações, abertura comercial) e crescimento econômico (PIB per capita) utilizando dados de bases internacionais confiáveis.
> O objetivo é investigar padrões de crescimento, testar hipóteses sobre o impacto do comércio e fornecer insights para políticas econômicas.

---

## 🎯 Objetivos
- **Investigar a relação entre comércio internacional e crescimento econômico**  
- **Testar hipóteses sobre o impacto diferenciado de exportações vs importações**  
- **Analisar padrões por nível de renda dos países**  
- **Identificar casos de sucesso e lições de política econômica**  

---

## 📊 Fontes de Dados

| Fonte | Tipo de Dados | Principais Indicadores |
|-------|---------------|----------------------|
| **World Bank – WDI** | Macro e desenvolvimento econômico | PIB per capita, Crescimento do PIB, Abertura Comercial, Taxa de câmbio |
| **UN Comtrade** | Comércio detalhado | Exportações e importações por país, produto e setor |
| **IMF – BoP** | Contas externas e balanço de pagamentos | Fluxos financeiros, importações de serviços, transferências e investimentos |

---

## 📊 Indicadores Utilizados

| Indicador | Código / Fonte | Descrição |
|-----------|----------------|-----------|
| PIB per capita | NY.GDP.PCAP.CD (WDI) | PIB per capita (US$ corrente) |
| Crescimento PIB | NY.GDP.MKTP.KD.ZG (WDI) | Crescimento anual do PIB (%) |
| Exportações (% PIB) | NE.EXP.GNFS.ZS (WDI / UN Comtrade) | Exportações de bens e serviços (% do PIB) |
| Importações (% PIB) | NE.IMP.GNFS.ZS (WDI / UN Comtrade) | Importações de bens e serviços (% do PIB) |
| Abertura Comercial | NE.TRD.GNFS.ZS (WDI) | Exportações + Importações (% do PIB) |
| Taxa de Câmbio | PX.REX.REER (WDI) | Taxa de câmbio efetiva real |
| Balanço de Pagamentos | Diversos códigos (IMF BoP) | Fluxos de capital e contas externas |

---

## 🌍 Países Analisados
- **Alta Renda:** USA, DEU, JPN, GBR, FRA, CAN, AUS, KOR  
- **Média Renda:** BRA, MEX, CHN, TUR, RUS, ZAF, ARG, THA  
- **Baixa Renda:** IND, IDN, NGA, EGY, KEN, BGD, VNM, PAK  

---

## 🔍 Hipóteses Testadas
- Países com maior abertura comercial crescem mais rápido?  
- Exportações têm peso maior que importações no crescimento?  
- Importações de tecnologia/capital estão ligadas a maior crescimento?  
- Países dependentes de commodities são mais voláteis?  
- A relação comércio-crescimento muda conforme nível de renda?  

---

## 🛠️ Metodologia (enxuta)
1. **Coleta de dados** – Automática via APIs do World Bank, UN Comtrade e IMF BoP  
2. **Limpeza e preparação dos datasets** – Tratamento de dados missing e padronização  
3. **Análises exploratórias** – Correlações, visualizações por grupo de países, séries temporais  
4. **Modelagem** – Testes de hipóteses e análises econométricas  
5. **Relatório final em LaTeX** – gera PDF com capa, resumo, introdução, metodologia, resultados e conclusões  

---

## 📈 Métodos de Análise
- Análise de correlação entre indicadores de comércio e crescimento  
- Comparação por nível de renda dos países  
- Séries temporais para identificar tendências  
- Testes de hipóteses estatísticas  
- Visualizações gráficas (scatter plots, heatmaps, evolução temporal)  

---

## 📊 Resultados Esperados
- Arquivos CSV com dados processados  
- Visualizações gráficas de correlação e evolução temporal  
- Estatísticas descritivas por grupo de países  
- Relatório executivo com conclusões e recomendações  

---

## 💡 Principais Funcionalidades
✅ Coleta automática de dados das APIs World Bank, UN Comtrade e IMF BoP  
✅ Limpeza e tratamento de dados missing  
✅ Análise estatística robusta  
✅ Visualizações profissionais  
✅ Relatório executivo automatizado  
✅ Configuração fácil e reproduzível  

---

## 🎨 Personalização
- Adicionar países: modificar o dicionário `countries`  
- Incluir novos indicadores: adicionar à lista `indicators`  
- Alterar período temporal: modificar o parâmetro `date` na função `get_worldbank_data`  
- Customizar visualizações: ajustar parâmetros nos gráficos  

---

## 🔧 Requisitos do Sistema

**Pacotes Python**
```bash
pip install pandas matplotlib seaborn numpy requests scipy jupyterlab
pip install statsmodels scikit-learn openpyxl xlsxwriter plotly
```

**Pacotes Linux (Ubuntu/Debian)**
```bash
sudo apt install python3-pip python3-venv git python3-tk
```

---

## 🚀 Como Executar
```bash
git clone <repository-url>
cd mb-trade-economic-growth
python3 mb-trade-economic-growth.py
# ou use Jupyter Lab
jupyter lab
```

---

## 📁 Estrutura de Arquivos
```
mb-trade-economic-growth/
│
├── mb-trade-economic-growth.py      # Script principal de análise
├── requirements.txt                 # Dependências do projeto
├── setup.sh                         # Script de instalação (Linux)
├── check_installation.py            # Verificador de dependências
│
├── data/                            # Dados brutos e processados
│   ├── trade_economic_growth_data.csv
│   └── trade_economic_growth_avg.csv
│
├── figures/                         # Visualizações geradas
│   ├── correlation_matrix.png
│   ├── trade_growth_relationship.png
│   └── temporal_evolution.png
│
└── outputs/                         # Relatórios e resultados
    └── executive_report.txt
```

---

## 📚 Referências Teóricas
- Teoria do comércio internacional (Ricardo, Heckscher-Ohlin)  
- Modelos de crescimento endógeno (Romer, Lucas)  
- Estudos empíricos sobre comércio e crescimento  
- Relatórios do Banco Mundial, UN Comtrade e FMI  

---

## 🤝 Contribuição
- Adicionar mais indicadores econômicos  
- Implementar modelos econométricos mais avançados  
- Criar dashboard interativo  
- Adicionar testes unitários  
- Expandir documentação  

---

## 📝 Licença
MIT License – uso acadêmico  

---

## 🆘 Suporte
- Verifique se todas as dependências estão instaladas  
- Confirme a conexão com a internet para acesso às APIs  
- Consulte a documentação:  
  - [World Bank WDI](https://data.worldbank.org)  
  - [UN Comtrade](https://comtrade.un.org/)  
  - [IMF BoP](https://www.imf.org/en/Data)

