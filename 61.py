"""Indicator_Right"""
def main(width, height):
    """MAIN FUNC"""
    for i in range(-(height//2), (height//2)+1):
        print(" "* (abs(abs(i)-(height//2))), end="")
        print("*" * width)
main(int(input()), int(input()))
