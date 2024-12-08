import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_preparation import load_data,clean_data
from src.analysis import summary_statistics,data_quality_check
from src.eda import plot_time_series,cleaning_impact,correlation_matrix,wind_analysis,temperature_analysis,plot_histograms


def main():
    pass

if __name__ == '__main__':
    filepath = ''   #path of the csv file
    data = load_data(filepath)

    cleaned_data = clean_data(data)

    summary = summary_statistics(cleaned_data)

    data_quality = data_quality_check(data)

    plot_time_series(cleaned_data, ['GHI', 'DNI', 'DHI', 'Tamb'], "Time Series Analysis of GHI, DNI, DHI, and Tamb")
    cleaning_impact(cleaned_data, 'ModA')
    cleaning_impact(cleaned_data, 'ModB')
    
    correlation_matrix(cleaned_data, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust'])
    wind_analysis(cleaned_data)
    temperature_analysis(cleaned_data)
    plot_histograms(cleaned_data, ['GHI', 'DNI', 'DHI', 'Tamb', 'WS'])




    