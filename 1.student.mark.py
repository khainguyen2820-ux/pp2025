student = {}
course = {}
mark = {}

number_of_student = int(input("enter number of student"))
number_of_course = int(input("enter number of course"))

for _ in range(number_of_student):
    id = input("enter student id:")
    name = input("enter student's name:")
    dob = input("enter date of birth (dd/mm/yyyy):")

    student[id] = {
        "name" : name,
        "dob" : dob
    }

for _ in range(number_of_course):
    course_id = input("enter course id:")
    course_name = input("enter course name:")

    course[course_id] = {
        "course_name" : course_name,
    }

course_id = input("enter course id to mark:")
if course_id in course:
    for id in student:
        mark = float(input("enter mark for student {id}:"))
        mark[id][course_id] = mark
else:
    print("no course found")

print(student)
print(course)
print(mark)