import momo_user_1
import transfer_money
import wallet
import airtime_bundles

print("Welcome to the Menu")
passcode = 1234
balance = 100
while True:
    print(""" 
          1. Transfer Money
          3. Airtime & Bundle
          6. My Wallet """
          )
    option_1 = int(input("Choose your option: "))

    if option_1 == 1:
        print("Transfer Money")
        transfer_money.transfer_money()

    elif option_1 == 3:
        print("Airtime & Bundles")
        airtime_bundles.airtime_bundles()

    elif option_1 == 6:
        print("Wallet")
        wallet.wallet()

    else:
        quit("Invalid input,Start the program again")
