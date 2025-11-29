from Bio.PDB import PDBparser          # 1
parser = PDBParser()
structure = parser.get_structure("prot","1U8F.pdb")
model = structure[0]
res_count = 0
for chain in model.get_chains():
    for res in chain.get_residues():
        if re.id[0] == " ":           #hetero flag check - re is supposed to be res
            res_count = res_count + 1
print(f"Residues counted: {rescount}") # 3
print("Chains:", len(model.child_list)) # 4
print(f"First chain id: {chain}")       # 5
