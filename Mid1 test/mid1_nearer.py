"""
Midterm Crisis: Nearer
Level: Free score
"""
def main(alice, bob, ice):
    """
    This problem want you to find a distance from ice-cream bus <ice>
    to a person <bob/alice> who has a shortest distance

    Alert!! Distance can be only Integer+
    """

    if abs(bob-ice) > abs(alice-ice):
        print("Alice %d" % (abs(alice-ice)))
    elif abs(bob-ice) < abs(alice-ice):
        print("Bob %d" % (abs(bob-ice)))
    else:
        print("Sundaes %d" %(abs(bob-ice)))

main(int(input()), int(input()), int(input()))
