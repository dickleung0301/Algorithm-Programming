import sys

args = sys.argv

def Task1_2(args):
    for i in range(len(args[1])):
        if (ord(args[1][i]) > 57) or (ord(args[1][i]) < 48): # check str first or flow into other check will ereor
            print(False)
            return
    for i in range(len(args[2])):
        if (ord(args[2][i]) > 57) or (ord(args[2][i]) < 48): # check str first or flow into other check will ereor
            print(False)
            return
    for i in range(len(args[3])):
        if (ord(args[3][i]) > 57) or (ord(args[3][i]) < 48): # check str first or flow into other check will ereor
            print(False)
            return
    if len(args) != 4:
        print(False)
    elif (int(args[3]) >= (int(args[1]) + int(args[2]))) or (int(args[1]) >= (int(args[2]) + int(args[3]))) or (int(args[2]) >= (int(args[1]) + int(args[3]))):
        print(True)
    else:
        print(False)

Task1_2(args)