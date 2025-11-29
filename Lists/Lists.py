genes = ["BRCA1", "TP53", "MYC"]

# Indexing
print(f"The gene at index 0 is {genes[0]}")

# Adds element to the end of the list
genes.append("CDK2")
print(f"The appended gene list is {genes}")

# Adds multiple elements from another list to the end  
genes.extend(["CDK2", "KRAS"])
print(f"The extended gene list is {genes}")

# Inserts an element at a specific position in the list  
genes.insert(1, "GAPDH")
print(f"The element has been inserted, and the updated list is {genes}")

# Removes the first occurrence of a specific element  
genes.remove("TP53")
print(f"The updated list after removing the element is {genes}")

# Removes and returns an element from the list (by index or last item)  
print(f"The removed element from the list is {genes.pop()}")

# Returns the index of the first occurrence of an element  
print(f"The index of BRCA1 is {genes.index('BRCA1')}")

# Counts the number of occurrences of an element
print(f"The number of times GAPDH appears is {genes.count('GAPDH')}")

# Sorts the list in ascending order  
genes.sort()
print(f"This is the list in ascending order: {genes}")

# Reverses the order of the list  
genes.reverse()
print(f"This is the list in reverse: {genes}")

# Removes all elements from the list, making it empty
genes.clear()
print(genes)

# Dictionaries
expression_levels = {"TP53": 4.5, "CDK2": 3.2}
print(expression_levels["TP53"])
