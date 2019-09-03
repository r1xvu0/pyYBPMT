#MAIN FUNCTION #
import sys
import commands
import os


def main():
    # SHITLOAD OF VARS ###
    programRun = 1
    btcValue = 0
    amountTraded = 0
    btcSellValue = 0
    totalValue = 0
    exchangeFee = 0
    profit = 0
    profitCalc = 0
    feeProfit = 0
    percGain = 0
    increase = 0
    negaFee = False

    # Making sure we loop back at the start of the program #
    while programRun == 1:
        print("\t\t\t\t\t -=###############################=-")
        print("\t\t\t\t\t -=###### Welcome to YBPMT ######=-")
        print("\t\t\t\t\t  -=########## Py-V1.0 ##########=-")
        print("\t\t\t\t\t -=###############################=-")
        print("Choose one:")
        print("1. BTC Profit Calculator")
        print("1.1 BTC Average Profit")
        print("2. How High it has to go?")
        print("3. What is my BTC worth?")
        print("3.1 Your average BTC Value")
        print("4. How much coins I need for profit?")
        choice = float(input("Enter Option Number #:\n"))
        # CHOICE OF CASE  //IF #
        # CHOICE #0 EXIT #
        if choice == 0:
            programRun = 0

        # CHOICE #1 BTC PROFIT FUNC CALL #
        elif choice == 1:
            commands.option1()
        # CHOICE #1.1 AVERAGE PROFIT #
        elif choice == 1.1:
            commands.option11()
        # CHOICE #2 HOW HIGH #
        elif choice == 2:
            commands.option2()
        # CHOICE #3 BTC WORTH #
        elif choice == 3:
            commands.option3()
        # CHOICE #5 AVERAGE BTC #
        elif choice == 3.1:
            commands.option31()
        # CHOICE #4 PROFIT NEED #
        elif choice == 4:
            commands.option4()

        else:
            print("\n\n404#EXPECTED CHOICE ERROR#404\n\n")
            input("PRESS ENTER TO CONTINUE\n")


# RUNTIME LAYER #
if __name__ == "__main__":
    main()