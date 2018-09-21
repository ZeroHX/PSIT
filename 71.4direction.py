"""61070023  4-direction"""
def main(act):
    """
    print a Arrow on direction  <U:up D:down L:left R:right>

    """

    for _ in act:
        print("  *  ", end=" ")
    print()

    for line2 in act:
        if line2 == "U":
            print(" *** ", end=" ")
        elif line2 == "D":
            print("  *  ", end=" ")
        elif line2 == "L":
            print(" *   ", end=" ")
        elif line2 == "R":
            print("   * ", end=" ")
    print()

    for line3 in act:
        print("* * *" if line3 in "UD" else "*****", end=" ")
    print()

    for line4 in act:
        if line4 == "U":
            print("  *  ", end=" ")
        if line4 == "D":
            print(" *** ", end=" ")
        if line4 == "L":
            print(" *   ", end=" ")
        if line4 == "R":
            print("   * ", end=" ")
    print()

    for _ in act:
        print("  *  ", end=" ")
main(input())
