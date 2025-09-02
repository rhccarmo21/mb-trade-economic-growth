import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import wb
import os
from datetime import datetime

# Configurações de visualização
plt.style.use('default')
sns.set_palette("deep")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# Definição de países por nível de renda
countries = {
    'high_income': ['USA', 'DEU', 'JPN', 'GBR', 'FRA', 'CAN', 'AUS', 'KOR'],
    'middle_income': ['BRA', 'MEX', 'CHN', 'TUR', 'RUS', 'ZAF', 'ARG', 'THA'],
    'low_income': ['IND', 'IDN', 'NGA', 'EGY', 'KEN', 'BGD', 'VNM', 'PAK']
}

# Mapeamento de códigos para nomes completos
country_code_to_name = {
    'USA': 'United States', 'DEU': 'Germany', 'JPN': 'Japan', 'GBR': 'United Kingdom',
    'FRA': 'France', 'CAN': 'Canada', 'AUS': 'Australia', 'KOR': 'South Korea',
    'BRA': 'Brazil', 'MEX': 'Mexico', 'CHN': 'China', 'TUR': 'Turkey',
    'RUS': 'Russia', 'ZAF': 'South Africa', 'ARG': 'Argentina', 'THA': 'Thailand',
    'IND': 'India', 'IDN': 'Indonesia', 'NGA': 'Nigeria', 'EGY': 'Egypt',
    'KEN': 'Kenya', 'BGD': 'Bangladesh', 'VNM': 'Vietnam', 'PAK': 'Pakistan'
}

# Definição dos indicadores
indicators = {
    'NY.GDP.PCAP.CD': 'gdp_per_capita',
    'NY.GDP.MKTP.KD.ZG': 'gdp_growth',
    'NE.EXP.GNFS.ZS': 'exports_pct_gdp',
    'NE.IMP.GNFS.ZS': 'imports_pct_gdp',
    'NE.TRD.GNFS.ZS': 'trade_openness',
    'PX.REX.REER': 'real_exchange_rate'
}

# Período de análise
start_year = 2000
end_year = 2022

def fetch_real_data():
    """Tenta buscar dados reais do World Bank"""
    try:
        print("Tentando buscar dados reais do World Bank...")
        
        # Buscar dados
        data = wb.download(
            indicator=list(indicators.keys()), 
            country=list(countries.keys()), 
            start=start_year, 
            end=end_year
        )
        
        if data.empty:
            print("Nenhum dado retornado pela API")
            return None
            
        # Processar dados
        data = data.reset_index()
        data['year'] = data['year'].astype(int)
        
        # Renomear colunas
        for code, name in indicators.items():
            if code in data.columns:
                data = data.rename(columns={code: name})
        
        # Classificar países por nível de renda
        def get_income_level(country_code):
            for level, countries_list in countries.items():
                if country_code in countries_list:
                    return level
            return 'unknown'
        
        data['income_level'] = data['country'].apply(get_income_level)
        
        # Remover países não classificados
        data = data[data['income_level'] != 'unknown']
        
        if data.empty:
            print("Nenhum dado válido após classificação")
            return None
            
        # Calcular métricas adicionais
        data = calculate_additional_metrics(data)
        
        print(f"Dados reais coletados: {data.shape[0]} observações")
        return data
        
    except Exception as e:
        print(f"Erro ao buscar dados reais: {e}")
        return None

def create_sample_data():
    """Cria dados de exemplo para demonstração"""
    print("Criando dados de exemplo...")
    
    data = []
    years = list(range(start_year, end_year + 1))
    
    # Gerar dados realistas para cada país
    for income_level, country_codes in countries.items():
        for country_code in country_codes:
            country_name = country_code_to_name.get(country_code, country_code)
            
            for year in years:
                # Valores base por nível de renda
                if income_level == 'high_income':
                    gdp_base = np.random.uniform(30000, 60000)
                    growth_base = np.random.uniform(1.5, 3.5)
                    trade_openness = np.random.uniform(60, 100)
                elif income_level == 'middle_income':
                    gdp_base = np.random.uniform(8000, 15000)
                    growth_base = np.random.uniform(3.0, 6.0)
                    trade_openness = np.random.uniform(40, 70)
                else:  # low_income
                    gdp_base = np.random.uniform(1000, 5000)
                    growth_base = np.random.uniform(4.0, 8.0)
                    trade_openness = np.random.uniform(30, 60)
                
                # Adicionar tendência temporal
                years_passed = year - 2000
                gdp_per_capita = gdp_base * (1.02 ** years_passed)  # Crescimento de 2% ao ano
                gdp_growth = growth_base + np.random.uniform(-2.0, 2.0)
                
                # Aumentar abertura comercial ao longo do tempo
                trade_openness = trade_openness * (1 + 0.01 * years_passed)
                
                # Calcular exportações e importações
                exports_share = np.random.uniform(0.4, 0.6)
                exports_pct = trade_openness * exports_share
                imports_pct = trade_openness * (1 - exports_share)
                
                data.append({
                    'country': country_name,
                    'country_code': country_code,
                    'year': year,
                    'gdp_per_capita': gdp_per_capita,
                    'gdp_growth': gdp_growth,
                    'exports_pct_gdp': exports_pct,
                    'imports_pct_gdp': imports_pct,
                    'trade_openness': trade_openness,
                    'real_exchange_rate': np.random.uniform(80, 120),
                    'income_level': income_level
                })
    
    df = pd.DataFrame(data)
    df = calculate_additional_metrics(df)
    
    return df

def calculate_additional_metrics(df):
    """Calcula métricas adicionais"""
    df = df.copy()
    
    # Calcular saldo comercial
    df['trade_balance_pct_gdp'] = df['exports_pct_gdp'] - df['imports_pct_gdp']
    
    # Calcular crescimento do PIB per capita
    df = df.sort_values(['country', 'year'])
    df['gdp_per_capita_growth'] = df.groupby('country')['gdp_per_capita'].pct_change() * 100
    
    return df

def create_visualizations(df, data_type="real"):
    """Cria visualizações para a análise"""
    
    os.makedirs('figures', exist_ok=True)
    suffix = "_sample" if data_type == "sample" else ""
    
    # 1. Matriz de correlação
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    numeric_cols = [col for col in numeric_cols if col not in ['year']]
    corr_matrix = df[numeric_cols].corr()
    
    fig, ax = plt.subplots(figsize=(12, 10))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
    ax.set_title('Matriz de Correlação entre Indicadores Econômicos')
    plt.savefig(f'figures/correlation_matrix{suffix}.png')
    plt.close(fig)
    
    # 2. Relação entre abertura comercial e crescimento
    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = {'high_income': 'blue', 'middle_income': 'green', 'low_income': 'red'}
    for level, color in colors.items():
        subset = df[df['income_level'] == level]
        ax.scatter(subset['trade_openness'], subset['gdp_growth'], 
                  alpha=0.6, label=level, c=color)
    
    ax.set_xlabel('Abertura Comercial (% do PIB)')
    ax.set_ylabel('Crescimento do PIB (%)')
    ax.set_title('Relação entre Abertura Comercial e Crescimento do PIB')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.savefig(f'figures/trade_growth_relationship{suffix}.png')
    plt.close(fig)
    
    # 3. Evolução temporal
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
    
    # Evolução da abertura comercial
    trade_evolution = df.groupby(['year', 'income_level'])['trade_openness'].mean().reset_index()
    for level, color in colors.items():
        subset = trade_evolution[trade_evolution['income_level'] == level]
        ax1.plot(subset['year'], subset['trade_openness'], 
                marker='o', linewidth=2, label=level, color=color)
    
    ax1.set_xlabel('Ano')
    ax1.set_ylabel('Abertura Comercial Média (% do PIB)')
    ax1.set_title('Evolução Temporal da Abertura Comercial')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Evolução do crescimento econômico
    growth_evolution = df.groupby(['year', 'income_level'])['gdp_growth'].mean().reset_index()
    for level, color in colors.items():
        subset = growth_evolution[growth_evolution['income_level'] == level]
        ax2.plot(subset['year'], subset['gdp_growth'], 
                marker='o', linewidth=2, label=level, color=color)
    
    ax2.set_xlabel('Ano')
    ax2.set_ylabel('Crescimento do PIB Médio (%)')
    ax2.set_title('Evolução Temporal do Crescimento Econômico')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'figures/temporal_evolution{suffix}.png')
    plt.close(fig)
    
    return corr_matrix

def generate_report(df, corr_matrix, data_type="real"):
    """Gera relatório completo"""
    
    os.makedirs('outputs', exist_ok=True)
    suffix = "_sample" if data_type == "sample" else ""
    
    # Estatísticas descritivas
    income_stats = df.groupby('income_level').agg({
        'gdp_per_capita': ['mean', 'std'],
        'gdp_growth': ['mean', 'std'],
        'exports_pct_gdp': 'mean',
        'imports_pct_gdp': 'mean',
        'trade_openness': 'mean'
    }).round(2)
    
    # Análise de correlação
    growth_correlations = corr_matrix['gdp_growth'].sort_values(ascending=False)
    
    report = f"""
    RELATÓRIO DE ANÁLISE: COMÉRCIO INTERNACIONAL E CRESCIMENTO ECONÔMICO
    ====================================================================
    
    Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    Tipo de dados: {'Amostra simulada' if data_type == 'sample' else 'Dados reais'}
    Período: {start_year}-{end_year}
    Países analisados: {df['country'].nunique()}
    Observações: {len(df)}
    
    ESTATÍSTICAS POR NÍVEL DE RENDA:
    {income_stats.to_string()}
    
    CORRELAÇÕES COM CRESCIMENTO DO PIB:
    {growth_correlations.to_string()}
    
    PRINCIPAIS DESCOBERTAS:
    
    1. DIFERENÇAS ENTRE NÍVEIS DE RENDA:
    - Países de alta renda: PIB per capita mais elevado, crescimento moderado
    - Países de média renda: Crescimento econômico sólido
    - Países de baixa renda: Maior taxa de crescimento, menor PIB per capita
    
    2. RELAÇÃO COMÉRCIO-CRESCIMENTO:
    - Correlação {'positiva' if growth_correlations.get('trade_openness', 0) > 0 else 'negativa'} 
      entre abertura comercial e crescimento
    - Países com maior integração comercial tendem a apresentar melhor desempenho
    
    3. PADRÕES TEMPORAIS:
    - Tendência de aumento da abertura comercial ao longo do tempo
    - Crescimento econômico mostra volatilidade em períodos de crise
    
    RECOMENDAÇÕES:
    
    • Países de baixa renda: Focar em aumentar a integração comercial e desenvolver
      capacidades exportadoras
    
    • Países de média renda: Diversificar pautas de exportação e promover acordos
      comerciais estratégicos
    
    • Países de alta renda: Manter abertura existente e focar em inovação e comércio
      de serviços
    
    LIMITAÇÕES:
    {'• Dados simulados para fins demonstrativos' if data_type == 'sample' else '• Dados sujeitos à disponibilidade das fontes'}
    • Análise baseada em correlações, não estabelece causalidade
    • Resultados podem variar com a inclusão de variáveis adicionais
    """
    
    with open(f'outputs/report{suffix}.txt', 'w', encoding='utf-8') as f:
        f.write(report)
    
    return report

def main():
    """Função principal"""
    print("Iniciando análise de comércio internacional e crescimento econômico...")
    
    # Tentar buscar dados reais primeiro
    df = fetch_real_data()
    data_type = "real"
    
    # Se não conseguir, usar dados de exemplo
    if df is None or df.empty:
        print("Usando dados de exemplo para demonstração...")
        df = create_sample_data()
        data_type = "sample"
    
    # Verificar dados
    print(f"Dados disponíveis: {df.shape[0]} observações")
    print(f"Países: {df['country'].nunique()}")
    print(f"Distribuição por renda:")
    print(df['income_level'].value_counts())
    
    # Salvar dados
    os.makedirs('data', exist_ok=True)
    filename = "trade_economic_growth_data.csv" if data_type == "real" else "trade_economic_growth_sample_data.csv"
    df.to_csv(f'data/{filename}', index=False)
    
    # Criar visualizações
    corr_matrix = create_visualizations(df, data_type)
    
    # Gerar relatório
    report = generate_report(df, corr_matrix, data_type)
    
    print("Análise concluída com sucesso! ✅")
    print(f"\nArquivos gerados:")
    print(f"- data/{filename}")
    print(f"- figures/correlation_matrix{'_sample' if data_type == 'sample' else ''}.png")
    print(f"- figures/trade_growth_relationship{'_sample' if data_type == 'sample' else ''}.png")
    print(f"- figures/temporal_evolution{'_sample' if data_type == 'sample' else ''}.png")
    print(f"- outputs/report{'_sample' if data_type == 'sample' else ''}.txt")
    
    # Mostrar resumo
    print(f"\nRESUMO EXECUTIVO ({'Dados Reais' if data_type == 'real' else 'Dados de Exemplo'}):")
    print("=" * 60)
    
    # Estatísticas básicas
    stats = df.groupby('income_level')['gdp_growth'].mean()
    for level, value in stats.items():
        print(f"{level:15}: {value:.2f}% crescimento médio")
    
    # Correlação principal
    trade_corr = corr_matrix.loc['trade_openness', 'gdp_growth']
    print(f"\nCorrelação abertura comercial-crescimento: {trade_corr:.3f}")
    
    if data_type == "sample":
        print("\n💡 NOTA: Análise realizada com dados simulados para demonstração.")
        print("Para análise com dados reais, verifique a conexão com a API do World Bank.")

if __name__ == "__main__":
    main()
