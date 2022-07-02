"""
Prepara datos para pronóstico.

Esta función crea el archivo data_lake/business/features/precios-diarios.csv
que ha de contener una matriz de precios con 13 rezagos que usa la función 
de entrenamiento de Regresión con Perceptrones Multicapa, a ser usada en la 
fase de training.

El archivo resultante contiene la fecha en la primera columna. 
Las siguientes trece columnas contienen el valor de la fecha y de las doce fechas anteriores.


"""

def make_features():

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

    make_features.to_csv("data_lake/business/features/precios_diarios.csv", index=None, header=True)

    # raise NotImplementedError("Implementar esta función")


def test_make_features():
    assert os.path.isfile("data_lake/business/features/precios_diarios.csv") is True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_features()
