"""
The main driver for AoC 2024. Run this from the src directory
"""

try:
    from classes.d_1 import D1
except ModuleNotFoundError:
    print("[!] Could not find modules!")

def main():
    """
    Generates a solution for a day's puzzles
    """
    print("[*] Beginning...")
    d1 = D1(debug=True)
    print(d1.one("../input/d1.txt"))
    print(d1.two("../input/d1.txt"))


if __name__ == '__main__':
    main()
