"""
Class file containing the solution to Day Five's puzzles
"""
try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D4(Day):
    """
    Class containing the solution to Day 5
    """
    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)

    def one(self):
        """
        TBD
        """
        # To safely use this attribute, we're going to reinitialize it to zero
        self.total = 0
        return self.total

    def two(self):
        """
        TBD
        """
        # To safely use this attribute, we're going to reinitialize it to zero
        self.total = 0
        return self.total


if __name__ == '__main__':
    print("[!] This is just a class definition!")
