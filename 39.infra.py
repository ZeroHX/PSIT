"""Inflation"""
def main(money, year):
    """main func"""
    for _ in range(year):
        money += money*(3.81/100)

    ans = money*100//1/100
    print("%.2f" % ans)

main(float(input()), int(input()))
