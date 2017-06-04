import string
import secrets
from itertools import cycle
from enum import Enum

LC = string.ascii_lowercase


class Cipher(object):
    ENCODE = 1
    DECODE = -1

    def __init__(self, key=None):
        if key is None:
            self.key = self.random_key()
        else:
            if key.isalpha() and key.islower():
                self.key = key
            else:
                raise ValueError('Key must be alphabetical only!')

        self.shift_values = self.calculate_shifts()

    def random_key(self):
        return "".join(secrets.choice(LC) for _ in range(128))

    def calculate_shifts(self):
        return [ord(c) - ord('a') for c in self.key]

    def encode(self, text):
        return self.shift(text, Cipher.ENCODE)

    def decode(self, cipher):
        return self.shift(cipher, Cipher.DECODE)

    def shift(self, data, direction):
        text_only = [c.lower() for c in data if c.isalpha()]
        zipped = zip(text_only, cycle(self.shift_values))
        return "".join([shift_lc(c, direction * shift) for c, shift in zipped])


class Caesar(object):
    def __init__(self):
        self.cipher = Cipher('d')
        pass

    def encode(self, text):
        return self.cipher.encode(text)

    def decode(self, cipher):
        return self.cipher.decode(cipher)


# This might come in handy later.
def shift_lc(letter, amount):
    shifted_index = (ord(letter) + amount) - ord(LC[0])
    return LC[shifted_index % len(LC)]
