import pandas as pd


data = dict(Malmö = 347949, Stockholm = 975551, Uppsala = 233839, Göteborg = 583056)
series_cities = pd.Series(data=data)
df_cities = pd.DataFrame({"Kommun": series_cities.index,"Befolkning": series_cities.values})
# a)
print(df_cities["Kommun"])
# b)
print(df_cities[df_cities["Kommun"] == "Göteborg"])
# c)
df_sorted = df_cities.sort_values(by="Befolkning", ascending=False).reset_index(drop=True)
print(df_sorted)
# d)
print(df_sorted.head(3))
# e)
df_cities["Population(%)"] = (df_cities["Befolkning"] / 10379295 * 100).round(2)
print(df_cities)
