"""gradeIII"""
def main():
    """main func"""
    stop = int(input())
    result = 0
    for _ in range(stop):
        num = calc(float(input()))
        result += num

    #NormalAverage
    total = result/stop

    #Calculate SP case
    total1 = total * 1000           #EX_total:3.656 => 3656.0
    last = total1 % 10              #LastDigit:6
    total2 = (total1 - last)/1000   #3656-6 = 3650  => 3.650

    if last <= 5:                   #Normal
        print("%.2f" % total)
    elif last > 5 and last <= 9:    #Special
        print("%.2f" % total2)


def calc(num):
    """calculte here!!"""
    result = 0
    if num >= 0 and num < 60:
        result += 0
    elif num >= 60 and num < 65:
        result += 0.5
    elif num >= 65 and num < 70:
        result += 1
    elif num >= 70 and num < 75:
        result += 1.5
    elif num >= 75 and num < 80:
        result += 2
    elif num >= 80 and num < 85:
        result += 2.5
    elif num >= 85 and num < 90:
        result += 3
    elif num >= 90 and num < 95:
        result += 3.5
    elif num >= 95 and num < 100:
        result += 4

    #RETURN GRADE(EX3.5)
    return result


main()
