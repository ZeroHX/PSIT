"""Boot SEQ"""
def main(num):
    """main func"""
    for i in range(1, num):
        print(i, end="_")
    print(num)
main(int(input()))
