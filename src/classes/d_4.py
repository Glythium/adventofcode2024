"""
Class file containing the solution to Day Four's puzzles
"""
try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D4(Day):
    """
    Class containing the solution to Day 4
    """
    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.matrix = []
        self.create_matrix()
    
    def search(self, y, x, y_dir, x_dir, target):
        string = ""
        try:
            for i in range(len(target)):
                string += self.matrix[y][x]
                x += 1 * x_dir
                y += 1 * y_dir
            if self.debug:
                print(string)
            return string == target
        except IndexError:
            return False

    def one(self):
        """
        Finds every instance of 'XMAS' forwards, backwards, vertically, and
        diagonally in a matrix of input.
        """
        # To safely use this attribute, we're going to reinitialize it to zero
        self.total = 0

        # Iterate through each line in the matrix
        for idx_y,line in enumerate(self.matrix):
            # We're going to use idx_y for accessing other lines vertically.
            # Iterate through each character in the line from the anchoring 'X'
            for idx_x,letter in enumerate(line):
                # We're going to use idx_x for accessing other lines horizontally
                #   from the anchoring 'X'
                if letter == 'X':
                    if self.debug:
                        print(idx_y,idx_x)
                    # We have found an anchoring 'X'
                    # Now, we need to start reaching out from here to
                    #   find the rest of our 'MAS'

                    # Forward horizontal (+X , Y)
                    if self.search(idx_y, idx_x, 0, 1, "XMAS"):
                        self.total += 1
                        if self.debug:
                            print("FH")
                    
                    # Straight down vertically (X , +Y)
                    if self.search(idx_y, idx_x, 1, 0, "XMAS"):
                        self.total += 1
                        if self.debug:
                            print("SDV")
                    
                    # Forward down diagonally (+X , +Y)
                    if self.search(idx_y, idx_x, 1, 1, "XMAS"):
                        self.total += 1
                        if self.debug:
                            print("FDD")
                    
                    # For the reverse searches, we need to check to ensure
                    #   we don't attempt a negative index which will wrap
                    if idx_x - len("MAS") >= 0:
                        # Reverse horizontal (-X , Y)
                        if self.search(idx_y, idx_x, 0, -1, "XMAS"):
                            self.total += 1
                            if self.debug:
                                print("RH")
                        
                        try:
                            # Reverse down diagonally (-X , +Y)
                            if self.search(idx_y, idx_x, 1, -1, "XMAS"):
                                self.total += 1
                                if self.debug:
                                    print("RDD")
                        except IndexError:
                            pass
                    
                    if idx_y - len("MAS") >= 0:
                        # Reverse up vertically (X , -Y)
                        if self.search(idx_y, idx_x, -1, 0, "XMAS"):
                            self.total += 1
                            if self.debug:
                                print("RUV")

                        try:
                            # Forward up diagonally (+X , -Y)
                            if self.search(idx_y, idx_x, -1, 1, "XMAS"):
                                self.total += 1
                                if self.debug:
                                    print("FUD")
                        except IndexError:
                            pass
                    
                    if idx_x - len("MAS") >= 0 and idx_y - len("MAS") >= 0:
                        # Reverse up diagonally (-X , -Y)
                        if self.search(idx_y, idx_x, -1, -1, "XMAS"):
                            self.total += 1
                            if self.debug:
                                print("RUD")
        return self.total

    def two(self):
        """
        Pretty much same as above, but we're looking for a X-MAS
        """
        # To safely use this attribute, we're going to reinitialize it to zero
        self.total = 0

        # Iterate through each line in the matrix
        for idx_y,line in enumerate(self.matrix):
            # We're going to use idx_y for accessing other lines vertically.
            # Iterate through each character in the line from the anchoring 'X'
            for idx_x,letter in enumerate(line):
                # We're going to use idx_x for accessing other lines horizontally
                #   from the anchoring 'A'
                if letter == 'A':
                    if self.debug:
                        print(idx_y, idx_x)
                    if idx_y - 1 >= 0 and idx_x - 1 >= 0:
                        if self.search(idx_y - 1, idx_x - 1, 1, 1, "MAS"):
                            if self.search(idx_y - 1, idx_x + 1, 1, -1, "MAS"):
                                """
                                M   M
                                  A
                                S   S
                                """
                                self.total += 1
                                if self.debug:
                                    print("FDD -> RDD")
                                continue
                            if self.search(idx_y + 1, idx_x - 1, -1, 1, "MAS"):
                                """
                                M   S
                                  A
                                M   S
                                """
                                self.total += 1
                                if self.debug:
                                    print("FDD -> FUD")
                                continue
                    try:
                        if self.matrix[idx_y + 1][idx_x + 1] == "M":
                            if self.search(idx_y + 1, idx_x + 1, -1, -1, "MAS"):
                                if idx_x - 1 >= 0 and idx_y - 1 >= 0:
                                    if self.search(idx_y + 1, idx_x - 1, -1, 1, "MAS"):
                                        """
                                        S   S
                                          A
                                        M   M
                                        """
                                        self.total += 1
                                        if self.debug:
                                            print("RUD -> FUD")
                                        continue
                                    if self.search(idx_y - 1, idx_x + 1, 1, -1, "MAS"):
                                        """
                                        S   M
                                          A
                                        S   M
                                        """
                                        self.total += 1
                                        if self.debug:
                                            print("RUD -> RDD")
                    except IndexError:
                        pass
        return self.total


if __name__ == '__main__':
    print("[!] This is just a class definition!")
