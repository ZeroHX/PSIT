"""boomerang"""
from math import sqrt
def main():
    """main func"""
    numx = int(input())
    numy = int(input())
    numz = int(input())

    print(calc1(numx))
    print(calc2(numy))
    print(calc3(numz))
    print(calc4(numx, numy))
    print(calc5(numx, numy, numz))

def calc1(num):
    """calculate 1"""
    num += 1
    return num

def calc2(num):
    """calculate 2"""
    result = (7*(num**3))+(2*(num**2))-(31*num)+1
    return result

def calc3(num):
    """calculate2"""
    return -num

def calc4(num1, num2):
    """calculate4"""
    result = (num1+num2)*(num1-num2)
    return result


def calc5(num1, num2, num3):
    """calculate5"""
    result = (num2-sqrt((num2**2)-(4*num1*num3)))/(2*num1)
    return result

main()
