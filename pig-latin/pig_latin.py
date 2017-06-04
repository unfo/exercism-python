def translate(word):
    if any(c.isspace() for c in word):
        return " ".join([translate(word) for word in word.split()])

    vowels = ['a', 'e', 'i', 'o', 'u']
    AYYYYYY_LLLMAO = 'ay'
    for vowel in vowels:
        if word.startswith(vowel):
            return word + AYYYYYY_LLLMAO

    # special cases
    if (word.startswith('sch') or
        word.startswith('squ') or
        word.startswith('thr')):
        return word[3:] + word[0:3] + AYYYYYY_LLLMAO
    elif (word.startswith('qu') or
          word.startswith('th') or
          word.startswith('ch')):
        return word[2:] + word[0:2] + AYYYYYY_LLLMAO
    elif word.startswith('x') or word.startswith('y'):
        if len(word) > 1:
            if word[1] in vowels:
                return word[1:] + word[0] + AYYYYYY_LLLMAO
            else:
                return word + AYYYYYY_LLLMAO
    else:
        return word[1:] + word[0] + AYYYYYY_LLLMAO
