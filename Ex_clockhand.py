"""Ex_clockhand"""
def main(hrs, mins):
    """This problem want to find hand_h and hand_m in condition below"""
    #Change [hours to mins]
    ##EX. hrs = 1, mins = 6 >> hand_h = 5+(0.5)
    hand_h = (hrs * 5) + (mins / 12)

    #find that both hand will equal or not
    if hand_h >= mins and (hand_h -mins) < 1:
        print("True")
    else:
        print("False")

main(int(input()), int(input()))
