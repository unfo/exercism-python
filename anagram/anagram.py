def detect_anagrams(word, words):
    return [wrd for wrd in words if sorted(word.lower()) == sorted(wrd.lower()) and word.lower() != wrd.lower()]
