"""61070023 blackjack"""
def main(num):
    """Main func"""
    score, ace = 0, 0
    for _ in range(num):
        card = input()
        if card == "J" or card == "Q" or card == "K":
            score += 10
        elif card == "A":
            ace += 1
            score += 1
        else:
            score += int(card)

    for _ in range(ace):
        score += 10
        if score > 21:
            score -= 10

    print(score)

main(int(input()))
