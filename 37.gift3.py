"""GiftIII"""
def main():
    """main func"""
    num = int(input())      #amount
    high = 0                #1st
    sec = 0                 #2nd
    for _ in range(num):        #Run Weight
        num1 = int(input())
        if num1 > high:
            sec = high
            high = num1
        if num1 > sec and num1 < high:
            sec = num1

    if high != 0 and sec != 0:
        print(sec)
    else:
        print("Exit")

main()
