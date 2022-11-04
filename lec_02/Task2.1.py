import sys

args = sys.argv

def check_str(index): # check str first or flow into other check will ereor
    if len(args[index]) > 1: # exlcude the case only pass '-'
        if args[index][0] == '-':
            temp = args[index][1:]
            for i in range(len(temp)):
                if (ord(temp[i]) > 57) or (ord(temp[i]) < 48):
                    return True
    else:
        for i in range(len(args[index])):
            if (ord(args[index][i]) > 57) or (ord(args[index][i]) < 48):
                return True

def Task2_1(args):
    if check_str(1):
        print(False, 1)
        return
    if check_str(2):
        print(False, 2)
        return
    if check_str(3):
        print(False, 3)
        return
    if len(args) != 4:
        print(False)
    elif (args[1] == args[2] == args[3]):
        print(True)
    else:
        print(False, 4)

Task2_1(args)