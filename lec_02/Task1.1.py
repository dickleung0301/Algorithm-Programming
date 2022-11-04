import sys

args = sys.argv

def check_str(index): # check str first or flow into other check will ereor
    for i in range(len(args[index])):
        if (ord(args[index][i]) > 57) or (ord(args[index][i]) < 48):
            return True

def Task1_1(args):
    if check_str(1):
        print(False)
        return
    if check_str(2):
        print(False)
        return
    if len(args) != 3:
        print(False)
    elif (int(args[1]) % int(args[2]) == 0) or (int(args[2]) % int(args[1]) == 0):
        print(True)
    else:
        print(False)

Task1_1(args)