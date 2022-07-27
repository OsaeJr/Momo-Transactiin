import main


def momo_user():
    number = str(input("Enter your the MTN number: "))
    if len(number) != 10:
        print("Invalid number,try again")
        momo_user()
    check = str(input("Re-enter your the MTN number: "))

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
        print("Number mismatch, try again")
        momo_user()
