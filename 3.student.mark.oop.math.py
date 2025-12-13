import math
import numpy as np

class Student:
    def __init__(self, student_id, student_name, DoB):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__DoB = DoB
    
    def getSID(self):
        return self.__student_id
    
    def getSName(self):
        return self.__student_name
    
    def getSDoB(self):
        return self.__DoB
    
    def setSName(self, student_name):
        self.__student_name = student_name

    def setSID(self, student_ID):
        self.__student_id = student_ID

    def setSDoB(self, DoB):
        self.__DoB = DoB
    
    def __student_str__(self):
        return f"{self.__student_name}, id: {self.__student_id}, date of birth: {self.__DoB}"
    
class Course:
    def __init__(self, course_name, course_id, course_credit):
        self.__course_name = course_name
        self.__course_id = course_id
        self.__course_credit = course_credit

    def getCid(self):
        return self.__course_id
    
    def getCName(self):
        return self.__course_name
    
    def getCCredit(self):
        return self.__course_credit
    
    def setCName(self, course_name):
        self.__course_name = course_name
    
    def setCID(self, course_id):
        self.__course_id = course_id

    def setCCredit(self, course_credit):
        self.__course_credit = course_credit
    
    def __course_str__(self):
        return f"{self.__course_name} id: {self.__course_id}, number of credit: {self.__course_credit}"

class Mark_for_Student:
    def __init__(self):
        self.__student = {}
        self.__course = {}
        self.__mark = {}
        self.__GPA = {}

    def add_student(self):
        student_name = input("enter name of student: ")
        student_id  = input("enter id of studen: ")
        while student_id in self.__student.keys():
            student_id = input("this student id already exist, enter new student id: ")
        DoB = input("enter student's DoB: ")
        student = Student(student_id, student_name, DoB)
        self.__student[student_id] = student
    
    def add_course(self):
        course_name = input("enter course name: ")
        while course_name in self.__course.values():
            course_name = input("already have this course, enter course name: ")
        course_id = input("enter course id: ")
        while course_id in self.__course.keys():
            course_id = input("already have this id, enter course id: ")
        course_credit = int(input("enter number of credit: "))
        course = Course(course_name, course_id, course_credit)
        self.__course[course_id] = course

    def set_mark(self):
        for course_id in self.__course.keys():
            for student_id in self.__student.keys():
                mark = int(input(f"Enter mark of course {self.__course[course_id]} for student {self.__student[student_id]}: "))
                mark = math.floor(mark)
                self.__mark[student_id][course_id] = mark

    def cal_GPA(self):
        for student_id in self.__mark.keys():
            total_mark = 0
            total_credit = 0

            for course_id in self.__mark.keys():
                total_mark = np.add(total_mark, self.__mark[student_id][course_id])
                total_credit = np.add(total_credit, self.__course[course_id].getCCredit())

            GPA_mark = np.divide(total_mark, total_credit)
            self.__GPA[student_id] = GPA_mark

    def show_data(self):
        print("\n Student:")
        for student in self.__student.values():
            print(student)

        print("\n Course:")
        for course in self.__course.values():
            print(course)

        print("\n Marks:")
        for student_id in self.__marks.items():
            print(f"Student id {self.__student[student_id].getSID}: \n")
            for course_id in self.__mark.item():
                print(f"Course id {self.__course[course_id].getCID} mark: {self.__mark[student_id][course_id]} \n")

            print(f"Average GPA: {self.__GPA[student_id]}")

system = Mark_for_Student()

NumOfStudents = int(input("Enter number of students: "))
for _ in range(NumOfStudents):
    system.add_student()

NumOfCourses = int(input("Enter number of courses: "))
for _ in range(NumOfCourses):
    system.add_course()

system.set_mark()
system.cal_GPA()
system.show_data()