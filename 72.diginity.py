"""61070023  diginity midterm 4"""
def main():
    """
    This problem want you to find sum of input until they have only 1 digits
    EX: 47 >> 4+7 = 11   =>   11 >> 1+1 = 2
    Answer is  2

    """
    while 1:     #This is the infinite input loop until input = 0
        num = int(input())
        if num == 0:    #End loop
            break

        else:           #Continue calc
            while len(str(num)) != 1:   #This loop run a sum loop until they have only 1 digit.
                result = 0
                for i in str(num):      #This loop perform a sum of all digit.
                    result += int(i)
                    num = result
            print(num)

main()
