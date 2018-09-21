"""61070023  RockPaperScissor"""
def main(act, score_a, score_b):
    """

    This input are the RPS battle between playerA & playerB switch each other
    Question is Who is the winner and what is score

    """

    for i in range(0, len(act), 2):
        if act[i:i+2] == "RP" or act[i:i+2] == "PS" or act[i:i+2] == "SR":
            score_b += 1
        elif act[i:i+2] == "RS" or act[i:i+2] == "PR" or act[i:i+2] == "SP":
            score_a += 1

    if score_a > score_b:
        print("A win %d-%d" % (score_a, score_b))
    elif score_b > score_a:
        print("B win %d-%d" % (score_b, score_a))
    else:
        print("DRAW %d" % score_a)


main(input(), 0, 0)
