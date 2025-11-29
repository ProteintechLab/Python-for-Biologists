import seaborn as sns

# Boxplot comparing protein expression by genotype (Control vs Trisomic)
sns.boxplot(x="Genotype", y="DYRK1A_N", data=df)  # Using DYRK1A_N for example
plt.title("Protein Expression by Genotype")
plt.savefig("protein_expression_boxplot.svg")  # Save as SVG
plt.show()
