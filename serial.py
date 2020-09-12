"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        "Create an int starting point"
        self.start = start
        self.next = start


    def generate(self):
        "Adds one to self"
        self.next += 1
        return self.next

    def reset(self):
        "Resets self to original starting point"
        self.next = self.start
