"""train"""
def main():
    """main func"""
    text1 = input()
    text2 = input()
    time = int(input())

    print("%s%s" % (text1, text2))
    print(("%s%s" % (text1, text2)) * time)

main()
