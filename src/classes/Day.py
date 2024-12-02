class Day():
    def __init__(self, debug=False):
        self.debug = debug

    def read_input(self, input_file):
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
