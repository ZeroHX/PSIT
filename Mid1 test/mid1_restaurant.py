"""
Midterm Crisis: Restaurant
"""
def main(cost, pro, dis, sug):
    """Calculate best price"""
    if cost == pro:
        ncost = cost-(cost * dis/100)
    else:
        ncost = cost

    if (cost + sug) *(1-(dis/100)) > ncost:
        print("No %.3f" % ((cost + sug) *(1-(dis/100)) - ncost))
    elif (cost + sug) *(1-(dis/100)) == ncost:
        print("Yes")
    else:
        print("Yes %.3f" % (ncost - (cost + sug) *(1-(dis/100))))
main(float(input()), float(input()), float(input()), float(input()))
