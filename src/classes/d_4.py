"""
Class file containing the solution to Day Four's puzzles
"""
import re
try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D4(Day):
    """
    Class containing the solution to Day 3
    """
    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)

    def one(self):
        """
        TBD
        """
        return self.input

    def two(self):
        """
        TBD
        """
        pass


if __name__ == '__main__':
    print("[!] This is just a class definition!")
