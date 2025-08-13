# 📊 Automated Data Analysis Tool

A tool for quick CSV data analysis with automatic statistics generation and visualizations.

## 🎯 Features

- **Basic Statistics** - dataset size, data types, descriptive statistics
- **Missing Values Analysis** - detection and visualization of missing data
- **Categorical Analysis** - distribution of values in categorical columns
- **Text Analysis** - analysis of text data
- **Correlation Analysis** - relationships between numerical variables
- **Summary Report** - comprehensive dataset overview

## 🚀 Installation


```bash
pip install pandas matplotlib
```

## 📋 Usage

1. Place your CSV file in the project folder
2. Update the file path in the `load_data()` function:
   ```python
   file_path = "path/to/your/file.csv"
   ```
3. Run the script:
   ```bash
   python data_analysis.py
   ```

## 🔧 Interactive Menu

After running, choose the type of analysis:
- `1` - Basic statistics
- `2` - Missing values analysis  
- `3` - Categorical data analysis
- `4` - Text data analysis
- `5` - Correlation analysis
- `6` - Summary report
- `7` - Run all analyses

You can select multiple options with commas: `1,2,3`

## 📊 Example Output

```
START AUTOMATIC DATA ANALYSIS
==================================================
Dataset loaded: (418, 11)
Columns: ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', ...]

What do you want to check/find/see?: 
1 - basic_statistics
2 - missing_values_analysis
...
Write the number or numbers (e.g., 1,2,3 or just 1): 1

==================================================
 Basic Statistics
==================================================
 Dataset size: 418 rows, 11 columns

 Descriptive statistics of numerical columns:
       PassengerId      Pclass         Age       SibSp       Parch        Fare
count   418.000000  418.000000  332.000000  418.000000  418.000000  417.000000
mean   1100.500000    2.265550   30.272590    0.447368    0.392344   35.627188

```

## 🛠️ Technologies

- **Python 3.7+**
- **Pandas** - data manipulation
- **Matplotlib** - data visualization

