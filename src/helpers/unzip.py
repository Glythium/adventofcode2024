"""
Unzips a list
"""

def unzip(zipped_list):
    """
    Splits the first two items in a list into their own lists
    """
    list1 = []
    list2 = []

    for i in zipped_list:
        items = i.split()
        list1.append(items[0])
        list2.append(items[1])

    return list1, list2


if __name__ == '__main__':
    print("[!] This library should not be called directly!")
