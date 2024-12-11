"""
The main driver for AoC 2024. Run this from the src directory
"""

try:
    from classes.d_7 import D7
except ModuleNotFoundError:
    print("[!] Could not find modules!")

def main():
    """
    Generates a solution for a day's puzzles
    """
    d7 = D7("../input/d7ex.txt", debug=True)
    # print(d7.one())
    print(d7.two())

if __name__ == '__main__':
    main()
