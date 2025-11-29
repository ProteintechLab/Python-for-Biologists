from Bio.PDB import PDBParser
parser = PDBParser()
structure = parser.get_structure("prot","1U8F.pdb")
model = structure[0]
res_count = 0
chains = list(model.get_chains())
for chain in chains:
    for res in chain.get_residues():
        if res.id[0] == " ":
            res_count += 1
print(f"Residues counted: {res_count}")
print("Chains:", len(chains))
print(f"First chain id: {chains[0].id if chains else 'NA'}")
