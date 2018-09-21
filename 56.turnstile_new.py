"""turnstile new ver"""
def main():
    """This is a new turnstile by P'mai & Jajaja"""
    act = " "
    while 1:
        text = input()
        if text == "END":
            break
        else:
            act += text
    print(act.count("CP"))
main()
