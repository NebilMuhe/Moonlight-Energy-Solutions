import pandas as pd
from scipy.stats import zscore

def load_data(file_path): 
    data = pd.read_csv(file_path)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    print(data)
    return data


