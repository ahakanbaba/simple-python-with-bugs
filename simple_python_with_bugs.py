def atoi(s: str) -> int:
    if not s:
        raise ValueError("Input string is empty")

    num = 0
    start = 0
    negative = False

    # Check for negative numbers
    if s[0] == "-":
        negative = True
        start = 1
    elif s[0] == "+":
        start = 1

    for i in range(start, len(s)):
        # Horner's method: accumulate the value
        num = num * 10 + (ord(s[i]) - ord("0"))

    if negative:
        num = -num

    return num
