import pandas as pd
import numpy as np

# Load the Mice Protein Expression dataset
df = pd.read_csv("mice_protein_expression.csv")

# Display the first 10 rows
print(df.head(10))  # Or df.head(20) for the first 20 rows

# Filter genes with high expression
high_expr = df[df["DYRK1A_N"] > 5.0]
print(high_expr)

# Example: Protein expression levels (subset for illustration)
expression_levels = np.array(df["DYRK1A_N"].head(10))  # Using DYRK1A_N for illustration

# Perform operations
print("Mean:", np.mean(expression_levels))  # Calculate mean
print("Standard deviation:", np.std(expression_levels))  # Calculate standard deviation
