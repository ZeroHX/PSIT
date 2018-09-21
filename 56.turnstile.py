"""Turnstile"""
def main():
    """main func"""
    count = 0
    stage = 0
    mem = 0

    while 1:
        act = input()
        if act == "END":
            break
        #stage 0 No coin
        if stage == 0:
            if act == "C":
                stage = 1
            else:
                stage = 0

        #stage 1 Coin
        if stage == 1:
            mem = 1
            stage = 2
            continue

        #stage 2 Door open return to s0
        if stage == 2 and mem == 1 and act == "P":
            count += 1
            mem = 0
            stage = 0

    print(count)



main()
