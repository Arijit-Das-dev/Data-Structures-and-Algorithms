from rich import print

total = 0

while True:

    print()
    print("="*40)
    print("ENTER YOUR CHOICE")

    ask_user = input("""
    1. DEPOSIT [Type 1]
    2. WITHDRAW [Type 2]
    3. CHECK BALANCE [Type 3] 
    = """)

    ask_user = int(ask_user)

    if ask_user == 1:

        print("\n1. DEPOSIT MONEY")
        deposit = int(input("Enter amount : "))
        total += deposit
        
        print(f"DEPOSITED AMOUNT : {deposit}")
        print(f"BALANCE : {total}")
        print("="*30)

    elif ask_user == 2:

        print("\n2. WITHDRAW MONEY\n")
        withdraw = int(input("Enter amount : "))

        if total == 0:
            print("Money can not be withdrawled !!!")
            print(f"BALANCE : {total}")

        elif withdraw <= total:
            total -= withdraw
            print(f"WITHDRAWLED AMOUNT : {withdraw}")
            print(f"BALANCE : {total}")
        
    elif ask_user == 3:

        print("\n3. BALANCE")
        print(f"BALANCE : {total}")