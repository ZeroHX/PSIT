"""circular I"""
def main(mex, mey, rad, mosx, mosy):
    """main func"""
    dis = ((mex-mosx)**2 + (mey-mosy)**2)**0.5
    if rad >= dis:
        print("Yes")
    else:
        print("No")

main(float(input()), float(input()), float(input()), float(input()), float(input()), )
