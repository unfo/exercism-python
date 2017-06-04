import string
lc = string.ascii_lowercase
rev = lc[::-1]
translation = str.maketrans(lc, rev)

def encode(message):
    # This is uuuuuugly
    cipher = [_chr for _chr in message.lower().translate(translation) if _chr.isalnum()]
    for space in range(4,len(cipher),5):
        cipher[space] += ' '
    return "".join(cipher).rstrip()


def decode(cipher):
    return "".join([_chr for _chr in cipher.translate(translation) if _chr.isalnum()])
