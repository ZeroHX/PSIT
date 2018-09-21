"""timing"""
def main():
    """main func"""
    sec = int(input())
    day = sec//86400
    sec -= 86400*day

    hour = sec//3600
    sec -= 3600*hour

    mins = sec//60
    sec -= 60*mins

    print(day, hour, mins, sec)

main()
