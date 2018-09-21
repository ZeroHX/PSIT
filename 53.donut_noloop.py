"""61070023 Donut"""
def main(cost, buy, bonus, need):
    """main func"""
    pack = buy+bonus
    amount = need//pack

    #This is donut set under or equal of need
    donut = amount*buy

    #Plus donut if pack*amount > need

        #ALERT!! SPECIAL CASE
    if need % pack < buy:       #if pack is over, let buy without pro
        donut += need % pack    #amount of donut without pro

    else:
        donut += buy            #Donut with normal pro

    pay = donut*cost
    get = donut + (donut//buy) * bonus

    print(pay, get)

main(int(input()), int(input()), int(input()), int(input()))
