def is_pangram(word):
	import string
	return len(set([c for c in word.lower() if c.isalpha()])) == len(string.ascii_lowercase)

	
