"""weightstation"""
def main():
    """main func"""
    avg = float(input())
    wei_1, wei_2, wei_3 = float(input()), float(input()), float(input())
    wei_4 = (avg*4)-(wei_1+wei_2+wei_3)
    weight = wei_1+wei_2+wei_3+wei_4

    if weight >= 15000:
        print("Overweight")

    elif (avg - wei_1) >= avg/2:
        print("Unbalance")

    elif (avg - wei_2) >= avg/2:
        print("Unbalance")

    elif (avg - wei_3) >= avg/2:
        print("Unbalance")

    elif (avg - wei_4) >= avg/2:
        print("Unbalance")

    else:
        print("Pass %.2f" % wei_4)

main()
