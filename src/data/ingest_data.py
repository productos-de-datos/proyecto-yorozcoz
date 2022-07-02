"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

Este módulo contiene las funciones que descargan desde el repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ 
los archivos de precios de bolsa nacional en formato xls a la capa landing del datalake, en tanto la información
está en multiples archivos.

Los años 2017 y 2018 están en formato .xls, para los demás años se trae en formato .xlsx


"""
import os  

def ingest_data():

    import pandas as pd
    import xlwt

    def descargar_archivo(ruta, file_name, extension):

        for año in file_name:
            url_rute = ruta + "/" + año + extension + "?raw=true"
            nombre_archivo = "data_lake/landing/" + "{}{}".format(año, extension)
            descarga = pd.read_excel(url_rute)
            descarga.to_excel(
                "data_lake/landing/{}{}".format(año, extension), index=None, header=True
            )
        return

    ruta = "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/"
    file_name1 = [str(año) for año in range(1995, 2016)]
    file_name2 = [str(año) for año in range(2018, 2022)]

    file_name_xlsx = file_name1 + file_name2
    descargar_archivo(ruta, file_name_xlsx, ".xlsx")

    file_name_xls = ["2016", "2017"]
    descargar_archivo(ruta, file_name_xls, ".xls")
    # raise NotImplementedError("Implementar esta función")
    # ingest_data()

def test_ingest_data():
    assert os.path.isfile("data_lake/landing/1995.xlsx") is True
    assert os.path.isfile("data_lake/landing/1996.xlsx") is True
    assert os.path.isfile("data_lake/landing/1997.xlsx") is True
    assert os.path.isfile("data_lake/landing/1998.xlsx") is True
    assert os.path.isfile("data_lake/landing/1999.xlsx") is True
    assert os.path.isfile("data_lake/landing/2000.xlsx") is True
    assert os.path.isfile("data_lake/landing/2001.xlsx") is True
    assert os.path.isfile("data_lake/landing/2002.xlsx") is True
    assert os.path.isfile("data_lake/landing/2003.xlsx") is True
    assert os.path.isfile("data_lake/landing/2004.xlsx") is True
    assert os.path.isfile("data_lake/landing/2005.xlsx") is True
    assert os.path.isfile("data_lake/landing/2006.xlsx") is True
    assert os.path.isfile("data_lake/landing/2007.xlsx") is True
    assert os.path.isfile("data_lake/landing/2008.xlsx") is True
    assert os.path.isfile("data_lake/landing/2009.xlsx") is True
    assert os.path.isfile("data_lake/landing/2010.xlsx") is True
    assert os.path.isfile("data_lake/landing/2011.xlsx") is True
    assert os.path.isfile("data_lake/landing/2012.xlsx") is True
    assert os.path.isfile("data_lake/landing/2013.xlsx") is True
    assert os.path.isfile("data_lake/landing/2014.xlsx") is True
    assert os.path.isfile("data_lake/landing/2015.xlsx") is True
    assert os.path.isfile("data_lake/landing/2016.xls") is True
    assert os.path.isfile("data_lake/landing/2017.xls") is True
    assert os.path.isfile("data_lake/landing/2018.xlsx") is True
    assert os.path.isfile("data_lake/landing/2019.xlsx") is True
    assert os.path.isfile("data_lake/landing/2020.xlsx") is True
    assert os.path.isfile("data_lake/landing/2021.xlsx") is True


if __name__ == "__main__":
    
    import doctest

    doctest.testmod()
    ingest_data()