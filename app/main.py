import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_preparation import load_data,clean_data


if __name__ == '__main__':
    data = load_data('data/benin-malanville.csv')

    data = clean_data(data)
    
    