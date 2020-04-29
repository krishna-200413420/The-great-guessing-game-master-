"""
Created on May 20,2019


This file read all the letters from txt file and stored in list data structure
"""

list = []
class stringDatabase:
    """
    class stringDatabase contains method for I/O operations
    """
    def IOop(self):
        """
        This method will be responsible for all disk I/O
        """
        with open("four_letters.txt", "r") as fd:
            f = fd.read().splitlines()  # read line from txt file
            for line in f:
                list2 = line.split(" ")  # split line
                for word in list2:
                    list.append(word)  # store words in list data structure
