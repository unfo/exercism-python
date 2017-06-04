from functools import lru_cache

NUMBERS = {
    0: 'zero',
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    '1c': 'hundred',
    '1k': 'thousand',
    '1M': 'million',
    '1G': 'billion'

}

TENS = {
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',

}


@lru_cache(maxsize=1024)
def number_parts(number):
    """
    English, MF, do you speak it?!
    """
    if number < 0:
        raise AttributeError('Numbers below zero are too hard for me')
    if number >= 1e12:
        raise AttributeError('Way above my pay grade, sorry.')

    if number == 0:
        return NUMBERS[number]

    rest = number

    billions = int(rest / 1e9)
    rest = rest - (billions * 1e9)

    millions = int(rest / 1e6)
    rest = rest - (millions * 1e6)

    thousands = int(rest / 1e3)
    rest = rest - (thousands * 1e3)

    hundreds = int(rest / 1e2)
    rest = rest - (hundreds * 1e2)

    tens = int(rest / 1e1)
    rest = rest - (tens * 1e1)

    last_bit = ""
    if tens == 1:
        last_bit += NUMBERS[rest + 10]
    elif tens > 1:
        last_bit += NUMBERS[tens * 10]
        if rest > 0:
            last_bit += "-%s" % NUMBERS[rest]
    elif rest > 0:
        last_bit = NUMBERS[rest]


    output = []
    things_before_tens = 0
    if billions > 0:
        output.append("%s %s" % (number_parts(billions), NUMBERS['1G']))
        things_before_tens += 1
    if millions > 0:
        output.append("%s %s" % (number_parts(millions), NUMBERS['1M']))
        things_before_tens += 1
    if thousands > 0:
        output.append("%s %s" % (number_parts(thousands), NUMBERS['1k']))
        things_before_tens += 1
    if hundreds > 0:
        output.append("%s %s" % (number_parts(hundreds), NUMBERS['1c']))
        things_before_tens += 1
    if tens > 0 or rest > 0:
        if things_before_tens > 0:
            output.append("and")
        output.append(last_bit)


    return " ".join(output)

def say(number):
    parts = number_parts(number)
    return parts
