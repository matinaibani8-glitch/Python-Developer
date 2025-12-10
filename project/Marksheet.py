sub1 = int(input("Enter A Sub1 Mark: "))
sub2 = int(input("Enter A Sub2 Mark: "))
sub3 = int(input("Enter A Sub3 Mark: "))
sub4 = int(input("Enter A Sub4 Mark: "))
sub5 = int(input("Enter A Sub5 Mark: "))
sub6 = int(input("Enter A Sub6 Mark: "))

if sub1<=40 or sub2<=40 or sub3<=40 or sub4<=40 or sub5<=40 or sub6<=40:
    print("FAIL")

total = sub1+sub2+sub3+sub4+sub5+sub6
print(f"Your Total Marks is:{total} Outof 600")

pr = total/6

if pr>=90 and pr<=100:
    print("A Grade Your Marks is:",pr)
elif pr>=80 and pr<=89:
    print("B Grade Your Marks is:",pr)
elif pr>=70 and pr<=79:
    print("C Grade Your Marks is:",pr)
elif pr>=60 and pr<=69:
    print("D Grade Your Marks is:",pr)
elif pr>=50 and pr<=59:
    print("E Grade Your Marks is:",pr)

