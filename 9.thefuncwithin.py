"""thefunc"""
def main():
    """main func"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_d = float(input())

    def funcf(num_x):
        """function F"""
        return 2*num_x

    def funcg(num_x):
        """function G"""
        return 3*(num_x**4) - (num_x**3) +2*(num_x**2) +10

    def funch(num_x, num_y, num_z):
        """function H"""
        return (num_z+num_x)**2 - num_x*num_y + (num_y**2)

    def funci(num_x, num_y, num_z, num_w):
        """function I"""
        return ((num_x**2) + (num_y**2) - (num_z**2)) / ((num_w**2) - 2*num_x*num_w + 2*num_x)

    print(funcf(funcf(num_a)))
    print(funcg(funcf(num_a - num_b)))
    print(funch(funcf(num_a + num_b), funcf(num_a+num_c), funcg(funcf(num_d**2))))
    print(funci(funch(funcf(num_a+num_b), funcf(num_a-num_c), funcg(funcf(num_d**2))), \
        funcg(funcf(num_a-num_b)), funcf(funcf(funcf(funcf(funcf(num_c))))), num_d**8))

main()
