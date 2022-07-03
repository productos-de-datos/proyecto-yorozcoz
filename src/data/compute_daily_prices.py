"""
Esta función crea el archivo data_lake/business/precios-diarios.csv que computa el promedio diario 
de los precios en cada uno de los días contenidos en data_lake/cleansed/precios-horarios.csv

Verifica que el archivo resultado contenga los campos con formato:

* fecha: fecha en formato YYYY-MM-DD
* precio: valor

Verifica que el promedio se efectúe correctamente tomando un dia aleatorio y lo cojeta buscandolo en el archivo resultado


"""
import os  

def compute_daily_prices():
    import pandas as pd

    df = pd.read_csv(
        "data_lake/cleansed/precios-horarios.csv", index_col=None, header=0
    )
    df = df[["fecha", "precio"]]
    df["fecha"] = pd.to_datetime(df["fecha"])
    compute_daily_prices = df.groupby("fecha").mean({"precio": "precio"})
    compute_daily_prices.reset_index(inplace=True)
    compute_daily_prices.to_csv("data_lake/business/precios-diarios.csv", index=None, header=True
    )
    # raise NotImplementedError("Implementar esta función")

def test_compute_daily_prices():
    assert os.path.isfile("data_lake/business/precios-diarios.csv") is True


if __name__ == "__main__":

    import doctest

    doctest.testmod()
    compute_daily_prices()
