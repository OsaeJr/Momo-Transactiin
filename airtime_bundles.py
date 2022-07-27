import main


def airtime_bundles():
    print("""
            Airtime & bundles  
            1. Airtime
            2. Internet bundles
            0. Back
     """)
    opt = int(input("Choose your option: "))
    if opt == 1:
        print("""
                Airtime
                1. Self
                2. Others
                0. Back
            """)
        opt_1 = int(input("Choose your option: "))
        if opt_1 == 1:
            amount = int(input("Enter amount: "))
            pin = int(input(f"You are buying GHS{amount} airtime, Enter your pin to proceed: "))
            if pin == main.passcode:
                if amount > main.balance:
                    print("Sorry, you have insufficient funds")
                    quit()
                else:
                    new_balance = main.balance - amount
                    print(f"you have purchased GHS{amount} airtime, your balance is GHS{new_balance}")
                    quit()

        elif opt_1 == 2:
            amount = int(input("Enter amount: "))
            number = str(input("Enter phone number: "))
            if len(number) != 10:
                print("Invalid number,Start the process again")
            pin = int(input(f"You are buying and sending GHS{amount} airtime to {number}, Enter your pin to proceed: "))
            if pin == main.passcode:
                if amount > main.balance:
                    print("Sorry, you have insufficient funds")
                    quit()
                else:
                    new_balance = main.balance - amount
                    print(f"you have purchased and sent GHS{amount} airtime, your balance is GHS{new_balance}")
                    quit()
        elif opt_1 == 0:
            airtime_bundles()

        else:
            quit("Invalid input, Try again")


    elif opt == 2:
        print("""
                Welcome to the Bundle Portal, Please select your bundle
                1. Buy Data Bundle
                2. Midnight Bundle
                0. Back to main menu
            """)
        opt_1 = int(input("Choose your option: "))
        if opt_1 == 1:
            print("""
                    1. Buy for self
                    2. Buy for others
            """)
            opt_2 = int(input("Choose your choice: "))
            if opt_2 == 1:
                print("""
                        1.GHS 10(30MB)
                        2.GHS 40 (70MB)
                        3.GHS 70 (100MB)
                    """)
                opt_3 = int(input("Choose your choice: "))
                if opt_3 == 1:
                    pin = int(input(f"You are buying GHS10 data bundle(30MB), Enter your pin to proceed: "))
                    if pin == main.passcode:
                        if 10 > main.balance:
                            print("Sorry, you have insufficient funds")
                            quit()
                        else:
                            new_balance = main.balance - 10
                            print(f"you have purchased and sent GHS10 airtime, your balance is GHS{new_balance}")
                            quit()

                elif opt_3 == 2:
                    pin = int(input(f"You are buying GHS40 data bundle(70MB), Enter your pin to proceed: "))
                    if pin == main.passcode:
                        if 40 > main.balance:
                            print("Sorry, you have insufficient funds")
                            quit()
                        else:
                            new_balance = main.balance - 40
                            print(f"you have purchased and sent GHS40 airtime, your balance is GHS{new_balance}")
                            quit()

                elif opt_3 == 3:
                    pin = int(input(f"You are buying GHS10 data bundle(70MB), Enter your pin to proceed: "))
                    if pin == main.passcode:
                        if 70 > main.balance:
                            print("Sorry, you have insufficient funds")
                            quit()
                        else:
                            new_balance = main.balance - 70
                            print(f"you have purchased and sent GHS70 airtime, your balance is GHS{new_balance}")
                            quit()

                else:
                    quit("Invalid input, Start the program again")

            elif opt_2 == 2:
                number = str(input("Enter phone number: "))
                if len(number) != 10:
                    quit("Invalid number,Start the process again")
                check = str(input("Repeat phone number: "))

                if number == check:
                    print("""
                            1.GHS 10(30MB)
                            2.GHS 40 (70MB)
                            3.GHS 70 (100MB)
                                       """)
                    opt_3 = int(input("Choose your option: "))
                    if opt_3 == 1:
                        pin = int(input(f"You are buying GHS10 data bundle(30MB), Enter your pin to proceed: "))
                        if pin == main.passcode:
                            if 10 > main.balance:
                                print("Sorry, you have insufficient funds")
                                quit()
                            else:
                                new_balance = main.balance - 10
                                print(f"you have purchased and sent GHS10 airtime, your balance is GHS{new_balance}")
                                quit()

                    elif opt_3 == 2:
                        pin = int(input(f"You are buying GHS40 data bundle(70MB), Enter your pin to proceed: "))
                        if pin == main.passcode:
                            if 40 > main.balance:
                                print("Sorry, you have insufficient funds")
                                quit()
                            else:
                                new_balance = main.balance - 40
                                print(f"you have purchased and sent GHS40 airtime, your balance is GHS{new_balance}")
                                quit()

                    elif opt_3 == 3:
                        pin = int(input(f"You are buying GHS10 data bundle(70MB), Enter your pin to proceed: "))
                        if pin == main.passcode:
                            if 70 > main.balance:
                                print("Sorry, you have insufficient funds")
                                quit()
                            else:
                                new_balance = main.balance - 70
                                print(f"you have purchased and sent GHS70 airtime, your balance is GHS{new_balance}")
                                quit()
                else:
                    quit("Sorry, the numbers are not the same")


        elif opt_1 == 2:
            print("""
                    1. Buy for self
                    2. Buy for others
                        """)
            opt_2 = int(input("Choose your choice: "))
            if opt_2 == 1:
                print("""
                        How much would you want to buy?
                        1. 2.99 GHS = 8GB
                        2. 2 GHC = 4GB
                        3. 1 = 2GB                
                    """)
                opt_3 = int(input("Choose your choice: "))
                if opt_3 == 1:
                    pin = int(input(f"You are buying GHS2.99 data bundle(8GB), Enter your pin to proceed: "))
                    if pin == main.passcode:
                        if 10 > main.balance:
                            print("Sorry, you have insufficient funds")
                            quit()
                        else:
                            new_balance = main.balance - 2.99
                            print(f"you have purchased and sent GHS10 airtime, your balance is GHS{new_balance}")
                            quit()

                elif opt_3 == 2:
                    pin = int(input(f"You are buying GHS2 data bundle(4GB), Enter your pin to proceed: "))
                    if pin == main.passcode:
                        if 40 > main.balance:
                            print("Sorry, you have insufficient funds")
                            quit()
                        else:
                            new_balance = main.balance - 2
                            print(f"you have purchased and sent GHS40 airtime, your balance is GHS{new_balance}")
                            quit()

                elif opt_3 == 3:
                    pin = int(input(f"You are buying GHS1 data bundle(2GB), Enter your pin to proceed: "))
                    if pin == main.passcode:
                        if 70 > main.balance:
                            print("Sorry, you have insufficient funds")
                            quit()
                        else:
                            new_balance = main.balance - 2
                            print(f"you have purchased and sent GHS70 airtime, your balance is GHS{new_balance}")
                            quit()

                else:
                    quit("Invalid input!")


            elif opt_2 == 2:
                number = str(input("Enter phone number: "))
                if len(number) != 10:
                    quit("Invalid number,Start the process again")
                check = str(input("Repeat phone number: "))

                if number == check:
                    print("""
                            How much would you want to buy?
                            1. 2.99 GHS = 8GB
                            2. 2 GHC = 4GB
                            3. 1 = 2GB                
                            """)
                    opt_3 = int(input("Choose your option: "))
                    if opt_3 == 1:
                        pin = int(input(f"You are buying GHS2.99 data bundle(8GB), Enter your pin to proceed: "))
                        if pin == main.passcode:
                            if 10 > main.balance:
                                print("Sorry, you have insufficient funds")
                                quit()
                            else:
                                new_balance = main.balance - 2.99
                                print(f"you have purchased and sent GHS10 airtime, your balance is GHS{new_balance}")
                                quit()

                    elif opt_3 == 2:
                        pin = int(input(f"You are buying GHS2 data bundle(4GB), Enter your pin to proceed: "))
                        if pin == main.passcode:
                            if 40 > main.balance:
                                print("Sorry, you have insufficient funds")
                                quit()
                            else:
                                new_balance = main.balance - 2
                                print(f"you have purchased and sent GHS40 airtime, your balance is GHS{new_balance}")
                                quit()

                    elif opt_3 == 3:
                        pin = int(input(f"You are buying GHS1 data bundle(2GB), Enter your pin to proceed: "))
                        if pin == main.passcode:
                            if 70 > main.balance:
                                print("Sorry, you have insufficient funds")
                                quit()
                            else:
                                new_balance = main.balance - 2
                                print(f"you have purchased and sent GHS70 airtime, your balance is GHS{new_balance}")
                                quit()

                    else:
                        print("Invalid input!")
