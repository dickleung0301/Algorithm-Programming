import sys

args = sys.argv

def Task1(args):
    if len(args) != 3:
        print(False)
    elif (len(args[1]) > 1) or (len(args[2]) > 1):
        print(False)
    elif (int(args[1]) > 9) or (int(args[2]) > 9): # ascii table
        print(False)
    elif (int(args[1]) % int(args[2]) == 0) or (int(args[2]) % int(args[1]) == 0):
        print(True)

Task1(args)