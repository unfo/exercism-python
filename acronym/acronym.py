import re


def abbreviate(name):
    wordlist = re.split(' +', re.sub('[^ a-zA-Z]', ' ', name))
    # can't use w.upper() because it only capitalizes the _first_
    # letter and lowercases the others. HyperText -> Hypertext
    cap_first_letters = [w[0].upper() + w[1:] for w in wordlist]
    acro = ""
    for word in cap_first_letters:
        # Grab only first letter of an all caps word
        # like GNU or PHP
        if word.isupper():
            acro += word[0]
        else:
            # Otherwise grab all uppercase letters of this word
            acro += re.sub('[^A-Z]', '', word)
    return acro
