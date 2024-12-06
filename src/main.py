"""
The main driver for AoC 2024. Run this from the src directory
"""

try:
    from classes.d_5 import D5
except ModuleNotFoundError:
    print("[!] Could not find modules!")

def main():
    """
    Generates a solution for a day's puzzles
    """
    d5 = D5("../input/d5.txt", debug=False)
    print(d5.one())
    print(d5.two())


if __name__ == '__main__':
    main()
