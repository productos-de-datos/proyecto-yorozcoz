"""

Este módulo crea un grafico de lines que representa los precios promedios mensuales.

Usando el archivo data_lake/business/precios-mensuales.csv, crea un grafico de
lines que representa los precios promedios mensuales.

Salva el archivo en formato PNG en data_lake/business/reports/figures/monthly_prices.png.


"""
def make_monthly_prices_plot():

    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv(
        "data_lake/business/precios-mensuales.csv", index_col=None, header=0
    )
    df["fecha"] = pd.to_datetime(df["fecha"])
    df = df.set_index(['fecha'])

    ax = df['precio'].plot(label='Precio',figsize=(10, 5))
    ax.set_title('Precios de Bolsa Nacional (Histórico de promedios mensuales)', fontsize = 14, loc='center', fontdict=dict(weight='bold'))
    ax.set_xlabel('Meses')
    ax.set_ylabel('Precio')

    plt.savefig('data_lake/business/reports/figures/monthly_prices.png', format="png")


    #plt.show()
    # raise NotImplementedError("Implementar esta función")

def test_make_monthly_prices_plot():
    assert os.path.isfile("data_lake/business/reports/figures/monthly_prices.png") is True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_monthly_prices_plot()
