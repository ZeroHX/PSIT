"""
Midterm Crisis: Triangle V2
Level: Hot-Headed
"""
def main(size):
    """
    This problem want you to draw Triangle pattern
    Ex: input = 5
            05
          04  04
        03      03
      02          02
    01              01
    """
    for i in range(size):
        print(" " * (((size-i)*2)-2), end="")
        if i == 0:
            print("%02d" %(size-i))
        else:
            print("%02d" % (size-i), end="")
            print(" " * ((4*i)-2), end="")
            print("%02d" % (size-i), end="")
            print()

main(int(input()))
