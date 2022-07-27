import main
import momo_user_1


def transfer_money():
    print("""
              1. MoMo User
              5. Other Network
              0. Back
              """)
    opt = int(input("Choose your option: "))
    if opt == 1:
        momo_user_1.momo_user()
    elif opt == 5:
        print("""
                Transfer Money to Other Network
                1. AirtelTigo
                2. Vodafone             
            """)
        opt_1 = int(input("Choose your network: "))
        if opt_1 == 1 or opt_1 == 2:
            number = str(input("Enter your the AirtelTigo or Vodafone number: "))
            if len(number) != 10:
                quit("Invalid number,Start the process again")
            check = str(input("Re-enter your AirtelTigo or Vodafone number: "))

            if number == check:
                amount = int(input("Enter amount(in GHS): "))
                pin = int(input("Enter your pin: "))
                if pin == main.passcode:
                    if amount > main.balance:
                        quit("You have insufficient funds")

                    else:
                        new_balance = main.balance - amount
                        print(f"you have withdrawn GHS{amount}, your balance is GHS{new_balance}")
                        quit()

                else:
                    quit("Invalid pin!,Start the program again")
            else:
                quit("The two numbers are not the same,Start the process again")

