"""
File containing the abstract base class for each Day
"""

class Day():
    """
    Abstract base class for each Day's solutions
    """
    def __init__(self, debug=False):
        self.debug = debug

    def read_input(self, input_file):
        """
        Reads in text in a given input file, returns the input as a list of strings
        """
        try:
            with open(input_file, "r", encoding="utf-8") as fp:
                return fp.readlines()
        except FileNotFoundError:
            if self.debug:
                print(f"[!] FileNotFound '{input_file}")
            return None

    def one(self, input_file):
        """
        Override this in your child class
        """

    def two(self, input_file):
        """
        Override this in your child class
        """


if __name__ == '__main__':
    print("[!] This is just the abstract base class!")
