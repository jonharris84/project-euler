def threes_and_fives(n):
    total = 0  # type: int
    for x in range(n):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total