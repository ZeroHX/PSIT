"""61070023  Donut"""
from math import ceil
def main(cost, donut, bonus, need):
    """MAIN FUNC"""
    pack = donut+bonus
    pay, get = 0, 0
    while need >= pack:
        get += pack
        pay += cost*donut
        need -= pack
    if need < donut:
        get += need
        pay += need*cost

    elif need >= donut:
        get += pack
        pay += donut*cost

    print("%d %d" % (pay, get))

main(int(input()), int(input()), int(input()), int(input()))