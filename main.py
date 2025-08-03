import pandas as pd


def load_data():
    file_path = input("Enter file path: ")
    try:
        # Determining the file type
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            print("Unsupported file format")
            return None

        print(f"Dataset loaded successfully!")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

def basic_statistics(df):
    print(f"Shape: {df.shape}")
    print("\n Info: ")
    df.info()
    print("\n Describe: ")
    print(df.describe())
    print(f"\n Dtypes: {df.dtypes}")

def create_visualizations(df):  return 0
def missing_values_analysis(df):  return 0
def numerical_analysis(df):  return 0
def categorical_analysis(df):  return 0
def text_analysis(df):  return 0
def correlation_analysis(df):  return 0
def generate_report(df):  return 0

#  call the functions to check
df = load_data()

