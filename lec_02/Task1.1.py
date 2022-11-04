import sys

args = sys.argv

def Task1_1(args):
    if len(args) != 3:
        print(False)
    elif (len(args[1]) > 1) or (len(args[2]) > 1):
        print(False)
    elif (ord(args[1]) > 57) or (ord(args[2]) > 57) or (ord(args[1]) < 48) or (ord(args[2]) < 48): # ascii table
        print(False)
    elif (int(args[1]) % int(args[2]) == 0) or (int(args[2]) % int(args[1]) == 0):
        print(True)
    else:
        print(False)

Task1_1(args)