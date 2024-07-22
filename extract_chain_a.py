def extract_chain_a(pdb_file, output_file):
    with open(pdb_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith("ATOM") and line[21] == 'A':
                outfile.write(line)
            elif line.startswith("TER") and line[21] == 'A':
                outfile.write(line)
        outfile.write("END\n")

extract_chain_a('6lu7.pdb', '6lu7_chainA.pdb')