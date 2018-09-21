"""chicken dinner"""
def main():
    """main func"""
    result = 0
    result += calc()
    result += calc()
    result += calc()
    result += calc()
    result += calc()
    result += calc()
    print(result)

def calc():
    """calculate"""
    count = 0
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())

    if num_a >= 50 and num_a <= 70:
        count += 1
    if num_b >= 50 and num_b <= 70:
        count += 1
    if num_c >= 50 and num_c <= 70:
        count += 1
    if num_d >= 50 and num_d <= 70:
        count += 1

    return count

main()
