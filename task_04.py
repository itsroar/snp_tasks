def sort_list(lst: list):
    if len(lst) == 0:
        return []

    min_ = min(lst)
    max_ = max(lst)
    res = list(map(lambda i: min_ if i == max_ else max_ if i == min_ else i, lst))
    res.append(min_)
    return res
