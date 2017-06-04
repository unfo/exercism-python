import string
# deliberately left out shift_by==0 optimization
def rotate(message, shift_by):
	uc = string.ascii_uppercase
	lc = string.ascii_lowercase
	_len = len(uc)
	cipher = ""
	for c in message:
		if c.isalpha():
			alphabet = uc if c in uc else lc
			idx = (lc.index(c.lower()) + shift_by) % _len
			cipher += alphabet[idx]
		else:
			cipher += c

	return cipher
