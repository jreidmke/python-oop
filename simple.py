def add_one(x):
    """Add one to argument
    >>> add_one(1)
    3
    """
    return x + 1

print(add_one(1))

import doctest
doctest.testmod()