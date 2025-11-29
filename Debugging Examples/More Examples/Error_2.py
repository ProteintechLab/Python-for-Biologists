import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("mice_protein_expression.csv")
col = "DYRK1A_N"
mean = np.meen(df[col])                # 1
std = np.std(df[col])
print(f"Mean: {mean}, SD: {std}")

vals = df[col].head(10).to_list()
plt.bar(range(len(vals)), vals)
plt.xlable("Index")                    # 2
plt.ylabel("Expression")
plt.title("DYRK1A_N (first 10)")
plt.savefig("dyrk1a_barplot.png", dpi="300")  # 3
plt.shwo()                             # 4
df["Log2_DYRK1A_N"] = np.log2(df["DYRK1A_n"]) # 5
