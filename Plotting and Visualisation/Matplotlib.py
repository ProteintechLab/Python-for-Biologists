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
