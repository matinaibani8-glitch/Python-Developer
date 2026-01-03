import datetime

many = 0

def men():

    user = input("Enter Username:")
    paas = input("Enter PassWord:")

    many = int(input("How Many Post Aplie:"))

    Employee = {} 
    for x in range(many):
        title = input("Enter Title: ")
        des = input("Enter Description: ")
        print("Your Date is Manually (1)Entered\n(2)Auto:")
        choice = int(input("Enter Your Choice:"))
        if choice == 2:
            date = datetime.datetime.now()
        elif choice == 1:
            date = int(input("Enter Date:"))
        Employee["Title"] = title
        Employee["Description"] = des
        Employee["Date"] = date

    for x in range(many):
        print("Employee Title is:",Employee["Title"])       
        print("Employee Description is:",Employee["Description"])
        print("Employee Date is:",Employee["Date"])       
men()