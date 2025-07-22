import pandas as pd

df = pd.read_csv("data.csv")

# df = pd.read_json("data.json")
# df = df.drop("bio", axis=1)

# print(df.tail())

# print(df.info())

new_df = df.dropna()

print(new_df.to_string())
