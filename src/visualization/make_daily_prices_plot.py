def make_daily_prices_plot():
    """
    Esta función crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv(
        "data_lake/business/precios-diarios.csv", index_col=None, header=0
    )
    df["fecha"] = pd.to_datetime(df["fecha"])
    df = df.set_index(['fecha'])


    ax = df['precio'].plot(label='Precio',figsize=(10, 5))
    ax.set_title('Precios de Bolsa Nacional (Histórico de promedios diarios)', fontsize = 14, loc='center', fontdict=dict(weight='bold'))
    ax.set_xlabel('Días')
    ax.set_ylabel('Precio')

    plt.savefig('data_lake/business/reports/figures/daily_prices.png', format="png")

    #plt.show()
    #raise NotImplementedError("Implementar esta función")
    

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_daily_prices_plot()
