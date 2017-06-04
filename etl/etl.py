"""
Transform { n: [letters], m: [others] }
into      { letter: n, letter2: n, letter3: m }
"""


def transform(legacy):
    new_data = {}
    for value, letters in legacy.items():
        for letter in letters:
            new_data[letter.lower()] = value
    return new_data
