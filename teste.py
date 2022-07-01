import os
import sys


def test_01():
    """Califica la creación del data lake"""
    os.system("rm -rf data_lake")
    os.system("make create_data_lake")
    assert os.path.isdir("data_lake/business") is True
    assert os.path.isdir("data_lake/business/reports/figures") is True
    assert os.path.isdir("data_lake/business/features") is True
    assert os.path.isdir("data_lake/business/forecasts") is True
    assert os.path.isdir("data_lake/cleansed") is True
    assert os.path.isdir("data_lake/landing") is True
    assert os.path.isdir("data_lake/raw") is True

test = {"01": test_01}[sys.argv[1]]

test()
