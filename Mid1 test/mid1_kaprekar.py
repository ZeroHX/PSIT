"""
Midterm crisis: Kaprekar's Constant <6174>
"""
def main(num):
    """Count until num == 6147"""

    count = 0
    while num != "6174":
        num0, num1, num2, num3 = num[0], num[1], num[2], num[3]

        num0, num1 = num0 if num0 < num1 else num1, num1 if num0 < num1 else num0
        num0, num2 = num0 if num0 < num2 else num2, num2 if num0 < num2 else num0
        num0, num3 = num0 if num0 < num3 else num3, num3 if num0 < num3 else num0
        num1, num2 = num1 if num1 < num2 else num2, num2 if num1 < num2 else num1
        num1, num3 = num1 if num1 < num3 else num3, num3 if num1 < num3 else num1
        num2, num3 = num2 if num2 < num3 else num3, num3 if num2 < num3 else num2

        low = num0+num1+num2+num3
        high = num3+num2+num1+num0

        num = str(int(high)-int(low))
        num = "%04d" % (int(num))
        count += 1

    print(count)

main(input())
