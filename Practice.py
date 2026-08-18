# Project-1 : Student Result Management System
name = input("Enter Student name: ")

marks = []
English = int(input("Enter English subject marks: "))
if English > 100 or English < 0:
    int("")
else:
    marks.append(English)
Hindi = int(input("Enter Hindi subject marks: "))
if Hindi > 100 or Hindi < 0:
    int("")
else:
    marks.append(Hindi)
Gujarati = int(input("Enter Gujarati subject marks: "))
if Gujarati > 100 or Gujarati < 0:
    int("")
else:
    marks.append(Gujarati)
Science = int(input("Enter Science subject marks: "))
if Science > 100 or Science < 0:
    int("")
else:
    marks.append(Science)
SocialScience = int(input("Enter Social Science subject marks: "))
if SocialScience > 100 or SocialScience < 0:
    int("")
else:
    marks.append(SocialScience)


marks = tuple(marks)
total = sum(marks)
average = total / 5

if average >= 75:
    grade = 'A'
elif average >= 60:
    grade = 'B'
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

Marks = set(marks)

Passed = average >= 50

result = {
      "name" : name, 
      "marks" : marks,
      "total" : total,
      "average" : average,
      "grade" : grade
 }

print(result)
print("Marks:", Marks)
print('Passed:', Passed)




# Project - 2  : University Student Record Management System

# students = []


# student1 = {}
# student1["ID"] = int(input("enter student1 ID: "))
# student1["name"] = str(input("enter student1 name: "))
# student1["age"] = float(input("enter student1 age: "))
# student1["gender"] = str(input("enter student1 gender: "))
# student1["department"] = str(input("enter student1 department: "))
# student1["semester"] = int(input("enter student1 semester: "))
# student1["city"] = str(input("enter student1 city: "))
# student1["CGPA"] = float(input("enter student1 CGPA: "))
# student1["attendance"] = float(input("enter student1 attendance: "))
# student1["fee status"] = str(input("enter student1 fee status: "))
# student1["scholarship status"] = str(input("enter student1 scholarship status: "))
# student1["scholarship amount"] = int(input("enter student1 scholarship amount: "))
# student1["hostel distance"] = int(input("enter student1 hostel distance: "))
# student1["library fine"] = int(input("enter student1 library fine: "))
# student1["club name"] = str(input("enter student1 club name: "))
# students.append(student1)

# student2 = {}
# student2["ID"] = int(input("enter student2 ID: "))
# student2["name"] = str(input("enter student2 name: "))
# student2["age"] = float(input("enter student2 age: "))
# student2["gender"] = str(input("enter student2 gender: "))
# student2["department"] = str(input("enter student2 department: "))
# student2["semester"] = int(input("enter student2 semester: "))
# student2["city"] = str(input("enter student2 city: "))
# student2["CGPA"] = float(input("enter student2 CGPA: "))
# student2["attendance"] = float(input("enter student2 attendance: "))
# student2["fee status"] = str(input("enter student2 fee status: "))
# student2["scholarship status"] = str(input("enter student2 scholarship status: "))
# student2["scholarship amount"] = int(input("enter student2 scholarship amount: "))
# student2["hostel distance"] = int(input("enter student2 hostel distance: "))
# student2["library fine"] = int(input("enter student2 library fine: "))
# student2["club name"] = str(input("enter student2 club name: "))
# students.append(student2)


# student3 = {}
# student3["ID"] = int(input("enter student3 ID: "))
# student3["name"] = str(input("enter student3 name: "))
# student3["age"] = float(input("enter student3 age: "))
# student3["gender"] = str(input("enter student3 gender: "))
# student3["department"] = str(input("enter student3 department: "))
# student3["semester"] = int(input("enter student3 semester: "))
# student3["city"] = str(input("enter student3 city: "))
# student3["CGPA"] = float(input("enter student3 CGPA: "))
# student3["attendance"] = float(input("enter student3 attendance: "))
# student3["fee status"] = str(input("enter student3 fee status: "))
# student3["scholarship status"] = str(input("enter student3 scholarship status: "))
# student3["scholarship amount"] = int(input("enter student3 scholarship amount: "))
# student3["hostel distance"] = int(input("enter student3 hostel distance: "))
# student3["library fine"] = int(input("enter student3 library fine: "))
# student3["club name"] = str(input("enter student3 club name: "))
# students.append(student3)

# student4 = {}
# student4["ID"] = int(input("enter student4 ID: "))
# student4["name"] = str(input("enter student4 name: "))
# student4["age"] = float(input("enter student4 age: "))
# student4["gender"] = str(input("enter student4 gender: "))
# student4["department"] = str(input("enter student4 department: "))
# student4["semester"] = int(input("enter student4 semester: "))
# student4["city"] = str(input("enter student4 city: "))
# student4["CGPA"] = float(input("enter student4 CGPA: "))
# student4["attendance"] = float(input("enter student4 attendance: "))
# student4["fee status"] = str(input("enter student4 fee status: "))
# student4["scholarship status"] = str(input("enter student4 scholarship status: "))
# student4["scholarship amount"] = int(input("enter student4 scholarship amount: "))
# student4["hostel distance"] = int(input("enter student4 hostel distance: "))
# student4["library fine"] = int(input("enter student4 library fine: "))
# student4["club name"] = str(input("enter student4 club name: "))
# students.append(student4)

# student5 = {}
# student5["ID"] = int(input("enter student5 ID: "))
# student5["name"] = str(input("enter student5 name: "))
# student5["age"] = float(input("enter student5 age: "))
# student5["gender"] = str(input("enter student5 gender: "))
# student5["department"] = str(input("enter student5 department: "))
# student5["semester"] = int(input("enter student5 semester: "))
# student5["city"] = str(input("enter student5 city: "))
# student5["CGPA"] = float(input("enter student5 CGPA: "))
# student5["attendance"] = float(input("enter student5 attendance: "))
# student5["fee status"] = str(input("enter student5 fee status: "))
# student5["scholarship status"] = str(input("enter student5 scholarship status: "))
# student5["scholarship amount"] = int(input("enter student5 scholarship amount: "))
# student5["hostel distance"] = int(input("enter student5 hostel distance: "))
# student5["library fine"] = int(input("enter student5 library fine: "))
# student5["club name"] = str(input("enter student5 club name: "))
# students.append(student5)

# Students = [student1, student2, student3, student4, student5]

# department = ("IT", "BCA")

# clubs = {"Dance club", "Sports club", "Coding club"}

# # Section A – Student Information

# print("\nFirst student: ")
# print(student1)
# print("\nLast student: ")
# print(student5)
# print("\nstudent 2 Name, Department, Semester: ")
# print(student2["name"])
# print(student2["department"])
# print(student2["semester"])
# print("\nstudent 3 Department, Semester, CGPA, Attendance: ")
# print("Department: ", student3["department"])
# print("Semester: ", student3["semester"])
# print("CGPA: ", student3["CGPA"])
# print("Attendance: ", student3["attendance"])
# print("\nstudent 5 Scholarship Status, Scholarship Amount: ")
# print("scholarship status: ", student5["scholarship status"])
# print("scholarship amount: ", student5["scholarship amount"])


# # Section B – Conditional Statements

# print("\nis student1 in IT?")
# if student1["department"] == "IT": 
#     print("Yes")
# else :
#     print("No")
# print("\nhas student2 CGPA greater than 9.0?")
# if student2["CGPA"] == 9.0:
#     print("Yes")
# else : 
#     print("No")
# print("\nhas student3 Attendance os at least 75%?")
# if student3["attendance"] == 75:
#     print("Yes")
# else : 
#     print("No")
# print("\nhas student4 paid the University fees?")
# if student4["fee status"] == "paid":
#     print("Yes")
# else : 
#     print("No")
# print("\nhas student5 an approved scholarship?")
# if student5["scholarship status"] == "approved":
#     print("Yes")
# else : 
#     print("No")

# # Section C – Eligibility

# print("\nis student1 eligible for an internship?")
# if student1["CGPA"] >= 8.0:
#     print("Eligible")
# else : 
#     print("Not Eligible")
# print("\nis student2 eligible for an Placement?")
# if student2["CGPA"] >= 7.5 and student1["attendance"] >= 80 and student1["fee status"] == "paid" :
#     print("Eligible")
# else : 
#     print("Not Eligible")
# print("\nis student3 eligible for Scholarship?")
# if student3["CGPA"] >= 8.5 and student1["attendance"] >= 85 and student1["fee status"] == "paid" :
#     print("Eligible")
# else : 
#     print("Not Eligible")
# print("\nis student4 eligible for Hostel accommodation?")
# if student4["hostel distance"] > 30 :
#     print("Eligible")
# else : 
#     print("Not Eligible")
# print("\ncan student5 download the hall ticket?")
# if student5["fee status"] == "paid" :
#     print("Eligible")
# else : 
#     print("Not Eligible")

# # Section D – Membership & Comparison

# print("\nis BCA in Department Tuple?")

# if "BCA" in department:
#     print("Yes")
# else:
#     print("No")
# print("\nis Coding club in Club set?")

# if "coding club" in clubs:
#     print("Yes")
# else:
#     print("No")
# print("\nComapare the CGPA of student1 & student2")
# if student1["CGPA"] > student2["CGPA"]:
#     print("Student 1 has higher CGPA")
# elif student1["CGPA"] < student2["CGPA"]:
#     print("Student 2 has higher CGPA")
# else:
#     print("Both have same CGPA")
# print("\nComapre the Attendance of student3 and student5")
# if student3["attendance"] > student5["attendance"]:
#     print("Student 3 has higher attendance")
# elif student3["attendance"] < student5["attendance"]:
#     print("Student 5 has higher attendance")
# else:
#     print("Both have same attendance")
# print("\nStudent 1 and Student 2 Same Department?")
# if student1["department"] == student2["department"]:
#     print("Yes")
# else:
#     print("No")

# # Section E – Academic Evaluation

# print("\nStudent 3 Academic Grade:")
# if student3["CGPA"] >= 9 and student3["attendance"] >= 85:
#     print("Excellent")
# elif student3["CGPA"] >= 8 and student3["attendance"] >= 75:
#     print("Good")
# else:
#     print("Needs Improvement")
# print("\nIs Student 4 Final Year?")

# if student4["semester"] == 8:
#     print("Yes")
# else:
#     print("No")
# print("\nIs Student 5 Adult?")

# if student5["age"] >= 18:
#     print("Yes")
# else:
#     print("No")
# print("\nIs Student 1 Library Fine?")

# if student1["library fine"] > 0:
#     print("Pending Fine")
# else:
#     print("No Fine")
# print("\nStudent 5 University Excellence Award:")

# if student5["CGPA"] >= 9 and student5["attendance"] >= 80 and student5["fee status"] == "paid":
#     print("Qualified")
# else:
#     print("Not Qualified")


  