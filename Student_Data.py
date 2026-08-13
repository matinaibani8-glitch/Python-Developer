import json
from getpass import getpass
student_Data = []

#FUNCTION START

def fun():  
    while True:
    
        print("========= ADMIN DASHBOARD ========")
    
        print("===== STUDENT MANAGEMENT SYSTEM =====")
    
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Average Marks")
        print("7. Topper")
        print("8. Save Data")
        print("9. Load Data Automatically")
        print("10. Logout")
    
        choice = int(input("Enter Choice :"))
    
        if choice == 1:
            roll_no = int(input("Enter Student Roll No."))
            name_student = input("Enter Student Name: ") 
            age_student = int(input("Enter Student Age: "))
            course_student = input("Enter Student Course: ")
            marks_student = int(input("Enter Student Marks: "))
            city_student = input("Enter Student City: ")
            phone_student = int(input("Enter Student Phone No.: "))
    
            student_Datas = {
                "Roll" : roll_no,
                "Name" : name_student,
                "Age" : age_student,
                "Course" : course_student,
                "Marks" : marks_student,
                "City" : city_student,
                "Phone" : phone_student
            }
    
            student_Data.append(student_Datas)
            print("-"*30)
            print("Student Data Added Successfully!")
    
        elif choice == 2:
            print("\n=====All Students=====")
    
            if len(student_Data) == 0:
                print("No Student Found!")
    
            else:
                for stu_data in student_Data:
                    print("-"*30)
                    print("Roll :", stu_data["Roll"])
                    print("Name :", stu_data["Name"])
                    print("Age :", stu_data["Age"])
                    print("Course :", stu_data["Course"])
                    print("Marks :", stu_data["Marks"])
                    print("City :",stu_data["City"])
                    print("Phone :",stu_data["Phone"])
    
        elif choice == 3:
            roll_us = int(input("Enter Search_Student Roll_No.: "))
    
            for stu_data in student_Data:
                if roll_us == stu_data["Roll"]:
                    print("Roll :", stu_data["Roll"])
                    print("Name :", stu_data["Name"])
                    print("Age :", stu_data["Age"])
                    print("Course :", stu_data["Course"])
                    print("Marks :", stu_data["Marks"])
                    print("-"*30)
                    break
                else:
                    print("!!!!!Student Not Found!!!!!")
    
        elif choice == 4:
            roll_us2 = int(input("Enter Student Roll No.: "))
            for roll_us1 in student_Data:
                if roll_us2 == roll_us1["Roll"]:
                    print("-----Student Has Been Found And Update Data!-----\nBut We Cannot Update Roll No.!")
                    name1 = input("Enter Student Name: ")
                    age1 = int(input("Enter Student Age: "))
                    course1 = input("Enter Course: ") 
                    Marks1 = int(input("Enter Student Marks: "))
                    city_student1 = input("Enter Student City: ")
                    phone_student1 = int(input("Enter Student Number: "))
                            
                    roll_us1["Name"] = name1
                    roll_us1["Age"] = age1
                    roll_us1["Course"] = course1
                    roll_us1["Marks"] = Marks1
                    roll_us1["City"] = city_student1
                    roll_us1["Phone"] = phone_student1
                            
                    print("-"*30)
                    print("Student Data Update Successfully!")
                    break           
    
            else:                
                print("!!!!!Student Not Found!!!!!")
    
        elif choice == 5:
            roll_us3 = int(input("Enter A Student Roll No.: "))
            for roll_us in student_Data:
                if roll_us3 == roll_us["Roll"]:
    
                    student_Data.remove(roll_us)
    
                    print("The Data Is Deleted!")
                    break
                        
                else:
                    print("Student Not Found!")
    
        elif choice == 6:
            if len(student_Data) == 0:
                print("Student Not Found!")
            else:
                total_Marks = 0
    
                for stu_data in student_Data:
                    total_Marks += stu_data["Marks"]
    
                    average = total_Marks / len(student_Data)
    
                    # print(len(student_Data))
                    print("The Student Average :",average)
    
        elif choice == 7:
            for stu_data in student_Data:
                if 90 <= stu_data["Marks"]:
                    print("The Topper is: ",stu_data["Name"])
    
    
        elif choice == 8:
            with open("Student_Data.json","w") as file:
                json.dump(student_Data,file, indent = 4)
    
            print("Data Saved Successfully!")
    
        elif choice == 9:
            try:
                with open("Student_Data.json","r") as file:
                    student_Data = json.load(file)
                    print("All Student Data Inserted Successfully!")
            except FileNotFoundError:
                student_Data = []
                print("Student Data Not Found!")
    
        elif choice == 10:
            print("Logout Successfully!")
            break

#FUNCTION END

#Program Start 

max_attempts = 3

for attempt in range(max_attempts):
    print("========= ADMIN LOGIN ========")
    admin = input("Enter Username: ")
    password = getpass("Enter PassWord: ")

    if admin == "Test" and password == "test@123":
        print("Login Successful! ✅")
        fun()
    else:
        print("Invalid Username and Password!")

        remaining = max_attempts - (attempt+1)

        if remaining > 0:
        
            print("Attempts Remaining: ",remaining)

        else: 
            print("Too Many Wrong Attempts!")
            print("Access Denied!")
    
