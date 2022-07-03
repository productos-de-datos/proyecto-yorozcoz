
"""
Este módulo contiene las funciones crea las carpetas del 'datalake' del proyecto 
de acuerdo a la estructura necesaria para la fase de preprocesamiento de la información
entes del entrenamiento y predicción del modelo.

El data lake resultado contiene las siguientes subcarpetas :

```
.
|
\___ data_lake/
    |___ landing/
    |___ raw/
    |___ cleansed/
    \___ business/
        |___ reports/
        |    |___ figures/
        |___ features/
        |___ forecasts/

```
"""

import os  

def create_data_lake():
    
    os.mkdir("./data_lake/")
    
    parent_dir = "data_lake/"
    carpetas = ["landing", "raw", "cleansed", "business"]
    [os.mkdir(os.path.join(parent_dir, c)) for c in carpetas]

    parent_dir = "data_lake/business/"
    carpetas = ["reports", "features", "forecasts"]
    [os.mkdir(os.path.join(parent_dir, c)) for c in carpetas]

    parent_dir = "data_lake/business/reports/"
    directory = "figures"
    os.mkdir(os.path.join(parent_dir, directory))


def test_create_data_lake():
    """Verifica la correcta creación del data lake"""
    assert os.path.isdir("data_lake/business") is True
    assert os.path.isdir("data_lake/business/reports/figures") is True
    assert os.path.isdir("data_lake/business/features") is True
    assert os.path.isdir("data_lake/business/forecasts") is True
    assert os.path.isdir("data_lake/cleansed") is True
    assert os.path.isdir("data_lake/landing") is True
    assert os.path.isdir("data_lake/raw") is True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    create_data_lake()
    test_create_data_lake()
