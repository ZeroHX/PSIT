"""save_compute_repeat"""
def main():
    """main func"""
    start = 492137954293754252786
    milli = start
    sec = milli//1000
    milli = milli%1000
    mins = sec//60
    sec = sec%60
    hour = mins//60
    mins = mins%60
    day = hour//24
    hour = hour%24

    print(day, hour, mins, sec, milli)

main()
