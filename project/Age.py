a = int(input("Enter Your Age: "))

if a>=18:
    print("You Are Eligible To Vote")
elif a<18 and a>0:
    print("You Are Not Eligible To Vote")
else:
    print("You Are Entered Negative Value")