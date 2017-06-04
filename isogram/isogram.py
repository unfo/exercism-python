def is_isogram(word):
	chars = list(word.lower())
	chars.sort()
	prev = ''
	for char in chars:
		if char.isalpha():
			if char == prev:
				return False
			prev = char
	return True

