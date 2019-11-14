def coinAvg(coins, average):    # updates the averages for each list of coins
    for x in range(len(coins)):
        sum = 0
        if(len(coins[x])>1):
            for y in range(len(coins[x])):
                sum = sum + coins[x][y][2]
            average[x] = sum/(len(coins[x])-1)
        elif(len(coins[x]) == 1):
            average[x] = coins[x][0][2]
        else:
            average[x] = 0

    return average

def coinStrdev(average): #updates the standard deviations for each list of coins
    strdev = [0,0,0,0]
    for x in range(4):
        strdev[x] = (average[x]*.0675)
    return strdev

def coinFinder(circles):    #main function
    coins = [[[0,0,0]],[[0,0,0]],[[0,0,0]],[[0,0,0]]] # this is a list of list. Each list represents a different type of coin
                                                      # ex: [[quarter],[dime],[nickel][outliers]] or [[dime], [nickel], [quarter], [outlier]]
    i = 0
    average = [0, 0, 0, 0]
    for x in range(len(circles)):   # goes through circles list and sperates the coins by their size and puts them into list coins
        average = coinAvg(coins, average)
        strdev = coinStrdev(average)
    #prints newest coin and updated averages and strdevs
        # for u in range(len(average)):
        #     print("Average: ", average[u], "StrDev: ", strdev[u])
        # print("Circle: ", circles[x][2])
        n=0
        if(x==0):
            coins[i].append(circles[x]) #adds 1st coin
            i=i+1
        else:
            while(n<=3):
                if(n!=i and average[n]!=0):
                    if((circles[x][2] <= average[n]+strdev[n]) and (circles[x][2] >= average[n]-strdev[n])): #checks if circle fits in the standard deviations of each list
                        coins[n].append(circles[x])
                        n=4
                else:
                    coins[i].append(circles[x]) # puts circle in the 1st spot of the next list if it doesnt fit any of the other list
                    i=i+1
                    n=4
                n=n+1

    amount = [.25, .05, .10]

# prints the whole list of coins
    # for x in range(len(coins)):
    #     for y in range(len(coins[x])):
    #         print("Coin: ", coins[x][y][2])
    # for x in range(len(strdev)):
    #     print(x, ": ", strdev[x])

    total = 0
    for y in range(len(amount)):    # calculates the total money
        highest = 0
        high_index = 0
        for x in range(len(coins)-1):   #finds which list has the biggest coin
            if(coins[x][1][2] > highest):
                highest = coins[x][1][2]
                high_index = x
        total = total + (amount[y] * (len(coins[high_index])-1))    #calculates total

        del coins[high_index]   #deletes the list that was just used
    return total


def main():
    circles = [[0,0,61.379],
            [0,0,62.208],
            [0,0,52.943],
            [0,0,45.478],
            [0,0,44.952],
            [0,0,55.685],
            [0,0,62.356],
            [0,0,62.661],
            [0,0,59.762],
            [0,0,55.003],
            [0,0,45.278],
            [0,0,65.081],
            [0,0,46.167],
            [0,0,64.727],
            [0,0,63.297],
            [0,0,64.207],
            [0,0,63.138]]
    total = coinFinder(circles)
    print(total)

main()
