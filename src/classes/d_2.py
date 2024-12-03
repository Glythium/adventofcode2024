"""
Class file containing the solution to Day Two's puzzles
"""

try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D2(Day):
    """
    Class containing the solution to Day 2
    """
    def __init__(self, min_jump, max_jump, debug=False):
        super().__init__(debug=debug)
        self.sequences = []
        self.min_jump = min_jump
        self.max_jump = max_jump
        self.is_increasing = True
        self.is_decreasing = False
    
    def _set_flags(self, first, second):
        if first < second:
            # This sequence must be increasing
            self.is_increasing = True
            self.is_decreasing = False
        else:
            # This sequence must be decreasing
            self.is_increasing = False
            self.is_decreasing = True
    
    def is_following_pattern(self, sequence, should_dampen=False):
        self._set_flags(int(sequence[0]), int(sequence[1]))
        for idx in range(len(sequence)):
            if idx + 1 == len(sequence):
                # Here's a matching pattern of numbers
                return True

            first = int(sequence[idx])
            second = int(sequence[idx + 1])

            if first == second:
                # Any time we find a match, just break out
                break
            elif first > second:
                # The first number is bigger, so we're decrementing
                self.is_decreasing = True
            elif first < second:
                # The first number is smaller, so we're incrementing
                self.is_increasing = True

            if self.is_increasing and self.is_decreasing:
                # At some point it went up and down, this is not a match
                break

            jump = abs(first - second)
            if jump < self.min_jump or jump > self.max_jump:
                # This is too far of a jump between the numbers
                break

        if should_dampen:
            # Brute force by trying to remove each number
            for idx in range(len(sequence)):
                num = sequence.pop(idx)
                if self.is_following_pattern(sequence):
                    return True
                sequence.insert(idx, num)
        return False

    def solve(self, input_file, should_dampen=False):
        """
        Checks a sequence of numbers for a pattern that slightly increments or
        decrements by a min_jump and max_jump parameter

        Returns the total number of sequences that follows that pattern
        """
        self.total = 0
        self.sequences = self.read_input(input_file)
        for s in self.sequences:
            seq = s.strip().split()
            if self.is_following_pattern(seq, should_dampen=should_dampen):
                self.total += 1
        return self.total


if __name__ == '__main__':
    print("[!] This is just a class definition!")
