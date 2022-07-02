def make_forecasts():
    """
    
    Construya los pronosticos con el modelo entrenado final.

    Esta función halla los pronósticos de precios diarios a partir de 
    las características definidas en data_lake/business/features/precios-diarios.csv
    aplicando Multi-layer perceptron regression de la librería SkLearn.

    El resultado del pronóstico se salva en data_lake/business/forecasts/precios-diarios.csv. 
    
    Este archivo contiene tres columnas:

    * La fecha.
    * El precio promedio real de la electricidad.
    * El pronóstico del precio promedio real.


    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import pickle
    from datetime import timedelta
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler


    df = pd.read_csv("data_lake/business/precios-diarios.csv", index_col=None, header=0)

    df = df[["fecha", "precio"]]
    df["fecha"] = pd.to_datetime(df["fecha"])
    df = df.set_index(['fecha'])

    X = pd.read_csv(
        "data_lake/business/features/precios_diarios.csv", index_col=None, header=0
    ).values.tolist()
        
    #
    # Numero total de patrones al convertir
    # los datos a un modelo de regresión
    #
    Num_Patr = len(X)

    training_rate = 0.95
    test_size = len(df) - int(len(df)*training_rate)

    # P es la cantidad de rezagos que toma el modelo para pronosticar.
    P = 13


    # crea el transformador
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

    observed_scaled = data_scaled[P:]

    mlp = pd.read_pickle("src/models/precios-diarios.pkl")



    # Pronostico
    y_scaled_m1 = mlp.predict(X)

    y_scaled_m1 = pd.DataFrame(y_scaled_m1, 
                            columns=["predict"],
                            index = df[min(df.index) + timedelta(days=P): max(df.index)].index
                            )

    #
    # Se desescala para llevar los valores a la escala de los datos originales
    #
    y_m1 = scaler.inverse_transform([[u] for u in y_scaled_m1["predict"]])
    y_m1 = [u[0] for u in y_m1]

    y_m1 = pd.DataFrame(y_m1,
                        columns=["predict"],
                        index = y_scaled_m1.index
                        )


    daily_forecast= df.join(y_m1)
    daily_forecast.to_csv("data_lake/business/forecasts/precios-diarios.csv", index=True, header=True)

    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_forecasts()
