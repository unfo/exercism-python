def numeral(n):
    if n >= 4000:
        raise ValueError('Cant do that sir')

    millis = int(n / 1000)
    rest = int(n % 1000)

    cents = int(rest / 100)
    rest = int(rest % 100)

    tens = int(rest / 10)
    ones = int(rest % 10)

    # I know appending strings is bad
    # but here we know they won't be that big
    roman = ''
    if millis > 0:
        roman += "M" * millis

    roman += weird_rule(cents, 'C', 'D', 'M')
    roman += weird_rule(tens, 'X', 'L', 'C')
    roman += weird_rule(ones, 'I', 'V', 'X')

    return roman

def weird_rule(n, single, middle, upper):
    if n == 0:
        combo = ""
    if 0 < n < 4:
        combo = single * n
    elif n == 4:
        combo = single + middle
    elif 4 < n < 9:
        combo = middle + single*(n - 5)
    elif n == 9:
        combo = single+upper
    return combo