import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Load data 
protein_data = pd.read_csv("https://github.com/ProteintechLab/Introduction-to-Python-for-Biologists/blob/main/Plotting%20and%20Visualisation/mice_protein_expressionsss.csv") #Potential bug

# Print first 5 entries 
print(protein_data.head(5)) 

# Compare two proteins 
def compare_expression(a, b)                       
    diff = protein_data[a] - protein_data[b]       
    print("Average difference:", np.mean(diff)) 
    return diff 

# Call function 
compare_expression("DYRK1A_N", "CDK5_N") 

# Bar plot of result 
plt.figure(figsize=6, 4)                           
plt.bar(range(len(diff)), diff)                     
plt.xlabel("Mouse") 
plt.ylabel("Difference") 
plt.title("Expression Difference: DYRK1A vs CDK5") 
plt.show()
