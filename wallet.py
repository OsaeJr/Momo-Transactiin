import main
import back


def wallet():
    print("""
            1.Check Balance
            2.Allow Cash Out
            3. Change PIN 
            0. Back
    """)
    opt_1 = int(input("Choose your option: "))
    if opt_1 == 1:
        pin = int(input("Enter your pin: "))
        if pin == main.passcode:
            quit(f"Your balance is GHS{main.balance}")
        else:
            quit("Invalid PIN")
    elif opt_1 == 2:
        print("""
                Do you want allow Cash Out
                1. YES
                2. NO
                0.BACK
        """)
        opt = int(input("Choose your option:"))
        if opt == 1:
            pin = int(input("Enter pin: "))
            if pin == main.passcode:
                quit("Cash out allowed")
            else:
                quit("Cash Out not allowed due to invalid pin")
        if opt == 2:
            quit("Cash OUT not allowed")
        else:
            quit("Invalid input!")

    elif opt_1 == 3:
        pin = int(input("Enter your pin: "))
        if pin == main.passcode:
            new_pin = int(input("Enter your new pin: "))
            main.passcode = new_pin
            print(f"This is your new pin: {main.passcode} ")
        else:
            quit("Wrong Pin")



