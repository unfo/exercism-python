def hey(sentence):
	"""
	Bob is a lackadaisical teenager. In conversation, his responses are very limited.
	Bob answers 'Sure.' if you ask him a question.
	He answers 'Whoa, chill out!' if you yell at him.
	He says 'Fine. Be that way!' if you address him without actually saying
	anything.
	He answers 'Whatever.' to anything else.
	"""
	sentence = sentence.strip()
	response = "Whatever."
	if len(sentence) == 0:
		response = "Fine. Be that way!"
	elif sentence.startswith("Let's"):
		# This is just silly. If it ends with an ! then it is shouting...
		response = "Whatever."
	elif sentence[-1] == "!" or sentence.isupper():
		response = "Whoa, chill out!"
	elif sentence[-1] == "?":
		response = "Sure."

	return response