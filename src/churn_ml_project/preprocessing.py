from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.impute import SimpleImputer
import pandas as pd

# Kolonlar
BINARY_MAP = {"Yes": 1, "No": 0, "Male": 1, "Female": 0}
BINARY_COLS = ["gender", "Partner", "Dependents", "PhoneService", "PaperlessBilling"]
ONEHOT_COLS = ["InternetService", "Contract", "PaymentMethod", "MultipleLines",
               "OnlineSecurity", "OnlineBackup", "DeviceProtection",
               "TechSupport", "StreamingTV", "StreamingMovies"]
    
NUMERICAL_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]

# Binary map fonksiyonu
def binary_mapper(df):
    df = df.copy()
    for col in BINARY_COLS:
        df[col] = df[col].map(BINARY_MAP)
    # SeniorCitizen zaten sayısal (0/1) olabilir ama emin olmak için int'e çeviriyoruz
    df["SeniorCitizen"] = df["SeniorCitizen"].astype(int)
    return df


# Pipeline 
def build_pipeline():

    # Kategorik 
    cat_pipe = Pipeline([
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("ohe", OneHotEncoder(handle_unknown="ignore",drop="first", sparse_output=False)) # sparse_output=False eklemek genellikle faydalıdır
    ])

    # Sayısal 
    num_pipe = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    # hepsini birleştiriyoruz
    full_pipeline = ColumnTransformer(
        transformers=[
            ("binary",FunctionTransformer(binary_mapper, validate=False), BINARY_COLS + ["SeniorCitizen"]),
            ("cat", cat_pipe, ONEHOT_COLS), 
            ("num", num_pipe, NUMERICAL_COLS)],
        remainder="passthrough")
    return full_pipeline
                      