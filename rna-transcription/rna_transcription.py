def to_rna(dna):
	wrong_dna = [c for c in dna if c not in ['G','C','T','A']]
	if len(wrong_dna) > 0:
		return ''
	else:
		tr = str.maketrans('GCTA','CGAU')
		return dna.translate(tr)

