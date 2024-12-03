"""
The main driver for AoC 2024. Run this from the src directory
"""

try:
    from classes.d_3 import D3
except ModuleNotFoundError:
    print("[!] Could not find modules!")

def main():
    """
    Generates a solution for a day's puzzles
    """
    d3 = D3(debug=False)
    print(d3.solve("../input/d3.txt"))
    print(d3.solve("../input/d3.txt"))


if __name__ == '__main__':
    main()
