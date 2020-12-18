
def tetrate(a, b):
    if not isinstance(b, int) or not isinstance(a, (float, int, complex)):
        raise TypeError('a must be integer or float and b must be integer')
    if b < 0:
        raise ValueError('currently only support for positive b')
    if b == 0:
        return
    base = a
    while b > 1:
        a = base ** a
        b -= 1
    return a


def n_level_hyperoperation(a, b, lvl):
    # lvl = 0 -> incrementation
    # lvl = 1 -> addition
    # lvl = 2 -> multiplication
    # lvl = 3 -> exponentiation
    # lvl = 4 -> tetration
    # lvl = 5 -> pentation
    # lvl = 6 -> hexation
    # etc...

    if not isinstance(lvl, int):
        raise TypeError('lvl must be positive integer')
    if not isinstance(a, (int, float, complex)) or not isinstance(b, (int, float, complex)):
        raise TypeError('a, b must be a integer, float or complex')

    if lvl < 0:
        raise TypeError('lvl must be positive integer')
    elif lvl == 0:
        return a + 1
    elif lvl == 1:
        return a + b
    elif lvl == 2:
        return a * b
    elif lvl == 3:
        return a ** b
    elif lvl == 4:
        return tetrate(a, b)
    else:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('currently only support for a and b being positive, non-zero integers')
        if a <= 0 or b <= 0:
            raise TypeError('currently only support for a and b being positive, non-zero integers')
        base = a
        while b > 1:
            a = n_level_hyperoperation(base, a, lvl - 1)
            b -= 1
        return a

