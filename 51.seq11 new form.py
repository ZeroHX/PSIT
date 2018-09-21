"""61070023 Seq 11<new ver.>"""
def main(num):
    """new form"""
    for i in range(1-num, num):
        for j in range(1-num, num):
            print("%02d" % (num-max(abs(i), abs(j))), end=" ")
        print()

main(int(input()))
