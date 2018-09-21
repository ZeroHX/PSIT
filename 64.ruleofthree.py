"""61070023 Ruleofthree"""
def main(num, bcost, bsize, bratio):
    """This problem want to know, what is the best price with the biggest size"""
    for _ in range(num):
        cost = float(input())
        size = float(input())
        ratio = size/cost
        if ratio >= bratio:
            bratio = ratio
            bcost = cost
            bsize = size
    print("%.2f %.2f" % (bcost, bsize))

main(int(input()), 0, 0, 0)
