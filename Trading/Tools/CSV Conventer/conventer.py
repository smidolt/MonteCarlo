import pandas as pd
df = pd.read_csv("WRITE_NAME_OF_YOUR_CSV.csv")
df["Price"] = df["Price"].str.replace(",", "").astype(float)
df["Price"] = df["Price"].astype(int)
df.to_csv("new_file.csv", index=False)

