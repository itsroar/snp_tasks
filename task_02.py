def coincidence(lst: list = (), r: range = range(0)):
    res = []

    for elem in lst:
        try:
            if r.start <= elem < r.stop:
                res.append(elem)
        except TypeError:
            continue

    return res
