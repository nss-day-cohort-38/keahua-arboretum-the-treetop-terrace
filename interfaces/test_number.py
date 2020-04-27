def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        print ("Please enter a number...")
        input("\n\nPress any key to continue...")

def choice_in_range(s, length):
    try:
        # if int(s) < length + 1:
        #     return True
        # else:
        #     return False
        # return True
        int(s) < length +1
        return True

    except ValueError:
        print ("Please enter a valid choice...")

        input("\n\nPress any key to continue...")


def raise_val_error():
    try:
        int("yes")
        return True
    except ValueError:
        print ("Please enter a valid choice...")

        input("\n\nPress any key to continue...")