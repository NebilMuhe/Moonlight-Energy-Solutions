import pandas as pd
from scipy.stats import zscore


def load_data(file_path):
    data = pd.read_csv(file_path)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    print(data.shape)
    return data


def clean_data(data):
    cleaned_data = data.dropna(subset=['Timestamp'])

    if cleaned_data['Comments'].isna().all():
        cleaned_data = cleaned_data.drop(columns=['Comments'])

    numeric_cols = cleaned_data.select_dtypes(
        include=['int64', 'float64']).columns
    cleaned_data[numeric_cols] = cleaned_data[numeric_cols].apply(zscore)
    return data
