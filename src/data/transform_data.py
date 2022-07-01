def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import pandas as pd

    def transformar_xls_a_csv(year, encabezado, extension):
        read_file = pd.read_excel(
            "data_lake/landing/{}.{}".format(year, extension), header=encabezado
        )
        read_file = read_file.iloc[:, 0:25]
        read_file.columns = [
            "Fecha",
            "H00",
            "H01",
            "H02",
            "H03",
            "H04",
            "H05",
            "H06",
            "H07",
            "H08",
            "H09",
            "H10",
            "H11",
            "H12",
            "H13",
            "H14",
            "H15",
            "H16",
            "H17",
            "H18",
            "H19",
            "H20",
            "H21",
            "H22",
            "H23",
        ]
        read_file.to_csv("data_lake/raw/{}.csv".format(year), index=None)

        return

    for year in range(1995, 2022):
        if year in range(1995, 2000):
            transformar_xls_a_csv(year, 3, "xlsx")
        elif year in range(2000, 2016):
            transformar_xls_a_csv(year, 2, "xlsx")
        elif year in range(2016, 2018):
            transformar_xls_a_csv(year, 2, "xls")
        else:
            transformar_xls_a_csv(year, 0, "xlsx")
    # return
    # raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
