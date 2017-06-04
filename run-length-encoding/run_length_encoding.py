import re

def decode(code):
    if code == "":
        return ""

    pat = re.compile('((\d+)?([a-zA-Z ]))')
    message = ""
    for block in re.finditer(pat, code):
        multiplier = block.group(2)
        multiplier = 1 if multiplier is None else int(multiplier)
        character = block.group(3)
        message += "".center(multiplier, character)
    return message


# Not yet happy with how verbose this code is.
# Will have to return to make it more snazzy
def encode(cipher):
    if cipher == "":
        return ""
    code = prev = ""
    count = 0
    for _char in cipher:
        if _char == prev:
            count += 1
        else:
            if prev != "":
                if count < 2:
                    code += prev
                else:
                    code += str(count) + prev
            prev = _char
            count = 1

    if count < 2:
        code += prev
    else:
        code += str(count) + prev

    return code