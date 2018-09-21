"""data_spike"""
def main():
    """main func"""
    result = 0
    num_a = calc(int(input()), int(input()))
    num_b = calc(int(input()), int(input()))
    num_c = calc(int(input()), int(input()))
    num_d = calc(int(input()), int(input()))

    num_e = calc(num_a, num_b)
    num_f = calc(num_c, num_d)
    result = calc(num_e, num_f)

    print(result)

def calc(num1, num2):
    """calculate"""
    if num1 > num2:
        return num1
    else:
        return num2

main()
