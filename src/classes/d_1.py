"""
Class file containing the solution to Day One's puzzles
"""

try:
    from .day import Day
    from helpers.unzip import unzip
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D1(Day):
    """
    Class containing the solution to Day 1
    """
    def __init__(self, debug=False):
        super().__init__(debug=debug)

    def one(self, input_file):
        """
        Adds together the differences between each set of numbers in the input
        """
        input_one = self.read_input(input_file)
        if input_one is None:
            if self.debug:
                print("[!] Exiting...")
            return None
        list1, list2 = unzip(input_one)
        if self.debug:
            print(f"[*] L1 = '{list1[0:3]}'...L2 = '{list2[0:3]}'...")


if __name__ == '__main__':
    print("[!] This is just a class definition!")
