# Check expected columns
expected = ["Sample", "Concentration"]
for col in expected:
  if col not in df.columns:
    raise ValueError(f"Missing column: {col}")# Check size
  if len(df) < 5:
    print("Warning: Very small dataset")# Check value range
  if df["Concentration"].max() > 10:
    print("Values exceed expected range")
