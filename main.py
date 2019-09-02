#MAIN FUNCTION #
import sys
import commands


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
        print("-=###############################=-")
        print("-=###### Welcome to YBPMC ######=-")
        print("-=######### Py.v01 ##########=-")
        print("-=###############################=-")
        print("Choose one:")
        print("1. BTC Profit Calculator")
        print("2. How High it has to go?")
        print("3. What is my BTC worth?")
        print("4. How much coins I need for profit?")
        print("5. Your average BTC Value #NOTWORKING#")
        choice = int(input("Enter Option Number #:\n"))
        # CHOICE OF CASE  //IF #
        # CHOICE #0 EXIT #
        if choice == 0:
            programRun = 0

        # CHOICE #1 BTCPROFIT FUNC CALL #
        elif choice == 1:
            commands.option1()
        # CHOICE #2 HOW HIGH #
        elif choice == 2:
            commands.option2()
        # CHOICE #3 BTC WORTH #
        elif choice == 3:
            commands.option3()
        # CHOICE #4 PROFIT NEED #
        elif choice == 4:
            commands.option4()
        # CHOICE #5 AVERAGE BTC #
        elif choice == 5:
            print("This Function is Disabled for now! :)")
            input("PRESS ENTER TO CONTINUE\n")

        else:
            print("\n\n404#EXPECTED CHOICE ERROR#404\n\n")
            input("PRESS ENTER TO CONTINUE\n")


# RUNTIME LAYER #
if __name__ == "__main__":
    main()