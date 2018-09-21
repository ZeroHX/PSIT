"""dayI"""
def main(year):
    """main func"""
    if year > 0:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("Yes")
        else:
            print("No")
main(int(input()))
