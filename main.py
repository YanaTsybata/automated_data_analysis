import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    # Creating a test dataset like Titanic
    data = {
        'age': [22, 38, 26, 35, None, 54, 2, 27, 14, 4, 29, 33, 41, 19, 67],
        'fare': [7.25, 71.28, 7.92, 53.1, 8.05, 51.86, 21.08, 11.13, 30.07, 16.7, 13.5, 26.25, 77.96, 8.66, 26.55],
        'sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'female', 'female', 'male',
                'female', 'male', 'male', 'female'],
        'class': [3, 1, 3, 1, 3, 1, 3, 3, 2, 3, 3, 2, 1, 3, 2],
        'survived': [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        'embarked': ['S', 'C', 'S', 'S', 'S', None, 'S', 'S', 'C', 'S', 'Q', 'C', 'S', 'S', 'C']
    }
    df = pd.DataFrame(data)
    print(f"Test Titanic loaded: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    return df


# def basic_statistics(df):
#    print(f"Shape: {df.shape}")
#    print("\n Info: ")
#    df.info()
#    print("\n Describe: ")
#    print(df.describe())
#    print(f"\n Dtypes: {df.dtypes}")


#def missing_values_analysis(df):
    #  Сount the gaps by columns
#    missing_count = df.isnull().sum()

    #  Total number of lines
#    total_rows = len(df)

    #  Missing persent
#    missing_percent = (missing_count / total_rows) * 100
    #  Visualisation
#    missing_count.plot(kind='bar')
#    plt.show()

    # Results
#    print("Missing values:")
#    print(missing_count)
#    print("\nMissing percentage:")
#    print(missing_percent)


#def numerical_analysis(df):
#    #  Find only numeric columns
#    numeric_cols = df.select_dtypes(include=['number']).columns
#    for x in numeric_cols:
#        print("statistics")

def categorical_analysis(df):  return 0
def text_analysis(df):  return 0
def correlation_analysis(df):  return 0
def generate_report(df):  return 0


def main():
    print("START AUTOMATIC DATA ANALYSIS")
    print("=" * 50)

    # Загружаем данные
    df = load_data()

if __name__ == '__main__':
    main()
