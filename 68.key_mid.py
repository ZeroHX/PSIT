"""61070023  Key_midterm"""
def main(id_num, result1):
    """
    This problem want to know that ID_number on the condition
    1_sum of all
    2_ 3 final ID_number * 10
    Ans is 1+2 and if > 10000: print only 4 final num and if < 1000: +1000
    """

    #Con1
    for i in id_num:
        result1 += int(i)

    #Con2
    result2 = int(id_num[-3:])*10

    #Sum of Con1 & Con2
    total = result1 + result2

    if total >= 10000:
        total = str(total)
        print(total[-4:])
    elif total < 1000:
        print(total+1000)
    else:
        print(total)
main(input(), 0)
