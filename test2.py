"""Source code
By:Suphitsara Cheevanantaporn
"""
def main():
    """function"""
    name = input()
    if ord(name[0]) >= 65 and ord(name[0]) <= 122:
        print("Hello %s." %(name))
    else:
        print("สวัสดี %s" %(name))
main()