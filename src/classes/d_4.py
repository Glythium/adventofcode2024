"""
Class file containing the solution to Day Four's puzzles
"""
import re
try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D4(Day):
    """
    Class containing the solution to Day 3
    """
    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.matrix = []
        self.target_word = "XMAS"
        self.create_matrix()

    def create_matrix(self):
        """
        Using splitlines() here creates a list of strings that we can start
        referencing using two references corresponding to X and Y coordinates 
        """
        self.matrix = self.input.splitlines()
    
    def forward_horizontal(self, y, x, target):
        string = ""
        try:
            for i in range(1, len(target) + 1):
                string += self.matrix[y][x + i]
            return string == target
        except IndexError:
            return False
    
    def down_vertically(self, y, x, target):
        string = ""
        try:
            for i in range(1, len(target) + 1):
                string += self.matrix[y + i][x]
            return string == target
        except IndexError:
            return False
    
    def forward_down_diagonally(self, y, x, target):
        string = ""
        try:
            for i in range(1, len(target) + 1):
                string += self.matrix[y + i][x + i]
            return string == target
        except IndexError:
            return False
    
    def reverse_horizontal(self, y, x, target):
        string = ""
        for i in range(1, len(target) + 1):
            string += self.matrix[y][x - i]
        return string == target

    def reverse_vertically(self, y, x, target):
        string = ""
        for i in range(1, len(target) + 1):
            string += self.matrix[y - i][x]
        return string == target
    
    def reverse_down_diagonally(self, y, x, target):
        string = ""
        try:
            for i in range(1, len(target) + 1):
                string += self.matrix[y + i][x - i]
            return string == target
        except IndexError:
            return False
    
    def forward_up_diagonally(self, y, x, target):
        string = ""
        try:
            for i in range(1, len(target) + 1):
                string += self.matrix[y - i][x + i]
            return string == target
        except IndexError:
            return False
    
    def reverse_up_diagonally(self, y, x, target):
        string = ""
        for i in range(1, len(target) + 1):
            string += self.matrix[y - i][x - i]
        return string == target

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
                    if self.forward_horizontal(idx_y, idx_x, "MAS"):
                        self.total += 1
                        if self.debug:
                            print("FH")
                    
                    # Straight down vertically (X , +Y)
                    if self.down_vertically(idx_y, idx_x, "MAS"):
                        self.total += 1
                        if self.debug:
                            print("SDV")
                    
                    # Forward down diagonally (+X , +Y)
                    if self.forward_down_diagonally(idx_y, idx_x, "MAS"):
                        self.total += 1
                        if self.debug:
                            print("FDD")
                    
                    # For the reverse searches, we need to check to ensure
                    #   we don't attempt a negative index which will wrap
                    if idx_x - len("MAS") >= 0:
                        # Reverse horizontal (-X , Y)
                        if self.reverse_horizontal(idx_y, idx_x, "MAS"):
                            self.total += 1
                            if self.debug:
                                print("RH")
                        
                        try:
                            # Reverse down diagonally (-X , +Y)
                            if self.reverse_down_diagonally(idx_y, idx_x, "MAS"):
                                self.total += 1
                                if self.debug:
                                    print("RDD")
                        except IndexError:
                            pass
                    
                    if idx_y - len("MAS") >= 0:
                        # Reverse up vertically (X , -Y)
                        if self.reverse_vertically(idx_y, idx_x, "MAS"):
                            self.total += 1
                            if self.debug:
                                print("RUV")

                        try:
                            # Forward up diagonally (+X , -Y)
                            if self.forward_up_diagonally(idx_y, idx_x, "MAS"):
                                self.total += 1
                                if self.debug:
                                    print("FUD")
                        except IndexError:
                            pass
                    
                    if idx_x - len("MAS") >= 0 and idx_y - len("MAS") >= 0:
                        # Reverse up diagonally (-X , -Y)
                        if self.reverse_up_diagonally(idx_y, idx_x, "MAS"):
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
                        if self.forward_down_diagonally(idx_y - 2, idx_x - 2, "MAS"):
                            if self.reverse_down_diagonally(idx_y - 2, idx_x + 2, "MAS"):
                                """
                                M   M
                                  A
                                S   S
                                """
                                self.total += 1
                                if self.debug:
                                    print("FDD -> RDD")
                            if self.forward_up_diagonally(idx_y + 2, idx_x - 2, "MAS"):
                                """
                                M   S
                                  A
                                M   S
                                """
                                self.total += 1
                                if self.debug:
                                    print("FDD -> FUD")
                    try:
                        if self.matrix[idx_y + 1][idx_x + 1] == "M":
                            if self.reverse_up_diagonally(idx_y + 2, idx_x + 2, "MAS"):
                                if idx_x - 1 >= 0:
                                    if self.forward_up_diagonally(idx_y + 2, idx_x - 2, "MAS"):
                                        """
                                        S   S
                                          A
                                        M   M
                                        """
                                        self.total += 1
                                        if self.debug:
                                            print("RUD -> FUD")
                                if idx_y - 1 >= 0:
                                    if self.reverse_down_diagonally(idx_y - 2, idx_x + 2, "MAS"):
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
