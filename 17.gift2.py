"""gift II"""
def main():
    """main func"""
    num_a = calc(int(input()))
    num_b = calc(int(input()))
    num_c = calc(int(input()))
    num_d = calc(int(input()))
    num_e = calc(int(input()))
    num_f = calc(int(input()))
    num_g = calc(int(input()))
    num_h = calc(int(input()))

    print(num_a+num_b+num_c+num_d+num_e+num_f+num_g+num_h)

def calc(num):
    """calculate"""
    result = 0
    if num % 2 == 0:
        result += num
        return result
    else:
        return result * 0


main()
