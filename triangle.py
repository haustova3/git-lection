def whatKindOfTriangle(x, y, z):
    if x == y and y == z:
        return 1
    elif x == y or y == z or z == x:
        return 2
