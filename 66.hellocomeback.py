"""61070023 Hello world come back"""
def main(text):
    """check language TH/EN if TH >> สวัสดี  EN >> Hello"""
    for i in text:
        if 65 <= ord(i) <= 122:
            print("Hello %s." % text)
        else:
            print("สวัสดี %s" % text)
        break
main(input())
