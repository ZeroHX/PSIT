"""61070023 Frame"""
def main(text):
    """main func"""
    lenght = len(text)
    print("*" * (lenght+2))
    print("*%s*" % text)
    print("*" * (lenght+2))

main(input())
