print("-----Welcome To ATM-----")

amount = int(input("Enter Amount: "))

if amount >= 500:
    print("Withdraw Successfull")
elif amount < 500:
    print("Enter Valid Amount")