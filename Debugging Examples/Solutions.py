# Example 1 in this folder

sequence = "ATG cgt TAA"
def transcribe_dna_to_rna(dna):
    dna = dna.strip().replace(" ", "")
    rna = dna.upper().replace("T","U")
    return rna
print("RNA:", transcribe_dna_to_rna(sequence))
print(sequence.replace(" ", "")[0:3])

# Example 2 in this folder

genes = ["BRCA1","TP53","MYC"]
expression_levels = {"BRCA1": 4.2, "TP53": 3.9}
genes.append("GAPDH")
expression_levels["MYC"] = 5.1
for g in genes:
    level = expression_levels.get(g, "NA")
    if level != "NA" and level > 4:
        print(f"{g} high: {level}")

# Example 3 in this folder

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

protein_data = pd.read_csv("https://github.com/ProteintechLab/Introduction-to-Python-for-Biologists/blob/main/Plotting%20and%20Visualisation/mice_protein_expression.csv") # Correct filename 

def compare_expression(a, b): 
    if a not in protein_data.columns or b not in protein_data.columns: 
        raise ValueError("One or both proteins not found in the dataset.") 
    diff = protein_data[a] - protein_data[b] 
    print("Average difference:", np.mean(diff)) 
    return diff 

diff = compare_expression("DYRK1A_N", "CDK5_N") 

plt.figure(figsize=(6, 4)) 
plt.bar(range(len(diff)), diff) 
plt.xlabel("Mouse") 
plt.ylabel("Difference") 
plt.title("Expression Difference: DYRK1A vs CDK5") 
plt.show()
