#data_utils.py is a collection of methods
import matplotlib.pyplot as plt
import seaborn as sns

def missing_values_barplot(DataFrame) -> None:
    """Creates a bar plot showing the number of missing values per column in the given DataFrame."""
    missing_values = DataFrame.isnull().sum()
    missing_values = missing_values[missing_values > 0]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=missing_values.index, y=missing_values.values)
    plt.xticks(rotation=90)
    plt.title("Missing Values per Column")
    plt.ylabel("Number of Missing Values")
    plt.xlabel("Columns")
    plt.show()
