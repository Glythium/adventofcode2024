"""
File containing the abstract base class for each Day
"""

class Day():
    """
    Abstract base class for each Day's solutions
    """
    def __init__(self, input_file, debug=False):
        self.debug = debug
        self.total = 0
        self.input = self.read_input(input_file)

    def read_input(self, input_file):
        """
        Reads in text in a given input file, returns the input as a string
        """
        try:
            with open(input_file, "r", encoding="utf-8") as fp:
                return fp.read()
        except FileNotFoundError:
            if self.debug:
                print(f"[!] FileNotFound '{input_file}")
            return None

    def create_matrix(self):
        """
        Using splitlines() here creates a list of strings that we can start
        referencing using two references corresponding to X and Y coordinates 
        """
        self.matrix = self.input.splitlines()

    def one(self):
        """
        Override this in your child class
        """

    def two(self):
        """
        Override this in your child class
        """


if __name__ == '__main__':
    print("[!] This is just the abstract base class!")
