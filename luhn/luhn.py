class Luhn(object):
    def __init__(self, data):
        self.data = [c for c in data if not c.isspace()]

    """
    Strings of length 1 or less are not valid.
    Spaces are allowed in the input, but they
        should be stripped before checking.
    All other non-digit characters are disallowed.
    """
    def is_valid(self):
        d = self.data
        if len(d) < 2:
            return False

        for c in d:
            if not c.isdigit():
                return False

        return self.validate()

    """
    If the sum is evenly divisible by 10, then the number is valid.
    """
    def validate(self):
        return (sum(self.luhn_doubling()) % 10 == 0)

    """
    The first step of the Luhn algorithm is to
    double every second digit, starting from the right.
    If doubling the number results in a number greater than 9
    then subtract 9 from the product.
    """
    def luhn_doubling(self):
        rev = reverse_digits(self.data)

        def hedge(n): return (n - 9) if n > 9 else n

        for idx in range(1, len(rev), 2):
            rev[idx] = hedge(rev[idx] * 2)

        return rev


# A lone utility function that will probably be relevant elsewhere
def reverse_digits(number):
    return [int(n) for n in number[::-1]]
