#MAIN FUNCTION #
import sys
import commands
import os
import json


version = 1.31


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
        os.system("cls" if os.name == "nt" else "clear")
        commands.menu()

        # CHOICE OF CASE  //IF #
        # CHOICE #0 EXIT #
        # TRY TO EXCEPT VALUEERROR #
        try:
            choice = float(input("Enter Option Number #: "))

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
        # CHOICE #5 BTC LIVE PRICE #
            elif choice == 5:
                commands.option5()
        # Page 2 of the List #
            elif choice == 6:
                programRun = 2
            elif choice == 7:
                commands.check_update()
        # Expect wrong choice #
            else:
                print("\n\n404#EXPECTED CHOICE ERROR#404\n\n")
                input("PRESS ENTER TO CONTINUE\n")

        except ValueError:
            print("Invalid syntax")
            print("Please don't use Commas, use Dots")
            input("PRESS ENTER TO CONTINUE")


    while programRun == 2:
        os.system("cls" if os.name == "nt" else "clear")
        commands.menu2()

        try:

            choice = int(input("Enter Option Number #: "))

            if choice == 0:
                os.system("cls" if os.name == "nt" else "clear")
                programRun = 1
                main()
            elif choice == 1:
                print("SoonTM")
                input("Enter to Continue")
                os.system('cls')
            else:
                print("\n\n404#EXPECTED CHOICE ERROR#404\n\n")
                input("PRESS ENTER TO CONTINUE\n")
                os.system("cls" if os.name == "nt" else "clear")

        except ValueError:
            print("Invalid syntax")
            print("Please don't use Commas, use Dots")
            input("PRESS ENTER TO CONTINUE")



# RUNTIME LAYER #
if __name__ == "__main__":
    main()