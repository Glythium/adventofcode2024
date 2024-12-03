"""
The main driver for AoC 2024. Run this from the src directory
"""

try:
    from classes.d_2 import D2
except ModuleNotFoundError:
    print("[!] Could not find modules!")

def main():
    """
    Generates a solution for a day's puzzles
    """
    d2 = D2(1, 3, debug=True)
    print(d2.solve("../input/d2.txt"))
    print(d2.solve("../input/d2.txt", should_dampen=True))


if __name__ == '__main__':
    main()
