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
import matplotlib.pyplot as plt

# Select a few proteins to visualize expression (first 10 for illustration)
proteins = df.columns[1:11]  # Get the first 10 protein columns (excluding MouseID)
expression = df[proteins].iloc[0]  # Expression levels for the first mouse (row)

plt.bar(proteins, expression)
plt.xlabel("Protein")
plt.ylabel("Expression Level")
plt.title("Protein Expression Across Mice (First Mouse)")
plt.savefig("protein_expression_plot.png", dpi=300)  # Save as PNG
plt.show()
import seaborn as sns

# Boxplot comparing protein expression by genotype (Control vs Trisomic)
sns.boxplot(x="Genotype", y="DYRK1A_N", data=df)  # Using DYRK1A_N for example
plt.title("Protein Expression by Genotype")
plt.savefig("protein_expression_boxplot.svg")  # Save as SVG
plt.show()
import plotly.express as px

# Interactive scatter plot of protein expression across proteins and genotypes
fig = px.scatter(df, x="MouseID", y="DYRK1A_N", color="Genotype",  # Using DYRK1A_N for illustration
                 title="Interactive Protein Expression Plot")
fig.write_html("interactive_expression_plot.html")  # Save as HTML
fig.show()
