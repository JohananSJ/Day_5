students = []
count = int(input("Enter number of students: "))
for i in range(count):
    print(f"\nEnter details for Student {i + 1}")
    student = {}
    student["name"] = input("Enter student name: ")
    student["age"] = input("Enter student age: ")
    student["course"] = input("Enter course name: ")
    students.append(student)
print("\n========== Student Records ==========")
for i, student in enumerate(students, start=1):
    print(f"\nStudent {i}")
    print("-------------------")
    print("Name   :", student["name"])
    print("Age    :", student["age"])
    print("Course :", student["course"])

