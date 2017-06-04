def word_count(sentence):
	import re
	pat = re.compile('[^a-z0-9]+')
	words = [word for word in pat.split(sentence.lower()) if len(word) > 0]
	simple_freq = {}
	for word in words:
		simple_freq[word] = simple_freq[word] + 1 if word in simple_freq else 1

	return simple_freq

