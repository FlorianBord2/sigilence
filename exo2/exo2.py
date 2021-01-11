import exo_fct

#Sorting average freqentation day and return the day value of the less visited one
def smallOne(data):
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
    for day in data:
        return day

def myAlgo(data):
    tmp = {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[]
        }
    fct = exo_fct.journal(data)
    #Adding each frequentation value to his week day
    while fct.hasNextCount():
        data = fct.getNextCount()
        day = fct.getWeekDayFromDate(data[0])
        tmp[day].append(data[1])
    #Calcul of each week day average visitor
    for day in tmp:
        v  = 0
        for value in tmp[day]:
            v = v + value
        if v == 0:
            tmp[day] = 0
        else:
            tmp[day] = v / len(tmp[day])
    return (smallOne(tmp))

#Test main
def main():
    # fct = exo_fct.journal()
    # while fct.hasNextCount():
    #     data = fct.getNextCount()
    #     print(data[0])
    #     print(fct.getWeekDayFromDate(data[0]))

    data = [
            ['11/01/2021',1],
            ['12/01/2021',2],
            ['13/01/2021',3],
            ['14/01/2021',4],
            ['15/01/2021',5],
            ['16/01/2021',6],
            ['17/01/2021',7],
            ['18/01/2021',1],
            ['19/01/2021',2],
            ['20/01/2021',3],
            ['21/01/2021',4],
            ['22/01/2021',5],
            ['23/01/2021',6],
            ['24/01/2021',7]
            ]
    print(myAlgo(data))


if __name__ == '__main__':
    main()
