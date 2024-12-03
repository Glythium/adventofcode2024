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
        self.list1 = []
        self.list2 = []

    def get_input_lists(self, input_file):
        """
        Abstracted ability to unzip and store the sorted lists,
        which are used by both puzzles
        """
        input_one = self.read_input(input_file)
        if input_one is None:
            if self.debug:
                print("[!] Exiting...")
            return None
        self.list1, self.list2 = unzip(input_one)
        self.list1.sort()
        self.list2.sort()

    def one(self, input_file):
        """
        Adds together the differences between each set of numbers in the input
        """
        total = 0
        self.get_input_lists(input_file)
        if self.debug:
            print(f"[*] L1 = '{self.list1[0:3]}'...L2 = '{self.list2[0:3]}'...")
        for i in range(len(self.list1)):
            total += abs(int(self.list1[i]) - int(self.list2[i]))
        return total

    def two(self, input_file):
        """
        Calculates the 'similarity score' by multiplying the numbers in the
        first list by the number of times they appear in the second list
        """
        total = 0
        self.get_input_lists(input_file)
        if self.debug:
            print(f"[*] L1 = '{self.list1[0:3]}'...L2 = '{self.list2[0:3]}'...")
        for i in self.list1:
            total += int(i) * self.list2.count(i)
        return total

if __name__ == '__main__':
    print("[!] This is just a class definition!")
