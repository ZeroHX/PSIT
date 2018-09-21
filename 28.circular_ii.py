"""circular II"""
def main():
    """main func"""
    mex, mey, mer, frx, fry, frr = float(input()), float(input()), float(input()), \
    float(input()), float(input()), float(input())
    dis = ((mex-frx)**2 + (mey-fry)**2)**0.5
    if dis-(mer+frr) < 0:
        print("Yes")
    else:
        print("No")

main()
