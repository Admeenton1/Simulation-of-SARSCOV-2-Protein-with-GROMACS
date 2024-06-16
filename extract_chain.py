from Bio import PDB

def extract_chain(input_pdb, output_pdb, chain_id):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('protein', input_pdb)
    io = PDB.PDBIO()
    class ChainSelect(PDB.Select):
        def accept_chain(self, chain):
            return chain.id == chain_id

    io.set_structure(structure)
    io.save(output_pdb, ChainSelect())

# Example usage
input_pdb = '6lu7.pdb'
output_pdb = '6lu7_chainA.pdb'
chain_id = 'A'

extract_chain(input_pdb, output_pdb, chain_id)
