def on_square(n):
    if 0 < n < 65:
        return 1 << (n-1)
    else:
        raise ValueError("It puts the grains on the board")


def total_after(n):
    if 0 < n < 65:
        return (1 << n) - 1
    else:
        raise ValueError("It puts the grains on the board")
