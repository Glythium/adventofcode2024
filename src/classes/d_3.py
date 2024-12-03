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
        self.pattern = re.compile(r'mul\((\d+,\d+)\)')

    def one(self, input_file):
        """
        Uses regex to find the mul(X,Y) substrings and multiply those numbers
        together and sum it all up
        """
        total = 0
        self.lines = self.read_input(input_file)
        for line in self.lines:
            num_list = re.findall(self.pattern, line)
            for i in num_list:
                nums = i.split(',')
                total += int(nums[0]) * int(nums[1])
        return total

    def two(self, input_file):
        """
        Uses regex to find the mul(X,Y) substrings and multiply those numbers
        together and sum it all up, but not if there was a preceding 'don't'
        """
        total = 0
        self.lines = self.read_input(input_file)
        for line in self.lines:
            # Start by finding the first match
            match = re.search(self.pattern, line)
            while match:
                # If we find a 'don't()' before our next mul
                if "don't()" in line[:match.start()]:
                    # Just start looking for the next do()
                    line = line.split("don't()")[1]
                    new_start = line.find("do()")
                else:
                    # Otherwise, we have a mul we can add
                    nums = match.groups()[0].split(',')
                    total += int(nums[0]) * int(nums[1])
                    # Set the new start of the line just after this mul
                    new_start = match.end()
                # Set the new start of the line and find the next mul
                line = line[new_start:]
                match = re.search(self.pattern, line)
        return total


if __name__ == '__main__':
    print("[!] This is just a class definition!")
