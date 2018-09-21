"""61070023  Divide3or5"""
def main(num):
    """print sum of number that divide 3 or 5"""
    result = 0
    for i in range(1, num+1):
        if i % 5 == 0 or i % 3 == 0:
            result += i

    print(result)

main(int(input()))
