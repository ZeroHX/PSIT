"""61070023  Hamburger"""
def main(front, back):
    """print hamburger like ||**********|||
    inp = 2, 3 <a bread front and back hamburger>
    in middle print "*" * (inp1 + inp2) *2"""

    print("|" * front, end="")
    print("*" * ((front+back)*2), end="")
    print("|" * back, end="")

main(int(input()), int(input()))
