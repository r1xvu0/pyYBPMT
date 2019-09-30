import main
import os
import requests
import time
import wget

global totalValue
BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'


def norm(a):
    return ' '.join([a[i:i + 3] for i in range(0, len(a), 3)])


def update():
    new_version = open("pyybpmt_version.cfg")
    newer = new_version.readlines()
    new = float(newer[0])
    if os.path.exists("update"):
        print("Preparing update folder...")
    else:
        print("Update folder does not exist, creating it...")
        os.mkdir("update")

    if os.path.exists('main.py') & os.path.exists('commands.py'):
        print("Downloading Source Update for PyYBPMT v" + str(new))
        src = "https://johnyxmd.keybase.pub/pyYBPMT_v" + str(new) + "_source.zip?dl=1"
        wget.download(src, out="update/")
        print("")
        print("Done")
        print("How to Update:")
        print("Close PyYBPMT, go to update folder, extract the zip file and rewrite all files")
        input()
        quit()

    elif os.path.exists('PyYBPMT.exe'):
        print("Downloading Executable Update for PyYBPMT v" + str(new))
        exe = "https://johnyxmd.keybase.pub/PyYBPMT_v" + str(new) + ".exe?dl=1"
        wget.download(exe, out="update/")
        print("")
        print("Done")
        print("How to Update:")
        print("Close PyYBPMT, go to update folder, copy and rewrite the old PyYBPMT with the new one\nThe PyYBPMT_vXX.XX rename to PyYBPMT")
        input()
        quit()

    else:
        print("Unknown Runner!!!!!!!")


def check_update():
    if os.path.exists('pyybpmt_version.cfg'):
        print("Old version file detected")
        os.remove("pyybpmt_version.cfg")
        print("Deleting Old files...")
        input("Enter to continue")
        check_update()

    else:
        print("Checking for Update...")
        url = "https://johnyxmd.keybase.pub/pyybpmt_version.cfg?dl=1"
        wget.download(url)
        version = main.version
        new_version = open("pyybpmt_version.cfg")
        newer = new_version.readlines()
        new = float(newer[0])
        print("")
        if version == new:
            print("Version " + str(newer[0]) + " Detected")
            print("Your version of PyYBPMT is Up-to-Date!")
            cont()
        elif version > new:
            print("Somehow you managed to get Unreleased Version... You sick son of a ...")
            cont()
        elif version < new:
            print("Detected old version " + str(version) + " of PyYBPMT")
            print("Newest version detected: " + str(newer[0]))
            upd = int(input("Do you wish to Update? Y[1]/N[2]"))
            if upd == 1:
                update()
            else:
                print("Okay then!")
                cont()
        else:
            print("Wrong")


# Main Menu print #
def menu():
    print('''
    ###############################################
    ###############################################
    ############# Welcome to PyYBPMT ##############
    ###############################################
    ################# Py-v1.3 #####################
    ###############################################
    ###############################################
    ###############################################

    1.  BTC Profit Calculator          7.  *UPDATE* 
    1.1 BTC Average Profit                
    2.  How High it has to go?            
    3.  What is my BTC worth?             
    3.1 Your average BTC Value            
    4.  Coin price for Profit             
    5.  BTC Live Price - CoinMarketCap    
    6.  Next Page -->                      
    0.  Exit                              

    ''')


def menu2():
    print('''
    ###############################################
    ###############################################
    ############# Welcome to PyYBPMT ##############
    ###############################################
    ################# Py-v1.3 #####################
    ###############################################
    ############ www.yannickworks.cf ##############
    ###############################################
    ###############################################

    1.  KeyBase (NOT WORKING)
    0.  <-- Back
    ''')


# Function to Continue or Quit the program #
def cont():
    conti = int(input("Do you wish to Continue[1] or Exit[2]?\n"))
    if conti == 1:
        print("")

    elif conti == 2:
        os.system("cls" if os.name == "nt" else "clear")
        quit()
    else:

        print("Wrong choice, automatically continuing")


# 1 Function for BTC Profit #
def option1():
    # Take all vars #
    print("\nEnter BTC at Buy Position:")
    btcValue = float(input())

    print("Enter BTC at Sell Position:")
    btcSellValue = float(input())

    print("Enter amount of BTC Traded:")
    amountTraded = float(input())

    print("Enter your Leverage X:")
    leverageUsed = float(input())

    print("Enter your Exchange Fees (x%):")
    exchangeFee = float(input())

    # Calculate #
    profit = (btcSellValue * amountTraded) - (btcValue * amountTraded)
    totalValue = (profit + (btcValue * amountTraded)) / leverageUsed

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


# 1.1 Function for Average BTC Profit #
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
        cont()
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


# Function to show Live BTC Price #
def option5():
    livePrice = requests.get(BITCOIN_API_URL)
    livePrice_json = livePrice.json()
    print("BTC Price now is: " + str(livePrice_json[0]['price_usd']))
    print("BTC Available supply now is: " + str(norm(livePrice_json[0]['available_supply'])))
    k = livePrice_json[0]['24h_volume_usd']
    print("24H Volume is at: " + str(norm(k)))
    cont()


# Function Save to File #
def save(file, option):
    if os.path.exists("data/"):
        print("Saving to file Now...")
        fileWrite = open("data/" + file + ".btc", "+a")
        fileWrite.writelines(str(option) + "\n")
        cont()
    else:
        print("Directory not found. Creating it now!")
        os.mkdir("data")
        print("Directory Data created.")
        print("Saving to file Now...")
        fileWrite = open("data/" + file + ".btc", "+a")
        fileWrite.writelines(str(option) + "\n")
        cont()

