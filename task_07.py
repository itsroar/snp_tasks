def combine_anagrams(words):
    indexes = list(range(len(words)))
    sorted_letters = [sorted(w.lower()) for w in words]
    res = []

    for i in indexes:
        if i == -1:
            continue

        group = [words[i]]
        indexes[i] = -1

        for j in indexes:
            if j == -1:
                continue

            if sorted_letters[i] == sorted_letters[j]:
                group.append(words[j])
                indexes[j] = -1

        res.append(group)

    return res
