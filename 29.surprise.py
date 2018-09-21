"""surprise"""
def main():
    """main func"""
    total, num = float(input()), float(input())

    if num > (total-(num*2) + 2):
        if total == 3 and num == 2:
            print("Not surprising")
        else:
            print("Surprising")
    else:
        print("Not surprising")

main()
