"""61070023  Align"""
def main(size, pos, text):
    """
    This problem want you to print text with size in a true position <pos>
    _____________________________________________________________________
    WARNING !! This problem has Special case:

        In normal if you use text.center(size)
        and size-len(text) is a odd number
        Output will print space(" ") on right side more than left side
        but this problem want left side more than right side.
    _____________________________________________________________________

    """
    space = size - len(text)

    if pos == "left":
        print(text + " " * (space))

    elif pos == "center":
        if space % 2 == 0:
            print(text.center(size))
        else: #Special case
            print(" "+ text.center(size-1))
    else:
        print(" " * (space) + text)

main(int(input()), input(), input())
