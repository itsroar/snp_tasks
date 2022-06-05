def get_word_borders(left_border: int, text: str) -> tuple:
    # пропускаем небуквенные символы
    len_ = len(text)
    while left_border < len_ and not text[left_border].isalpha():
        left_border += 1

    if left_border == len_:
        return left_border, left_border

    right_border = left_border + 1
    while right_border < len_ and text[right_border].isalpha():
        right_border += 1

    return left_border, right_border


def count_words(text: str):
    res = {}
    i = 0
    while i < len(text):
        borders = get_word_borders(i, text)
        i = borders[1]

        w = text[borders[0]:borders[1]].lower()
        if w in res:
            res[w] += 1
        else:
            res[w] = 1

    return res
