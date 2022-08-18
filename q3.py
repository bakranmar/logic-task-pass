def char_count(string: str, char: str) -> int:
    count = 0
    for ch in string:
        if ch == char: count += 1
    return count


print(char_count("aaaawsdwsdw", 'a'))
