""" PSIT 61 - Exercise 76 (RockPaperScissors) """
def rps(data, count):
    """ This function prints the total score of Rock Paper Scissors between 2 people """
    match = ""
    for i in data:
        match += i
        count += 1
        if count % 3 == 0:
            match += " "
            count = 1

    win = match.count("RS") + match.count("SP") + match.count("PR")
    lose = match.count("SR") + match.count("PS") + match.count("RP")
    draw = (match.count("RR") + match.count("SS") + match.count("PP")) * 2

    if win > lose:
        print("A win %d-%d" %(win, lose))
    elif lose > win:
        print("B win %d-%d" %(lose, win))
    else:
        print("DRAW %d" %draw)

rps(input(), 1)