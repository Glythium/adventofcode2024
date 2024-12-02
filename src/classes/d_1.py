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
        total = 0
        input_one = self.read_input(input_file)
        if input_one is None:
            if self.debug:
                print("[!] Exiting...")
            return None
        list1, list2 = unzip(input_one)
        list1.sort()
        list2.sort()
        if self.debug:
            print(f"[*] L1 = '{list1[0:3]}'...L2 = '{list2[0:3]}'...")
        for i in range(len(list1)):
            total += abs(int(list1[i]) - int(list2[i]))
        return total


if __name__ == '__main__':
    print("[!] This is just a class definition!")
