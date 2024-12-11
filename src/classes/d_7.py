"""
Class file containing the solution to Day Five's puzzles
"""
try:
    import random
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D7(Day):
    """
    Class containing the solution to Day 7
    """
    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)

    def generate_possible_permutations(self, nums, possible_ops):
        possible_permutations = set()
        possible_spots = len(nums) - 1
        # Build the permutation list 
        while len(possible_permutations) < self.count_possible_permutations(nums, possible_ops):
            perm = list()
            for i in range(possible_spots):
                idx = random.randint(0, len(possible_ops) - 1)
                perm.append(possible_ops[idx])
            possible_permutations.add(tuple(perm))
        return possible_permutations

    def count_possible_permutations(self, nums, possible_ops):
        return len(possible_ops) ** (len(nums) - 1)

    def do_math(self, x, y, operator):
        value = 0
        if operator == '+':
            value = x + y
            if self.debug:
                print(f"{value} = {x} + {y}")
        elif operator == '*':
            value = x * y
            if self.debug:
                print(f"{value} = {x} * {y}")
        elif operator == "||":
            value = int(str(x) + str(y))
            if self.debug:
                print(f"{value} = {x} || {y}")
        return value
 
    def one(self):
        """
        Doing some math!
        """
        # To safely use this attribute, we're going to reinitialize it to zero
        self.total = 0
        possible_ops = ['+', '*']
        self.input = self.input.split('\n')
        for line in self.input:
            sum,nums = line.split(':')
            nums = nums.split()
            count_perms = self.count_possible_permutations(nums, possible_ops)
            permutations = self.generate_possible_permutations(nums, possible_ops)
            for perm in permutations:
                line_total = 0
                for idx,op in enumerate(perm):
                    x = int(nums[idx])
                    y = int(nums[idx + 1])
                    if idx == 0:
                        line_total = self.do_math(x, y, op)
                    else:
                        line_total = self.do_math(line_total, y, op)
                if line_total == int(sum):
                    self.total += int(sum)
                    break
        return self.total

    def two(self):
        """
        Doing some math!
        """
        # To safely use this attribute, we're going to reinitialize it to zero
        self.total = 0
        possible_ops = ['+', '*', "||"]
        self.input = self.input.split('\n')
        for line in self.input:
            sum,nums = line.split(':')
            nums = nums.split()
            count_perms = self.count_possible_permutations(nums, possible_ops)
            permutations = self.generate_possible_permutations(nums, possible_ops)
            for perm in permutations:
                line_total = 0
                for idx,op in enumerate(perm):
                    x = int(nums[idx])
                    y = int(nums[idx + 1])
                    if idx == 0:
                        line_total = self.do_math(x, y, op)
                    else:
                        line_total = self.do_math(line_total, y, op)
                if line_total == int(sum):
                    self.total += int(sum)
                    break
        return self.total


if __name__ == '__main__':
    print("[!] This is just a class definition!")
