import pandas as pd

# Load with handling for duplicates
df = pd.read_csv("messy_data.csv")
df = df.loc[:, ~df.columns.duplicated()] # remove duplicate columns

# Replace 'N/A' with NaN and drop missing rows
df.replace("N/A", pd.NA, inplace=True)
df.dropna(subset=["Concentration"], inplace=True)

# Convert column to float
df["Concentration"] = df["Concentration"].astype(float)
print(df)
