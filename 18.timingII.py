"""Timing II"""
def main():
    """main func"""
    num = int(input())
    sec = num

    day = sec//86400
    sec -= 86400*day

    hour = sec//3600
    sec -= 3600*hour

    mins = sec//60
    sec -= 60*mins

    if num >= 0 and num < 864000000:
        print("%04d:%02d:%02d:%02d" % (day, hour, mins, sec))
    else:
        print("ERR_:__:__:__")

main()
