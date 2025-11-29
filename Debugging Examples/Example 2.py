# Have a look at the error code https://learn.ptglab.com/view/courses/python/3293178-coding-examples/10727316-debugging-error-codes

genes = ["BRCA1","TP53","MYC"]

expression_levels = {"BRCA1": 4.2, "TP53": 3.9} 
genes.append(("GAPDH"))      
expression_levels["MYC"] = 5.1    

for g in genes: 
    level = expression_levels.get(g, "NA") 
    if level!="NA" and level > 4:               
        print(f"{g} high: {level}")
