def distance(a, b):
	if len(a) != len(b):
		raise ValueError('Length mismatch')
	return len([err for err in list(zip(a,b)) if err[0] != err[1]])
