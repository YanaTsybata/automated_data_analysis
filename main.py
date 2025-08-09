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


def basic_statistics(df):
    print("\n" + "=" * 50)
    print(" Basic Statistics")
    print("=" * 50)

    print(f" Dataset size: {df.shape[0]} rows, {df.shape[1]} columns")

    print("\n Information about the columns:")
    df.info()

    print("\n Descriptive statistics of numerical columns:")
    print(df.describe())

    print(f"\n️ Data types:")
    for col, dtype in df.dtypes.items():
        print(f"  {col}: {dtype}")


def missing_values_analysis(df):
    print("\n" + "=" * 50)
    print(" ANALYSIS OF MISSED VALUES")
    print("=" * 50)

    # Counting gaps by columns
    missing_count = df.isnull().sum()
    total_rows = len(df)
    missing_percent = (missing_count / total_rows) * 100

    # We create a table with the results
    missing_df = pd.DataFrame({
        'Column': missing_count.index,
        'Missing values': missing_count.values,
        'Percentage': missing_percent.values
    })

    print(" Summary of missing values:")
    print(missing_df.to_string(index=False))

    # Missing values visualization
    if missing_count.sum() > 0:
        plt.figure(figsize=(10, 6))
        missing_count[missing_count > 0].plot(kind='bar', color='coral')
        plt.title('Number of missing values per column')
        plt.xlabel('Columns')
        plt.ylabel('Number of missing values')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print(" No missing values found!")


def categorical_analysis(df):
    print("\n" + "="*50)
    print("CATEGORICAL Data Analyses")
    print("="*50)

    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    if len(categorical_cols) == 0:
        print("No categorised columns were found!")
        return

    print(f"Categorised columns found:: {list(categorical_cols)}")

    # Analysis of each categorical column
    for col in categorical_cols:
        print(f"\nColumn analysis '{col}':")
        value_counts = df[col].value_counts()
        print(f"  Unique values: {df[col].nunique()}")
        print(f"  🔝 Top values:")
        for value, count in value_counts.head(5).items():
            percentage = (count / len(df)) * 100
            print(f"    {value}: {count} ({percentage:.1f}%)")

    # Visualisation of categorical data
    if len(categorical_cols) > 0:
        fig, axes = plt.subplots(1, len(categorical_cols), figsize=(6 * len(categorical_cols), 4))
        if len(categorical_cols) == 1:
            axes = [axes]

        for i, col in enumerate(categorical_cols):
            df[col].value_counts().plot(kind='bar', ax=axes[i], color='lightgreen')
            axes[i].set_title(f'Distribution {col}')
            axes[i].set_xlabel(col)
            axes[i].set_ylabel('Quantity')
            axes[i].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.show()


def text_analysis(df):
    #  Text data analysis
    print("\nTEXT ANALYSIS")
    print("-" * 30)

    text_cols = df.select_dtypes(include=['object']).columns

    print(f"Text columns: {list(text_cols)}")

    for col in text_cols:
        print(f"\n'{col}' column:")
        print(f"  Unique values: {df[col].nunique()}")
        print(f"  Most common: {df[col].mode().iloc[0] if len(df[col].mode()) > 0 else 'None'}")


def correlation_analysis(df):
    #  Correlation analysis
    print("\nCORRELATION ANALYSIS")
    print("-" * 30)

    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) < 2:
        print("Need at least 2 numeric columns!")
        return

    print(f"Numeric columns: {list(numeric_cols)}")

    # Correlation between the first two columns
    col1, col2 = numeric_cols[0], numeric_cols[1]
    correlation = df[col1].corr(df[col2])
    print(f"Correlation between {col1} and {col2}: {correlation:.2f}")

def generate_report(df):
    """Generate a summary report"""
    print("\n" + "=" * 70)
    print(" FINAL DATA ANALYSIS REPORT")
    print("=" * 70)

    print(f" Dataset size: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f" Numerical columns: {len(df.select_dtypes(include=['number']).columns)}")
    print(f"️ Categorical columns: {len(df.select_dtypes(include=['object', 'category']).columns)}")
    print(f" Total missing values: {df.isnull().sum().sum()}")


def main():
    print("START AUTOMATIC DATA ANALYSIS")
    print("=" * 50)

    functions = {
        "1": basic_statistics,
        "2": missing_values_analysis,
        "3": categorical_analysis,
        "4": text_analysis,
        "5": correlation_analysis,
        "6": generate_report
    }

    # loading data
    df = load_data()
    print("What do you want to check/find/see?: \n1 - basic_statistics,\n2 - missing_values_analysis\n3 - categorical_analysis,\n4 - text_analysis,\n5 - correlation_analysis,\n6 - generate_report,\n7 - everything ")
    choice = input(f"Write the number or numbers (e.g., 1,2,3 or just 1): ").strip()
    if choice == 7:
        for func in functions.values():
            func(df)
    else:
        numbers = [num.strip() for num in choice.split(",")]
        for num in numbers:
            if num in functions:
                functions[num](df)
            else:
                print(f"Incorrect number: {num}")

if __name__ == '__main__':
    main()
