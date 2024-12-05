"""
Class file containing the solution to Day Five's puzzles
"""
try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D5(Day):
    """
    Class containing the solution to Day 5
    """
    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.ordering = dict()
        self.pages = list()

    def create_directions_dict(self, directions):
        for d in directions:
            before,after = d.split("|")
            # Create the initial schema for each number if it does not already exist
            try:
                self.ordering[before]
            except KeyError:
                self.ordering[before] = dict()
                self.ordering[before]["before"] = list()
                self.ordering[before]["after"] = list()  
            try:
                self.ordering[after]
            except KeyError:
                self.ordering[after] = dict()
                self.ordering[after]["before"] = list()
                self.ordering[after]["after"] = list()
            # Let the first number know it should come before the next
            self.ordering[before]["before"].append(after)
            # Let the next number know it should come before the first
            self.ordering[after]["after"].append(before)
        if self.debug:
            print(f"Example of directions dict -- '45': {self.ordering['45']}")

    def split_input(self):
        directions = list()
        for line in self.input.split():
            if "|" in line:
                directions.append(line.strip())
            elif "," in line:
                self.pages.append(line.strip().split(","))
        self.create_directions_dict(directions)
        if self.debug:
            print(f"Example of page list -- self.pages[0] = {self.pages[0]}")

    def one(self):
        """
        Identifies lines that follow a given set of number ordering rules
        """
        # To safely use this attribute, we're going to reinitialize it to zero
        self.total = 0
        self.split_input()
        # Iterate through each line of page numbers
        for nums in self.pages:
            is_following_rules = True
            # For each page number in a given line
            for idx,num in enumerate(nums):
                # We'll start with going forward
                for i in range(len(nums) - idx):
                    if idx == i:
                        continue
                    later = nums[i]
                    # Check if our anchor number is supposed to come after
                    #   this later number in the list
                    if later in self.ordering[num]["after"]:
                        # If it is, this is not a valid line
                        is_following_rules = False
                        break
                if not is_following_rules:
                    break
            if is_following_rules:
                if self.debug:
                    print(nums)
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
