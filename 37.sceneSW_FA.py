"""SceneSwitch FA_ver"""
def main():
    """main func"""

    ##0 = off, 1 = Daylight, 2 = Warmlight

    now = 0
    nxt = 1
    count = 0
    start = input()
    if start != "End":
        start = input()

    while sec != "End":
        sec1 = input()
        if sec1 != "End":
            #0 Light off
            if now == 0 and nxt == 1:
                now == 1
                nxt == 0
            elif now == 0 and nxt == 2:
                now == 2
                nxt == 0
                count += 1

            #1 Daylight
            elif now == 1 and float(start-sec1) <= 6:
                now = 0
                nxt = 2
            elif now == 1 and float(start-sec1) > 6:
                now = 0
                nxt = 1

            #2 Warmlight
            elif now == 2:
                now = 0
                nxt = 1


        else:
            break

    print(count)

main()
