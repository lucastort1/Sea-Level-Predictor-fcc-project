import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Leitura dos dados
    df = pd.read_csv('epa-sea-level.csv')
    
    # Configuração do gráfico de dispersão
    fig, ax = plt.subplots()
    ax.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)
    
    # Primeira linha de tendência (1880 até 2013)
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years = pd.Series(range(1880, 2051))  # Alterado para garantir que o intervalo de 1880 a 2050 seja incluído corretamente
    ax.plot(years, intercept + slope * years, 'r', label='First Line of Best Fit')
    
    # Segunda linha de tendência (a partir de 2000)
    df_recent = df.loc[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))  # Alterado para garantir que o intervalo de 2000 a 2050 seja incluído corretamente
    ax.plot(years_recent, intercept_recent + slope_recent * years_recent, 'b', label='Second Line of Best Fit')
    
    # Definindo rótulos e título
    ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")
    ax.legend()
    
    # Salvando o gráfico
    plt.savefig('sea_level_plot.png')
    
    return plt.gca()
