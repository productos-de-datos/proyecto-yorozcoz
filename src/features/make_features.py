def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler


    df = pd.read_csv(
        "data_lake/business/precios-diarios.csv", index_col=None, header=0
    )
    df = df[["fecha", "precio"]]
    df["fecha"] = pd.to_datetime(df["fecha"])
    df = df.set_index(['fecha'])
    

    training_rate = 0.95
    test_size = len(df) - int(len(df)*training_rate)


    scaler = MinMaxScaler()

    # escala la serie
    data_scaled = scaler.fit_transform(np.array(df).reshape(-1, 1))

    # z es un array de listas como efecto
    # del escalamiento
    data_scaled = [u[0] for u in data_scaled]

    data_scaled = pd.DataFrame(data_scaled, 
                            columns=["precio"],
                            index = df.index
                            )

    #se define en 13 el numero de rezagos
    P = 13

    # Ya que la implementación disponible en sklearn es para modelos de regresión, 
    # se debe armar una matrix donde las variables independientes son zt−1, …, zt−P 
    # y la variable dependiente es zt.

    X = []
    for t in range(P - 1, len(df) - 1):
        X.append([data_scaled["precio"][t - n].tolist() for n in range(P)])

    make_features = pd.DataFrame(X)

    make_features.to_csv("data_lake/business/features/precios-diarios.csv", index=None, header=True)

    # raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_features()
