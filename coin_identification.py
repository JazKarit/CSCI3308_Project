def coinAvg(coins, average):    # updates the averages for each list of coins
    average = []
    for x in range(len(coins)):
        sums = 0
        if(len(coins[x])>1):
            for y in range(len(coins[x])):
                sums = sums + coins[x][y]
            average.append(sums/(len(coins[x])))
        elif(len(coins[x]) == 1):
            average.append(coins[x][0])
    return average

def coinStrdev(average): #updates the standard deviations for each list of coins
    strdev = []
    for x in range(len(average)):
        strdev.append(average[x]*.0675)
    return strdev

def coinFinder(circles):    #main function
    coins = [[],[],[],[]] # this is a list of list. Each list represents a different type of coin
                                                      # ex: [[quarter],[dime],[nickel][outliers]] or [[dime], [nickel], [quarter], [outlier]]
    i = 0
    average = []
    for x in range(len(circles)):   # goes through circles list and sperates the coins by their size and puts them into list coins
        average = coinAvg(coins, average)
        strdev = coinStrdev(average)
    #prints newest coin and updated averages and strdevs
        # for u in range(len(average)):
        #     print("Average: ", average[u], "StrDev: ", strdev[u])
        # print("Circle: ", circles[x][1])
        n=0
        if(x==0):
            coins[i].append(circles[x][1]) #adds 1st coin
            i=i+1
        else:
            while(n<=3):
                if(n!=i and average[n]!=0):
                    if((circles[x][1] <= average[n]+strdev[n]) and (circles[x][1] >= average[n]-strdev[n])): #checks if circle fits in the standard deviations of each list
                        coins[n].append(circles[x][1])
                        n=4
                else:
                    coins[i].append(circles[x][1]) # puts circle in the 1st spot of the next list if it doesnt fit any of the other list
                    i=i+1
                    n=4
                n=n+1

    amount = [0,0,0,0]
    highest = 0
    high_index = 0
    changes = 1
    for x in range(len(average)):
        if(coins[x][0] > highest):
            highest = coins[x][0]
            high_index = x
            amount[x] = .25
    for x in range(len(average)):
        if(x!=high_index):

            if(((average[high_index]/average[x]) <= (1.1916+.10985)) and ((average[high_index]/average[x]) >= (1.1916-.10985))):
                amount[x] = .05
            #Pennies error bounds:
            # elif(((average[high_index]/average[x]) <= (1.3267+.0423)) and ((average[high_index]/average[x]) >= (1.3267-.06755))):
            #     amount[x] = .01
            elif(((average[high_index]/average[x]) <= (1.4113+.10985)) and ((average[high_index]/average[x]) >= (1.4113-.10985))):
                amount[x] = .10
                

# prints the whole list of coins
    for x in range(len(coins)):
        print("List", x, ":")
        for y in range(len(coins[x])):
            print("Coin: ", coins[x][y])
    for x in range(len(strdev)):
        print(x, ": ", strdev[x])

    total = 0
    for x in range(len(coins)):    # calculates the total money
        total = total + (amount[x] * (len(coins[x])))    #calculates total
    return total


if __name__== '__main__':
    circles = [[(0,0),61.379], #Sum = $3.05
            [(0,0),62.208],
            [(0,0),52.943],
            [(0,0),45.478],
            [(0,0),44.952],
            [(0,0),55.685],
            [(0,0),62.356],
            [(0,0),62.661],
            [(0,0),59.762],
            [(0,0),55.003],
            [(0,0),45.278],
            [(0,0),65.081],
            [(0,0),46.167],
            [(0,0),64.727],
            [(0,0),63.297],
            [(0,0),64.207],
            [(0,0),63.138]]
    circles2 = [[(0,0),61.379], #Sum = $2.65
            [(0,0),62.208],
            [(0,0),45.478],
            [(0,0),44.952],
            [(0,0),62.356],
            [(0,0),62.661],
            [(0,0),45.278],
            [(0,0),65.081],
            [(0,0),46.167],
            [(0,0),64.727],
            [(0,0),63.297],
            [(0,0),64.207],
            [(0,0),63.138]]
    circles3 = [[(0,0),61.379], #Sum = $1.00
            [(0,0),62.208],
            [(0,0),62.356],
            [(0,0),62.661]]
    circles4 = [((303.3307189941406, 114.0750503540039), 36.49294662475586),
((601.2237548828125, 132.0644073486328), 47.30678939819336),
((760.9459228515625, 137.1351318359375), 48.10158920288086),
((435.67669677734375, 138.0488739013672), 36.912940979003906),
((277.6201171875, 182.35491943359375), 34.313232421875), ((415.5,
219.5), 37.10131072998047), ((768.1914672851562, 235.91844177246094),
43.16984176635742), ((126.15723419189453, 245.76100158691406),
41.93385696411133), ((566.0, 255.0), 38.07896423339844),
((315.326171875, 303.1930236816406), 47.69312286376953),
((549.7882690429688, 369.5490417480469), 49.373958587646484),
((824.5972290039062, 388.59722900390625), 51.17155838012695),
((705.9117431640625, 421.0882263183594), 44.678226470947266),
((336.625, 427.5), 36.57728576660156), ((470.39849853515625,
506.1278076171875), 37.89807891845703)]

    total = coinFinder(circles2)
    print(total)
