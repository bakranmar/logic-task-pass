def remove_char(string: str, char: str) -> str:
    for ch in string:
        if ch != char:
            continue
        string = string.replace(char, '')
    return string


print(remove_char("abcdefg", 'd'))