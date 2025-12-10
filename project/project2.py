#Ragistration form
Name = input("Enter Your Name: ")
if Name.isalpha():
    email = input("Enter Your Email In Small Case: ")
    if email.islower():
        Number = input("Enter Your Mobil Number: ")
        if Number.isdigit():
            print("This is The Valid Number")
            password = input("Enter Your Min-8 and Max-12 PassWord: ")
            if 8 <=  len(password) <= 12:
                confirmpass = input("Enter Confirm PassWord: ")
                if password == confirmpass:
                    print("Login Is SuccessFul")
                else:
                    print("Your Ragistration Form is Fail!")
            else:
                print("This is Not Valid Index PassWord!")
                print("Your Ragistration Form is Fail!")
        else:
            print("Enter Valid Phone Number!")
            print("Your Ragistration Form is Fail!")
    else:
        print("This is Not Valid Email!")
        print("Your Ragistration Form is Fail!")
else:
    print("Your Name is Not Valid")        
    print("Your Ragistration Form is Fail!")
