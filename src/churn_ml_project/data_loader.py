from pathlib import Path
import pandas as pd

#csv dosyasının yolunu ayarlıyorum
DATA_PATH = (Path(__file__).resolve().parents[2] / "data" / "dataset.csv")

def _read_raw(path: str | Path= DATA_PATH) -> pd.DataFrame:
    """
    Csvyi okuyoruz, totalchargesı numeriğe çevirip eksik satırları silip indexi resetliyoruz (2.notebookda yapıldığı gibi)
    """
    df=pd.read_csv(path)

    df["TotalCharges"]= pd.to_numeric(df["TotalCharges"], errors="coerce")
    df= df.dropna().reset_index(drop=True)
    return df


def load_xy(path: str | Path=DATA_PATH, target: str ="Churn",id_col: str= "customerID"):
    """
    data framei alır X-y olarak ayırır
    """
    df= _read_raw(path)
    y=df[target]
    X=df.drop([id_col, target], axis=1)
    return X,y


def load_df(path: str | Path=DATA_PATH) -> pd.DataFrame:
    """
    data frame lazım olursa 
    """
    return _read_raw(path)
