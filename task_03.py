def max_odd(array):
    res = None

    for elem in array:
        try:
            num = int(elem)
            if abs(num) & 1 and (res is None or res < num):
                res = num
        except TypeError:
            continue
        except ValueError:
            continue

    return res
