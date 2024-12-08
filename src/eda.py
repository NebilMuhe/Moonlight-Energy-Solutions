import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(data, columns, title):
    plt.figure(figsize=(12, 6))
    for column in columns:
        plt.plot(data['Timestamp'], data[column], label=column)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.grid()
    plt.show()


# plot_time_series(cleaned_data, ['GHI', 'DNI', 'DHI', 'Tamb'], "Time Series Analysis of GHI, DNI, DHI, and Tamb")



def cleaning_impact(data, sensor_column):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data, x='Cleaning', y=sensor_column, showmeans=True)
    plt.title(f"Impact of Cleaning on {sensor_column}")
    plt.xlabel("Cleaning (0 = No, 1 = Yes)")
    plt.ylabel(sensor_column)
    plt.grid()
    plt.show()

# Example Usage
# cleaning_impact(cleaned_data, 'ModA')
# cleaning_impact(cleaned_data, 'ModB')

def correlation_matrix(data, columns):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data[columns].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

# Example Usage
# correlation_matrix(cleaned_data, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust'])

def wind_analysis(data):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=data, x='WD', y='WS', hue='WSgust', palette='viridis')
    plt.title("Wind Speed and Direction Analysis")
    plt.xlabel("Wind Direction (°N)")
    plt.ylabel("Wind Speed (m/s)")
    plt.grid()
    plt.show()

# Example Usage
# wind_analysis(cleaned_data)

def temperature_analysis(data):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=data, x='RH', y='Tamb')
    plt.title("RH vs. Temperature")

    plt.subplot(1, 2, 2)
    sns.scatterplot(data=data, x='RH', y='GHI')
    plt.title("RH vs. GHI")
    
    plt.tight_layout()
    plt.show()

# Example Usage
# temperature_analysis(cleaned_data)

def plot_histograms(data, columns):
    data[columns].hist(figsize=(12, 8), bins=20, edgecolor='black')
    plt.tight_layout()
    plt.show()

# Example Usage
# plot_histograms(cleaned_data, ['GHI', 'DNI', 'DHI', 'Tamb', 'WS'])
