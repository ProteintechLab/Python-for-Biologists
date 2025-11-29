import pandas as pd, numpy as np, matplotlib.pyplot as plt
df = pd.read_csv("mice_protein_expression.csv")
col = "DYRK1A_N"
mean = np.mean(df[col])
std = np.std(df[col])
print(f"Mean: {mean}, SD: {std}")
vals = df[col].head(10).to_list()
plt.bar(range(len(vals)), vals)
plt.xlabel("Index")
plt.ylabel("Expression")
plt.title("DYRK1A_N (first 10)")
plt.savefig("dyrk1a_barplot.png", dpi=300)
plt.show()
df["Log2_DYRK1A_N"] = np.log2(df["DYRK1A_N"])
