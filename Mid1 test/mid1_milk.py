"""
Midterm Crisis: Milk
Level: Hell
"""
def main(cost, buy, bonus, money):
    """
    This problem is the same as donut but change
    amount of need(i4) >> money that you have

    Alert! Alert1! Alert! When you buy a milk, it will continous calc that cover!
    and this problem have a very confuse testcase!!

    """
    amount = money//cost    #Find a lowest amount that possible
    cov = amount
    if buy != 0:
        while cov >= buy:
            amount += bonus
            cov -= buy
            cov += bonus

    print(amount)


main(int(input()), int(input()), int(input()), int(input()))
