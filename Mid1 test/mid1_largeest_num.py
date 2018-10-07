"""
Midterm crisis: Largest Number
Level: WTF I'm doing
"""
def main(num1, num2, num3):
    """
    This problem want you to find a largest number with 3 input

    ALERT!! This is not a arrange input
    """
    num123, num132, num213, num231, num312, num321 = int(num1+num2+num3), int(num1+num3+num2)\
    , int(num2+num1+num3), int(num2+num3+num1), int(num3+num1+num2), int(num3+num2+num1)

    #Just brute force
    if num123 >= num132 and num123 >= num213 and num123 >= num231 and num123 >= num312 \
    and num123 >= num321:
        print(num123)

    elif num132 >= num123 and num132 >= num213 and num132 >= num231 and num132 >= num312 \
    and num132 >= num321:
        print(num132)

    elif num213 >= num132 and num213 >= num123 and num213 >= num231 and num213 >= num312 \
    and num213 >= num321:
        print(num213)

    elif num231 >= num132 and num231 >= num213 and num231 >= num123 and num231 >= num312 \
    and num231 >= num321:
        print(num231)

    elif num312 >= num132 and num312 >= num213 and num312 >= num231 and num312 >= num123 \
    and num312 >= num321:
        print(num312)

    else:
        print(num321)

main(input(), input(), input())

