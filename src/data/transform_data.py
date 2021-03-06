"""
Dado que los archivos tienen extensiones diferentes, este módulo los homogeniza 
al reubicarlos en la carpeta datalake/raw en formato csv.

También verifica:
* Que los archivos estén en formato csv
* Que cada archivo CSV tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ..., H23.

"""
import os  
def transform_data():

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

def test_transform_data():
  import glob
  dir_list = os.listdir("data_lake/raw/")
  csv_list = glob.glob("data_lake/raw/*.csv")
  assert len(csv_list) == len(dir_list) - len(glob.glob("data_lake/raw/*.txt"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
