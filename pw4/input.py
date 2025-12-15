import domains
import math

def add_student(self):
    student_name = input("enter name of student: ")
    student_id  = input("enter id of studen: ")
    while student_id in self.__student.keys():
        student_id = input("this student id already exist, enter new student id: ")
    DoB = input("enter student's DoB: ")
    student = domains.Student(student_id, student_name, DoB)
    domains.Mark.Mark_for_Student.__student[student_id] = student
    
def add_course(self):
    course_name = input("enter course name: ")
    while course_name in self.__course.values():
        course_name = input("already have this course, enter course name: ")
    course_id = input("enter course id: ")
    while course_id in self.__course.keys():
        course_id = input("already have this id, enter course id: ")
    course_credit = int(input("enter number of credit: "))
    course = domains.Course(course_name, course_id, course_credit)
    domains.Mark.Mark_for_Student.__course[course_id] = course

def set_mark(self):
    for course_id in self.__course.keys():
        for student_id in self.__student.keys():
            mark = int(input(f"Enter mark of course {domains.Mark.Mark_for_Student.__course[course_id]} for student {domains.Mark.Mark_for_Student.__student[student_id]}: "))
            mark = math.floor(mark)
            domains.Mark.Mark_for_Student.__mark[student_id][course_id] = mark