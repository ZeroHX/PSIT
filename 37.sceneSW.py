"""SceneSwitch I"""
def main():
    """main func"""
    result = 0

    while 1:
        num1 = check(input())
        num2 = check(input())
        num3 = check(input())
        num4 = check(input())
        if num3 - num1 <= 6:
            result += 1
        if num1 == "End" or num2 == "End" or num3 == "End" or num4 == "End":
            break

    print(result)
def check(f_s):
    """check float or string"""
    if f_s.isdigit() == 1:
        return float(f_s)
    else:
        return f_s

main()
