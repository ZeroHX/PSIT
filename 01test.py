name = input("Enter name: ")
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
if name[0] in abc:
    print("Hello %s." % name)
else:
    print("สวัสดี %s" % name)