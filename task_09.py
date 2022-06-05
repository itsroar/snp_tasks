def connect_dicts(dict1: dict, dict2: dict):
    seq = (dict2, dict1) if sum(dict1.values()) > sum(dict2.values()) else (dict1, dict2)
    res = seq[0].copy()  # сначала берём значения менее приоритетного словаря
    res.update(seq[1])   # потом дополняем значениями более приоритетного словаря
    return {k: v for k, v in sorted(res.items(), key=lambda item: item[1]) if v >= 10}
