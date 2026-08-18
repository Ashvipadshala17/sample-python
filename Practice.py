# Project-1 : Student Result Management System
# name = input("Enter Student name: ")

# marks = []
# marks.append(int(input("Enter English subject marks: ")))
# marks.append(int(input("Enter Hindi subject marks: ")))
# marks.append(int(input("Enter Gujarati subject marks: ")))
# marks.append(int(input("Enter Science subject marks: ")))
# marks.append(int(input("Enter Social Science subject marks: ")))

# marks = tuple(marks)

# total = sum(marks)
# average = total / 5

# if average >= 75:
#     grade = 'A'
# elif average >= 60:
#     grade = 'B'
# elif average >= 50:
#     grade = "C"
# else:
#     grade = "Fail"

# Marks = set(marks)

# Passed = average >= 50

# result = {
#       "name" : name, 
#       "marks" : marks,
#       "total" : total,
#       "average" : average,
#       "grade" : grade
#  }

# print(result)
# print("Marks:", Marks)
# print('Passed:', Passed)


# Project - 2  : University Student Record Management System

student1 = {
    "Student ID" : 1,
    "Name" : "Ashvi",
    "Age" : 20,
    "Gender" : "Female",
    "Department" : "IT",
    "Semester" : 7,
    "City" : "Ahmedabad",
    "CGPA" : 8.5,
    "Attendance" : 85,
    "Fee Status" : "paid",
    "Scholarship Status" : "Approved",
    "Scholarship Amount" : 30000,
    "Hostel Distance" : 25,
    "Special Category" : "false",
    "Library Fine" : 0,
    "Club Name" : "Dance club",
}
student2 = {
    "Student ID" : 2,
    "Name" : "Moxa",
    "Age" : 20,
    "Gender" : "Female",
    "Department" : "IT",
    "Semester" : 7,
    "City" : "Nadiad",
    "CGPA" : 9.0,
    "Attendance" : 85,
    "Fee Status" : "paid",
    "Scholarship Status" : "Approved",
    "Scholarship Amount" : 30000,
    "Hostel Distance" : 0,
    "Special Category" : "false",
    "Library Fine" : 0,
    "Club Name" : "Sports club",
}
student3 = {
    "Student ID" : 3,
    "Name" : "Ishaan",
    "Age" : 20,
    "Gender" : "male",
    "Department" : "BCA",
    "Semester" : 7,
    "City" : "Ahmedabad",
    "CGPA" : 8.0,
    "Attendance" : 70,
    "Fee Status" : "paid",
    "Scholarship Status" : "Not Approved",
    "Scholarship Amount" : 30000,
    "Hostel Distance" : 25,
    "Special Category" : "false",
    "Library Fine" : 200,
    "Club Name" : "Dance club",
}
student4 = {
    "Student ID" : 4,
    "Name" : "Rudra",
    "Age" : 19,
    "Gender" : "male",
    "Department" : "BCA",
    "Semester" : 5,
    "City" : "Nadiad",
    "CGPA" : 7.0,
    "Attendance" : 75,
    "Fee Status" : "paid",
    "Scholarship Status" : "Approved",
    "Scholarship Amount" : 30000,
    "Hostel Distance" : 35,
    "Special Category" : "false",
    "Library Fine" : 500,
    "Club Name" : "Coding club",
}
student5 = {
    "Student ID" : 5,
    "Name" : "Manan",
    "Age" : 21,
    "Gender" : "male",
    "Department" : "IT",
    "Semester" : 8,
    "City" : "Rajkot",
    "CGPA" : 8.0,
    "Attendance" : 95,
    "Fee Status" : "paid",
    "Scholarship Status" : "Approved",
    "Scholarship Amount" : 30000,
    "Hostel Distance" : 25,
    "Special Category" : "false",
    "Library Fine" : 0,
    "Club Name" : "Coding club",
}

Students = [student1, student2, student3, student4, student5]

Department = ("IT", "BCA")

Clubs = {"Dance club", "Sports club", "Coding club"}

# Section A – Student Information

print("\nFirst student: ")
print(student1)
print("\nLast student: ")
print(student5)
print("\nstudent 2 Name, Department, Semester: ")
print(student2["Name"])
print(student2["Department"])
print(student2["Semester"])
print("\nstudent 3 Department, Semester, CGPA, Attendance: ")
print("Department: ", student3["Department"])
print("Semester: ", student3["Semester"])
print("CGPA: ", student3["CGPA"])
print("Attendance: ", student3["Attendance"])
print("\nstudent 5 Scholarship Status, Scholarship Amount: ")
print("Scholarship Status: ", student5["Scholarship Status"])
print("Scholarship Amount: ", student5["Scholarship Amount"])


# Section B – Conditional Statements

print("\nis student1 in IT?")
if student1["Department"] == "IT": 
    print("Yes")
else :
    print("No")
print("\nhas student2 CGPA greater than 9.0?")
if student2["CGPA"] == 9.0:
    print("Yes")
else : 
    print("No")
print("\nhas student3 Attendance os at least 75%?")
if student3["Attendance"] == 75:
    print("Yes")
else : 
    print("No")
print("\nhas student4 paid the University fees?")
if student4["Fee Status"] == "paid":
    print("Yes")
else : 
    print("No")
print("\nhas student5 an approved scholarship?")
if student5["Scholarship Status"] == "Approved":
    print("Yes")
else : 
    print("No")

# Section C – Eligibility

print("\nis student1 eligible for an internship?")
if student1["CGPA"] >= 8.0:
    print("Eligible")
else : 
    print("Not Eligible")
print("\nis student2 eligible for an Placement?")
if student2["CGPA"] >= 7.5 and student1["Attendance"] >= 80 and student1["Fee Status"] == "paid" :
    print("Eligible")
else : 
    print("Not Eligible")
print("\nis student3 eligible for Scholarship?")
if student3["CGPA"] >= 8.5 and student1["Attendance"] >= 85 and student1["Fee Status"] == "paid" :
    print("Eligible")
else : 
    print("Not Eligible")
print("\nis student4 eligible for Hostel accommodation?")
if student4["Hostel Distance"] > 30 :
    print("Eligible")
else : 
    print("Not Eligible")
print("\ncan student5 download the hall ticket?")
if student5["Fee Status"] == "paid" :
    print("Eligible")
else : 
    print("Not Eligible")

# Section D – Membership & Comparison

print("\nis BCA in Department Tuple?")

if "BCA" in Department:
    print("Yes")
else:
    print("No")
print("\nis Coding club in Club set?")

if "Coding club" in Clubs:
    print("Yes")
else:
    print("No")
print("\nComapare the CGPA of student1 & student2")
if student1["CGPA"] > student2["CGPA"]:
    print("Student 1 has higher CGPA")
elif student1["CGPA"] < student2["CGPA"]:
    print("Student 2 has higher CGPA")
else:
    print("Both have same CGPA")
print("\nComapre the Attendance of student3 and student5")
if student3["Attendance"] > student5["Attendance"]:
    print("Student 3 has higher attendance")
elif student3["Attendance"] < student5["Attendance"]:
    print("Student 5 has higher attendance")
else:
    print("Both have same attendance")
print("\nStudent 1 and Student 2 Same Department?")
if student1["Department"] == student2["Department"]:
    print("Yes")
else:
    print("No")

# Section E – Academic Evaluation

print("\nStudent 3 Academic Grade:")
if student3["CGPA"] >= 9 and student3["Attendance"] >= 85:
    print("Excellent")
elif student3["CGPA"] >= 8 and student3["Attendance"] >= 75:
    print("Good")
else:
    print("Needs Improvement")
print("\nIs Student 4 Final Year?")

if student4["Semester"] == 8:
    print("Yes")
else:
    print("No")
print("\nIs Student 5 Adult?")

if student5["Age"] >= 18:
    print("Yes")
else:
    print("No")
print("\nIs Student 1 Library Fine?")

if student1["Library Fine"] > 0:
    print("Pending Fine")
else:
    print("No Fine")
print("\nStudent 5 University Excellence Award:")

if student5["CGPA"] >= 9 and student5["Attendance"] >= 80 and student5["Fee Status"] == "paid":
    print("Qualified")
else:
    print("Not Qualified")









