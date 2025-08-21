# Projeto: Análise de Comércio Internacional e Crescimento Econômico

## 📊 Descrição do Projeto
Este projeto realiza uma análise econométrica da relação entre comércio internacional (exportações, importações, abertura comercial) e crescimento econômico (PIB per capita) utilizando dados da API do Banco Mundial.

## 🎯 Objetivos
- Investigar a relação entre comércio internacional e crescimento econômico  
- Testar hipóteses sobre o impacto diferenciado de exportações vs importações  
- Analisar padrões por nível de renda dos países  
- Identificar casos de sucesso e lições de política econômica  

## 📋 Indicadores Utilizados
| Indicador            | Código Banco Mundial | Descrição |
|----------------------|----------------------|-----------|
| PIB per capita       | NY.GDP.PCAP.CD       | PIB per capita (US$ corrente) |
| Exportações (% PIB)  | NE.EXP.GNFS.ZS       | Exportações de bens e serviços (% do PIB) |
| Importações (% PIB)  | NE.IMP.GNFS.ZS       | Importações de bens e serviços (% do PIB) |
| Abertura Comercial   | NE.TRD.GNFS.ZS       | Exportações + Importações (% do PIB) |
| Crescimento PIB      | NY.GDP.MKTP.KD.ZG    | Crescimento anual do PIB (%) |
| Taxa de Câmbio       | PX.REX.REER          | Taxa de câmbio efetiva real |

## 🌍 Países Analisados
- **Alta Renda**: USA, DEU, JPN, GBR, FRA, CAN, AUS, KOR  
- **Média Renda**: BRA, MEX, CHN, TUR, RUS, ZAF, ARG, THA  
- **Baixa Renda**: IND, IDN, NGA, EGY, KEN, BGD, VNM, PAK  

## 🔧 Requisitos do Sistema
### Pacotes Python
```bash
pip install pandas matplotlib seaborn numpy requests scipy jupyterlab
pip install statsmodels scikit-learn openpyxl xlsxwriter plotly
```
### Pacotes Linux (Ubuntu/Debian)
```bash
sudo apt install python3-pip python3-venv git python3-tk
```

## 🚀 Como Executar
Clone o repositório:
```bash
git clone <repository-url>
cd mb-trade-economic-growth
```
Execute o script:
```bash
python3 mb-trade-economic-growth.py
```
Ou use Jupyter Lab:
```bash
jupyter lab
```

## 📁 Estrutura de Arquivos
```text
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

## 🔍 Hipóteses Testadas
- Países com maior abertura comercial crescem mais rápido?  
- Exportações têm peso maior que importações no crescimento?  
- Importações de tecnologia/capital estão ligadas a maior crescimento?  
- Países dependentes de commodities são mais voláteis?  
- A relação comércio-crescimento muda conforme nível de renda?  

## 📈 Métodos de Análise
- Análise de correlação entre indicadores de comércio e crescimento  
- Análise comparativa por nível de renda dos países  
- Séries temporais para identificar tendências  
- Testes de hipóteses estatísticas  
- Visualizações para comunicação dos resultados  

## 📊 Saídas Geradas
- Arquivos CSV com dados processados  
- Visualizações gráficas (scatter plots, heatmaps, séries temporais)  
- Estatísticas descritivas por grupo de países  
- Matriz de correlação entre todos os indicadores  
- Relatório executivo com conclusões e recomendações  

## 💡 Principais Funcionalidades
✅ Coleta automática de dados da API do Banco Mundial  
✅ Limpeza e tratamento de dados missing  
✅ Análise estatística robusta  
✅ Visualizações profissionais  
✅ Relatório executivo automatizado  
✅ Configuração fácil e reproduzível  

## 🎨 Personalização
O projeto é altamente customizável:
- **Adicionar países**: Modificar o dicionário `countries`  
- **Incluir novos indicadores**: Adicionar à lista `indicators`  
- **Alterar período temporal**: Modificar o parâmetro `date` na função `get_worldbank_data`  
- **Customizar visualizações**: Ajustar parâmetros nos gráficos  

## 📚 Referências Teóricas
- Teoria do comércio internacional (Ricardo, Heckscher-Ohlin)  
- Modelos de crescimento endógeno (Romer, Lucas)  
- Estudos empíricos sobre comércio e crescimento  
- Relatórios do Banco Mundial e FMI  

## 🤝 Contribuição
Contribuições são bem-vindas! Áreas para melhoria:
- Adicionar mais indicadores econômicos  
- Implementar modelos econométricos mais avançados  
- Criar dashboard interativo  
- Adicionar testes unitários  
- Expandir documentação  

## 📝 Licença
Este projeto é de uso acadêmico e está licenciado sob a **MIT License**.

## 🆘 Suporte
Para dúvidas ou problemas:
- Verifique se todas as dependências estão instaladas  
- Confirme a conexão com a internet para acesso à API  
- Consulte a documentação do Banco Mundial: [data.worldbank.org](https://data.worldbank.org)
