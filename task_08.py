def multiply_numbers(inputs=None):
    res = None
    for ch in str(inputs):
        if ch.isdigit():
            if res is None:
                res = 1
            res *= int(ch)

    return res
