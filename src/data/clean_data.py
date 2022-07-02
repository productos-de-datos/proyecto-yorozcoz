def clean_data():
    """
    Esta función limpia los datos y los combina en un mismo archivo 
    data_lake/cleansed/precios-horarios.csv que contiene toda la 
    información del 1997 a 2021.
 
    Verifica que las columnas de este archivo sean:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    """

    import pandas as pd
    import glob

    path_file = glob.glob(r"data_lake/raw/*.csv")
    li = []

    for filename in path_file:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
    read_file = pd.concat(li, axis=0, ignore_index=True)
    read_file = read_file[read_file["Fecha"].notnull()]

    fecha1 = read_file.iloc[:, 0]  # fecha
    lista_datos = []

    precio = 0
    contador_filas = 0
    for fecha in fecha1:
        for hora in range(0, 24):
            precio = read_file.iloc[contador_filas, (hora + 1)]
            lista_datos.append([fecha, "{:0>2d}".format(hora), precio])
        contador_filas += 1
    df = pd.DataFrame(lista_datos, columns=["fecha", "hora", "precio"])
    df = df[df["fecha"].notnull()]
    df.to_csv("data_lake/cleansed/precios-horarios.csv", index=None, header=True)
    # raise NotImplementedError("Implementar esta función")
    # return



if __name__ == "__main__":

    import doctest

    doctest.testmod()
    clean_data()