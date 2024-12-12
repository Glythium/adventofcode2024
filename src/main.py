"""
The main driver for AoC 2024. Run this from the src directory
"""

try:
    from classes.d_8 import D8
except ModuleNotFoundError:
    print("[!] Could not find modules!")

def main():
    """
    Generates a solution for a day's puzzles
    """
    d8 = D8("../input/d8.txt", debug=True)
    print(d8.one())
    # print(d8.two())

if __name__ == '__main__':
    main()
