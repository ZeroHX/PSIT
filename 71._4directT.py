"""61070023  4_direction Newver by T"""
def main(act):
    """
    print a Arrow on direction  <U:up D:down L:left R:right>

    """
    #Point this problem are the loop that run a direction arrow in each row.
    for i in act:
        text = i
        line1 = text.replace("U", "  *  ").replace("D", "  *  ").replace("L", "  *  ")\
        .replace("R", "  *  ")
        print(line1, end=" ")
    print()

    for i in act:
        text = i
        line2 = text.replace("U", " *** ").replace("D", "  *  ").replace("L", " *   ")\
        .replace("R", "   * ")
        print(line2, end=" ")
    print()

    for i in act:
        text = i
        line3 = text.replace("U", "* * *").replace("D", "* * *").replace("L", "*****")\
        .replace("R", "*****")
        print(line3, end=" ")
    print()

    for i in act:
        text = i
        line4 = text.replace("U", "  *  ").replace("D", " *** ").replace("L", " *   ")\
        .replace("R", "   * ")
        print(line4, end=" ")
    print()

    for i in act:
        text = i
        line5 = text.replace("U", "  *  ").replace("D", "  *  ").replace("L", "  *  ")\
        .replace("R", "  *  ")
        print(line5, end=" ")
    print()


main(input())
