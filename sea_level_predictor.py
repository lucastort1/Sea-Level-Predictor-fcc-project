import pandas as pd # Importa a biblioteca Pandas para manipulação de dados
import matplotlib.pyplot as plt # Importa Matplotlib para gerar gráficos
from scipy.stats import linregress # Importa a função linregress da biblioteca SciPy para regressão linear

def draw_plot():
    # Leitura dos dados do arquivo CSV para um dataframe do Pandas
    df = pd.read_csv('epa-sea-level.csv')
    
    fig, ax = plt.subplots() # Configuração do gráfico de dispersão
    ax.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df) # Plota os dados como um gráfico de dispersão
    
    # Primeira linha de tendência (usando os dados de 1880 até 2013)
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"]) # Calcula a regressão linear para o nível do mar em função do ano
    # Cria uma série de anos de 1880 até 2050 para plotar a linha de tendência
    years = pd.Series(range(1880, 2051))
    # Plota a linha de tendência no gráfico usando os parâmetros calculados da regressão linear
    ax.plot(years, intercept + slope * years, 'r', label='First Line of Best Fit')
    
    # Segunda linha de tendência (a partir de 2000)
    df_recent = df.loc[df["Year"] >= 2000] 
    # Calcula a regressão linear para o período de 2000 em diante
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051)) # Cria uma série de anos de 2000 até 2050 para plotar a segunda linha de tendência
    # Plota a segunda linha de tendência no gráfico usando os parâmetros calculados da regressão linear recente
    ax.plot(years_recent, intercept_recent + slope_recent * years_recent, 'b', label='Second Line of Best Fit') 
    
    # Definindo rótulos e título
    ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")
    ax.legend() # Adiciona legenda
    
    # Salva o gráfico em um arquivo PNG
    plt.savefig('sea_level_plot.png')
    
    return plt.gca()
