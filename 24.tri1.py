"""Tri1"""
def main():
    """main func"""
    num1, num2, num3 = float(input()), float(input()), float(input())
    num_a = calc1(num1, num2, num3)
    num_b = calc2(num1, num2, num3)
    num_c = calc3(num1, num2, num3)

    if abs((num_a**2) - (num_b**2+num_c**2)) <= 0.01:
        print("Yes")
    else:
        print("No")

def calc1(num_x, num_y, num_z):
    """calculate max!!"""
    if num_x > num_y and num_x > num_z:
        return num_x
    elif num_y > num_x and num_y > num_z:
        return num_y
    else:
        return num_z

def calc2(num_x, num_y, num_z):
    """calculate mid!!"""
    if (num_x > num_y and num_x < num_z) or (num_x > num_z and num_x < num_y):
        return num_x
    elif (num_y > num_x and num_y < num_z) or (num_y > num_z and num_y < num_x):
        return num_y
    else:
        return num_z

def calc3(num_x, num_y, num_z):
    """calculate min!!"""
    if num_x < num_y and num_x < num_z:
        return num_x
    elif num_y < num_x and num_y < num_z:
        return num_y
    else:
        return num_z


main()
