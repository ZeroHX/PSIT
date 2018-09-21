"""61070023 OddEven"""
def main():
    """main func"""
    even, odd = 0, 0
    while 1:
        num = int(input())
        if num == 0:
            break
        elif num % 2 == 0:
            even += num
        else:
            odd += num
    if even > odd:
        print("Even %d" % even)
    elif odd > even:
        print("Odd %d" % odd)
    else:
        print("Draw %d" % even)

main()
