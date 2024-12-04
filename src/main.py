"""
The main driver for AoC 2024. Run this from the src directory
"""

try:
    from classes.d_4 import D4
except ModuleNotFoundError:
    print("[!] Could not find modules!")

def main():
    """
    Generates a solution for a day's puzzles
    """
    d4 = D4("../input/d4.txt", debug=False)
    print(d4.one())
    print(d4.two())


if __name__ == '__main__':
    main()
