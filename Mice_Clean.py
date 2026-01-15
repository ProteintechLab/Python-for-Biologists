from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
mice_protein_expression = fetch_ucirepo(id=342) 
  
# data (as pandas dataframes) 
X = mice_protein_expression.data.features 
y = mice_protein_expression.data.targets 
  
# metadata 
print(mice_protein_expression.metadata) 
  
# variable information 
print(mice_protein_expression.variables) 

print(X.shape)
print(X.head())
print(X.isna().sum().head())

# Create working copy
df = X.copy()

# Drop missing values for a key protein
df = df.dropna(subset=["DYRK1A_N"])

# Ensure numeric data types
df["DYRK1A_N"] = df["DYRK1A_N"].astype(float)

# Sanity Check
# Check expected columns

expected_columns = ["DYRK1A_N", "BDNF_N", "NR1_N"]
for col in expected_columns:
    if col not in df.columns:
        raise ValueError(f"Missing expected column: {col}")

# Check dataset size
if len(df) < 500:
    print("Warning! Dataset is smaller than expected after cleaning")

if df["DYRK1A_N"].max() > 20:
    print("Warning! Expression values exceed expected biological range")

