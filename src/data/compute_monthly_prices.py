def compute_monthly_prices():
    """
    
    Esta función crea el archivo data_lake/business/precios-mensuales.csv que computa el promedio mensual 
    de los precios en cada uno de los meses contenidos en data_lake/cleansed/precios-horarios.csv
    
    Verifica que el archivo resultado contenga los campos con formato:

    * fecha: fecha en formato YYYY-MM-DD
    * precio: valor

    Verifica que el promedio se efectúe correctamente tomando un mes aleatorio y lo cojeta buscandolo el en archivo resultado:

    """
    import pandas as pd

    df = pd.read_csv(
        "data_lake/cleansed/precios-horarios.csv", index_col=None, header=0
    )
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["year_mes"] = (
        ((df["fecha"].dt.year).astype(int)).astype(str)
        + "-"
        + ((df["fecha"].dt.month).astype(int)).astype(str)
    )

    df["dia"] = (df["fecha"].dt.day).astype(int)
    data_para_dia = df[["year_mes", "dia"]]

    dia_agrupacion = data_para_dia.groupby("year_mes").max({"dia": "dia"})
    dia_agrupacion.reset_index(inplace=True)
    dia_agrupacion["fecha"] = (
        dia_agrupacion["year_mes"] + "-" + (dia_agrupacion["dia"]).astype(str)
    )

    dia_agrupacion["fecha"] = pd.to_datetime(dia_agrupacion["fecha"])

    dfm = df[["year_mes", "precio"]]
    compute_month_prices = dfm.groupby("year_mes").mean({"precio_promedio": "precio"})
    compute_month_prices.reset_index(inplace=True)

    compute_month_prices = pd.merge(
        dia_agrupacion, compute_month_prices, on="year_mes", how="left"
    )

    compute_month_prices = compute_month_prices[["fecha", "precio"]]

    compute_month_prices = compute_month_prices.sort_values(by="fecha")
    compute_month_prices.to_csv(
        "data_lake/business/precios-mensuales.csv", index=None, header=True
    )

    # raise NotImplementedError("Implementar esta función")
    # return


if __name__ == "__main__":

    import doctest

    doctest.testmod()
    compute_monthly_prices()
