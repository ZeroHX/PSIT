"""SwitchSceneI
Ver4.0 FACJ-ed1"""

    #0 = off
    #1 = daylight
    #2 = warmlight <Special_case>

def main(state, data, sec1, count):
    """main func"""

    if data == "End":
        state = data
    else:
        state = 1
        sec1 = float(data)      #To find diff <will change when end loop>

    #Run Loop
    while state != "End":
        data2 = input()
        if data2 == "End":
            state = data2
        else:
            sec2 = float(data2)
            if state == 0:      #Change off to Daylight
                state = 1
            elif state == 1:    #Change Daylight to CheckSPcase <Warm/Day>
                state = 1.5
            elif state == 2:    #Change Warmlight to off
                state = 0
            elif state == 1.5:       #Check SP_case
                if sec2 - sec1 > 6:     #Back to Daylight
                    state = 1
                else:
                    state = 2           #Pass to Warm
                    count += 1
        sec1 = sec2                 #Change to find diff next loop
    print(count)

main(0, input(), 0, 0)
