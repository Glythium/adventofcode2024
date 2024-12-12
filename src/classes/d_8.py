"""
Class file containing the solution to Day Five's puzzles
"""
try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D8(Day):
    """
    Class containing the solution to Day 8
    """
    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
    
    def map_antenna(self):
        antenna_coords = dict()
        for idx_y,line in enumerate(self.matrix):
            for idx_x,chr in enumerate(line):
                if chr != '.':
                    if chr not in antenna_coords.keys():
                        antenna_coords[chr] = list()
                    antenna_coords[chr].append((idx_y, idx_x))
        return antenna_coords

    def map_antinodes(self, antenna_coords):
        max_y = len(self.matrix)
        max_x = len(self.matrix[0])
        antinodes = set()
        for key in antenna_coords.keys():
            for idx,antenna in enumerate(antenna_coords[key]):
                y1, x1 = antenna
                if idx + 1 < len(antenna_coords[key]):
                    for j in antenna_coords[key][idx + 1:]:
                        if self.debug:
                            print(f"{key}: {antenna} | {j}")
                        y2, x2 = j
                        dist_y = abs(y1 - y2)
                        dist_x = abs(x1 - x2)
                        lower_y = y1 - dist_y
                        lower_x = x1 + dist_x
                        upper_y = y2 + dist_y
                        upper_x = x2 - dist_x
                        if lower_y >= 0 and lower_x < max_x:
                            antinodes.add((lower_y, lower_x))
                        if upper_y < max_y and upper_x >= 0:
                            antinodes.add((upper_y, upper_x))
                        if self.debug:
                            print(f"|__({lower_y},{lower_x}) .. ({upper_y}, {upper_x})\n")
        return antinodes
    
    def deconflict_antinodes(self, antinodes):
        deconflicted_antinodes = set()
        for antinode in antinodes:
            an_y, an_x = antinode
            if self.matrix[an_y][an_x] == '.':
                deconflicted_antinodes.add(antinode)
        return deconflicted_antinodes
 
    def one(self):
        """
        Setting up antinodes
        """
        # To safely use this attribute, we're going to reinitialize it to zero
        self.total = 0
        self.create_matrix()
        antenna_coords = self.map_antenna()
        if self.debug:
            print(f"antenna coords = {antenna_coords}")
        antinodes = self.map_antinodes(antenna_coords)
        deconflicted_antinodes = self.deconflict_antinodes(antinodes)
        if self.debug:
            print(f"antinodes = {deconflicted_antinodes}")
        self.total = len(deconflicted_antinodes)
        # TODO: answer too high (248)
        return self.total

    def two(self):
        """
        TBD
        """
        return self.total


if __name__ == '__main__':
    print("[!] This is just a class definition!")
