"""
Class file containing the solution to Day Three's puzzles
"""
import re
try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D3(Day):
    """
    Class containing the solution to Day 3
    """
    def __init__(self, debug=False):
        super().__init__(debug=debug)
        # Shoutout to https://stackoverflow.com/questions/4666973/how-to-extract-the-substring-between-two-markers
        # and the re modules docs for this pattern. This pattern grabs the
        # contents of the parentheses preceded by the string literal 'mul'
        self.part_one_pattern = re.compile(r'mul\((\d+,\d+)\)')

    def solve(self, input_file):
        """
        Uses regex to find the mul(X,Y) substrings and multiply those numbers
        together and sum it all up
        """
        self.total = 0
        self.lines = self.read_input(input_file)
        for line in self.lines:
            num_list = re.findall(self.part_one_pattern, line)
            for i in num_list:
                nums = i.split(',')
                self.total += int(nums[0]) * int(nums[1])
        return self.total


if __name__ == '__main__':
    print("[!] This is just a class definition!")
