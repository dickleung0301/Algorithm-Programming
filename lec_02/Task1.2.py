import sys

args = sys.argv

def Task1_2(args):
    if len(args) != 4:
        print(False)
    elif (len(args[1]) > 1) or (len(args[2]) > 1) or len(args[2]) > 1: # check str first or flow into other check will ereor
        print(False)
    elif (ord(args[1]) > 57) or (ord(args[2]) > 57) or (ord(args[3]) > 57) or (ord(args[1]) < 48) or (ord(args[2]) < 48) or (ord(args[3]) < 48): # ascii table
        print(False)
    elif (int(args[3]) >= (int(args[1]) + int(args[2]))) or (int(args[1]) >= (int(args[2]) + int(args[3]))) or (int(args[2]) >= (int(args[1]) + int(args[3]))):
        print(True)
    else:
        print(False)

Task1_2(args)