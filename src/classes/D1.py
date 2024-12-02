from .Day import Day
from helpers.unzip import unzip

class D1(Day):
    def __init__(self, debug=False):
        super().__init__(debug=debug)

    def one(self, input_file):
        self.input_one = self.read_input(input_file)
        if self.input_one is None:
            if self.debug:
                print("[!] Exiting...")
            return None
        list1, list2 = unzip(self.input_one)
        if self.debug:
            print(f"[*] L1 = '{list1[0:3]}'...L2 = '{list2[0:3]}'...")



if __name__ == '__main__':
    print("[!] This is just a class definition!")
