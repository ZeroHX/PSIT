"""For!F-Ball"""
def main(act, pos):
    """
    3 Cup Miracle
    There have 3 action
    _____      _____      _____
    |   |      |   |      |   |
    | O |      |   |      |   |

    1            2           3

    ---Input----------------
    ActA: 1>>2 or 2>>1
    ActB: 2>>3 or 3>>2
    ActC: 1>>3 or 3>>1

    Question: Finally, where is a ball (1,2,3)

    """
    for i in act:
        #Position1
        if i == "A" and pos == 1:
            pos = 2
            continue
        if i == "C" and pos == 1:
            pos = 3
            continue

        #Position2
        if i == "A" and pos == 2:
            pos = 1
            continue
        if i == "B" and pos == 2:
            pos = 3
            continue

        #Position3
        if i == "B" and pos == 3:
            pos = 2
            continue
        if i == "C" and pos == 3:
            pos = 1
            continue

    print(pos)


main(input(), 1)
