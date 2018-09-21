"""Seq XI"""
def main(num):
    """Draw Seq7 with cap"""

    #1st Triangle<UP>
    for i in range(1, num+1):
        var = 0
        for j in range(1, i+1):
            print("%02d" % j, end=" ")
            var = j
        for _ in range(2*num-2*i):
            print("%02d" % var, end=" ")
        for cap1 in range(i-1, 0, -1):
            print("%02d" % cap1, end=" ")
        var1 = i
        print()

    #2nd Triangle<DOWN>
    for var1 in range(num-1, 0, -1):
        for var2 in range(1, var1+1):
            print("%02d" % var2, end=" ")
            var = var2
        for _ in range(2*num-2*var1):
            print("%02d" % var, end=" ")
        for cap2 in range(var1-1, 0, -1):
            print("%02d" % cap2, end=" ")

        print()


main(int(input()))
