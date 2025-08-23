import pandas as pd

df = pd.read_csv(r"C:/Users/luayd/Documents/Quant project start/portfolio-optimisation-dl/data/220 obs 4 asset.csv")

print(df.head())
print(df.info())
print(df.describe())

df. plot(title="Asset time series", figsize=(10, 5))