"""
Class file containing the solution to Day Five's puzzles
"""
try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D6(Day):
    """
    Class containing the solution to Day 5
    """
    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.heading = {
            "^": "North",
            ">": "East",
            "v": "South",
            "<": "West"
        }

    def change_heading(self, heading):
        """
        Takes in a given character representing a guard (ex: ^><v) and
        changes their heading by 90 degrees to the right
        """
        heading_change = {
            "North": ">",
            "East": "v",
            "South": "<",
            "West": "^"
        }
        current_direction = self.heading[heading]
        return heading_change[current_direction]

    def plot_step(self, current_point, heading):
        """
        Plans the guard's next step
        """
        next_distance = {
            "North": [-1, 0],
            "East": [0, 1],
            "South": [1, 0],
            "West": [0, -1]
        }
        planned_point = next_distance[self.heading[heading]]
        planned_point[0] += current_point[0]
        planned_point[1] += current_point[1]
        return planned_point

    def draw_matrix(self):
        if self.debug:
            for line in self.matrix:
                print(line)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def redraw_line(self, line, new_chr, new_chr_idx):
        updated_line = ""
        for idx,chr in enumerate(line):
            if idx == new_chr_idx:
                updated_line += new_chr
            else:
                updated_line += chr
        return updated_line

    def one(self):
        """
        Pathfinding!
        """
        # To safely use this attribute, we're going to reinitialize it to zero
        self.total = 0
        self.create_matrix()
        current_point = []
        max_y = len(self.matrix)
        max_x = len(self.matrix[0])
        cur_heading = ""

        # Find our starting point grid coordinate
        for idx_y,line in enumerate(self.matrix):
            for idx_x,chr in enumerate(line):
                if chr in "^>v<":
                    current_point = [idx_y, idx_x]
                    cur_heading = chr
        if self.debug:
            print(f"current_point = {current_point}")

        # Stepping loop
        while 0 <= current_point[0] < max_y and 0 <= current_point[1] < max_x:
            # Look ahead to our next location
            planned_point = self.plot_step(current_point, cur_heading)
            new_y = planned_point[0]
            new_x = planned_point[1]
            been_visited = False
            try:
                next_chr = self.matrix[new_y][new_x]
            except IndexError:
                next_chr = "."

            if next_chr == "X":
                been_visited = True

            # If the next point is a blocker
            if next_chr == "#":
                # Just change heading this round
                cur_heading = self.change_heading(cur_heading)
            else:
                # Now, we're moving
                self.matrix[current_point[0]] = self.redraw_line(self.matrix[current_point[0]], "X", current_point[1])
                try:
                    # This is wrapped in a try/catch so we don't try to write a line OOB
                    self.matrix[new_y] = self.redraw_line(self.matrix[new_y], cur_heading, new_x)
                except IndexError:
                    pass
                # Increment our point so we can break this while loop naturally
                current_point = planned_point
                if not been_visited:
                    self.total += 1
                self.draw_matrix()
                if self.debug:
                    print(self.total)

        if self.debug:
            # Just counting the X chars gives the right answer for the example (41)
            just_xs = 0
            for line in self.matrix:
                just_xs += line.count("X")
            print(f"justxs = {just_xs}")

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
