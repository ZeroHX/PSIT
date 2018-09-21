"""Seq5 40%"""
from math import ceil
def main(num):
    """main func"""
    line = ceil(num/7)
    for _ in range(line):
        for j in range(num, num-7, -1):
            if j < 1:
                break
            print(j, end=" ")
        print()
        num -= 7

main(int(input()))
