"""61070023 Bill"""
def main(cost):
    """main func"""
    ser = cost*0.1
    if ser < 50:
        ser = 50
    elif ser > 1000:
        ser = 1000
    vat = (ser + cost) * 0.07

    total = ser+vat+cost

    print("%.2f" % (total))
main(int(input()))
