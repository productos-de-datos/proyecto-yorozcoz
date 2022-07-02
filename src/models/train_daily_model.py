def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de pronóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.neural_network import MLPRegressor
    import numpy as np
    import pickle


    df = pd.read_csv(
        "data_lake/business/precios-diarios.csv", index_col=None, header=0
    )
    df = df[["fecha", "precio"]]
    df["fecha"] = pd.to_datetime(df["fecha"])
    df = df.set_index(['fecha'])
    
  
    X = pd.read_csv(
        "data_lake/business/features/precios-diarios.csv", index_col=None, header=0
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


    # Construcción del regresor
    np.random.seed(123456)

    H = 1  # Se escoge arbitrariamente

    mlp = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="logistic",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.1,
        max_iter=10000,
    )

    # Entrenamiento
    mlp.fit(X[0:Num_Patr-test_size], observed_scaled["precio"][0:Num_Patr-test_size])

    # save the model to disk


    filename = 'src/models/precios-diarios.pkl'
    pickle.dump(mlp, open(filename, 'wb'))

    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()
