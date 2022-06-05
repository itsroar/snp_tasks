def is_palindrome(string):
    string = str(string).lower()
    l = 0
    r = len(string) - 1

    while l < r:
        if not (string[l].isdigit() or string[l].isalpha()):
            l += 1
            continue

        if not (string[r].isdigit() or string[r].isalpha()):
            r -= 1
            continue

        if string[l] != string[r]:
            return False

        l += 1
        r -= 1

    return True
