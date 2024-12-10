"""
The main driver for AoC 2024. Run this from the src directory
"""

try:
    from classes.d_6 import D6
except ModuleNotFoundError:
    print("[!] Could not find modules!")

def main():
    """
    Generates a solution for a day's puzzles
    """
    d6 = D6("../input/d6.txt", debug=True)
    print(d6.one())
    # print(d5.two())

if __name__ == '__main__':
    main()
