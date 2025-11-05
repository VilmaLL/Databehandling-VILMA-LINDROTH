import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\vilma\Databehandling-VILMA-LINDROTH\komtopp50_2020.xlsx", skiprows = 6)
df.columns = ["Rank_2020", "Rank_2019", "Municipality", "Population_2020", "Population_2019", "Change"]

df_largest = df.sort_values(by="Population_2020", ascending = False).reset_index(drop=True)
print(df_largest.head())
largest5 = df_largest.iloc[:5]

df_smallest = df.sort_values(by="Population_2020", ascending = True)
print(df_smallest.head())
smallest5 = df_smallest.iloc[:5]

total_population_2020 = df["Population_2020"].sum()
total_population_2019 = df["Population_2019"].sum()
print(f"Populationen i Sverige 2020: {total_population_2020}")
print(f"Populationen i Sverige 2019: {total_population_2019}")

fig, axes = plt.subplots(1, 2, dpi = 80, figsize = (10, 6))
titles = ["5 största kommuner i Sverige 2020", "5 minsta kommuner i Sverige 2020"]
data_frames = [largest5, smallest5]
x_column = ["Municipality", "Municipality"]

for i, (data, title) in enumerate(zip(data_frames, titles)):
    sns.barplot(data = data, x = x_column[i], y = "Population_2020", ax = axes[i])
    axes[i].set(title = title)
    axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation = 90)
plt.show()