import main
import os

global totalValue


# Function to Continue or Quit the program #
def cont():
    conti = int(input("Do you wish to Continue[1] or Exit[2]?\n"))
    if conti == 1:
        print("")
    elif conti == 2:
        quit()
    else:
        print("Wrong choice")


# 1 Function for BTC Profit #
def option1():
    # Take all vars #
    print("\nEnter BTC at Buy Position:")
    btcValue = float(input())

    print("Enter BTC at Sell Position:")
    btcSellValue = float(input())

    print("Enter amount of BTC Traded:")
    amountTraded = float(input())

    print("Enter your Exchange Fees:")
    exchangeFee = float(input())

    # Calculate #
    profit = (btcSellValue * amountTraded) - (btcValue * amountTraded)
    totalValue = profit + (btcValue * amountTraded)

    # Results #
    print("Your pure profit is: " + str(profit))
    print("Your total value is: !" + str(totalValue) + "!")
    profitCalc = (profit / 100) * exchangeFee
    feeProfit = profit - profitCalc

    # Take care of Loss instead of Profit #
    negFee = bool(feeProfit < 0)
    if negFee == True:
        negaFee = profit - profitCalc
        print("Your profit with fees is: " + str(negaFee))
    else:
        print("Your profit with fees is: " + str(feeProfit))

    increase = btcSellValue - btcValue
    percGain = (increase / btcValue) * 100
    print("Your percentage gain is: " + str(percGain) + "%")
    print("")

    choice = int(input("Would you like to save the result? Y[1]/N[2]"))
    if choice == 1:
        save("profit", profit)
    elif choice == 2:
        cont()
    else:
        print("Wrong choice!")

def option11():
    print("Looking for data file...")
    if os.path.exists("data/profit.btc"):
        print("File Found!\nOpening...")
        fileRead = open("data/profit.btc", "+r")
        avprofit = fileRead.readlines()

        x = 0
        sum = 0.0
        for line in avprofit:
            print(avprofit[x])
            sum += float(avprofit[x])
            x += 1

        average = int(sum) / int(len(avprofit))
        print("Your average BTC Value is " + str(average))
        cont()
    else:
        print("Data file not found\nPlease save some results before trying again!\n")
        input("PRESS ENTER TO CONTINUE\n")
    return

# 2 Function for EXPECTED RESULT #
def option2():
    expectedResult = 0
    amountOwned = 0
    valueNeeded = 0
    print("")
    expectedResult = float(input("What is your expected result: "))
    amountOwned = float(input("How much coins do you own: "))

    valueNeeded = expectedResult / amountOwned
    print("Your coins need to get to:")
    print(str(valueNeeded) + "$$$ to reach your goal of " + str(expectedResult) + "$")
    print("")
    cont()


# 3 Function for BTC Worth #
def option3():
    print("")
    btcValue = float(input("BTC Value Now:\n"))
    amountTraded = float(input("Enter amount of BTC HODLED:\n"))
    totalValue = amountTraded * btcValue
    print("Your " + str(amountTraded) + " BTC is worth $" + str(totalValue) + "$ at Value of " + str(btcValue) + " per Coin")
    print("")
    choice = int(input("Would you like to save the result? Y[1]/N[2]"))
    if choice == 1:
        save("networth", totalValue)
    elif choice == 2:
        cont()
    else:
        print("Wrong choice!")


# 3.1 Function MY AVERAGE BTC #
def option31():
    print("Looking for data file...")
    if os.path.exists("data/networth.btc"):
        print("File Found!\nOpening...")
        fileRead = open("data/networth.btc", "+r")
        networth = fileRead.readlines()

        x = 0
        sum = 0.0
        for line in networth:
            print(networth[x])
            sum += float(networth[x])
            x += 1

        average = int(sum) / int(len(networth))
        print("Your average BTC Value is " + str(average))
        cont()

    else:
        print("Data file not found\nPlease save some results before trying again!\n")
        input("PRESS ENTER TO CONTINUE\n")
    return


# 4 Function for How Many Coins #
def option4():
    print("")
    totalValue = float(input("Enter expected profit:\n"))
    btcValue = float(input("Enter Buy price:\n"))
    btcSellValue = float(input("Enter expected SELL price:\n"))

    global coinsNeeded
    coinsNeeded = totalValue / (btcSellValue - btcValue)
    print("You would need to have " + str(coinsNeeded) + " BTC to reach your expected profit!")
    cont()


def save(file, option):
    print("Saving to file Now...")
    fileWrite = open("data/" + file + ".btc", "+a")
    fileWrite.writelines(str(option) + "\n")
    cont()
