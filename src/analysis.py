from scipy.stats import zscore

def summary_statistics(data):
    summary_data = data.drop(columns=['Timestamp'])
    summary = summary_data.describe().T 
    
    summary['median'] = summary_data.median()
    summary['skewness'] = summary_data.skew()
    summary['kurtosis'] = summary_data.kurtosis()

    return summary



def data_quality_check(data):
    missing_values = data.isnull().sum()
    positive_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust', 'TModA', 'TModB']
    negative_values = (data[positive_columns] < 0).sum()

    numeric_cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 'RH', 'WS', 'WSgust', 'WSstdev', 'BP', 'TModA', 'TModB']
    zscore_data = data[numeric_cols].apply(zscore)
    outliers = (zscore_data.abs() > 3).sum()

    report = {
        "Missing Values": missing_values,
        "Negative Values": negative_values,
        "Outliers (Z-Score > 3)": outliers
    }
    
    return report

