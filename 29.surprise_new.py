"""Surprise NEW"""
def main(total, num):
    """main func"""
    num1 = total-(num*2)
    if num1 < 0:
        num1 = 0
    if num-(num1) > 2:
        print("Surprising")
    else:
        print("Not surprising")

main(float(input()), float(input()))
