#!/u7sr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i is not x:
            print("{:d}".format(my_list[i]), end="")
            i += 1
    except IndexError:
        print("", end="")
    print("")
    return i
