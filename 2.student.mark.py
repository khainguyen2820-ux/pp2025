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
    def __init__(self, course_name, course_id):
        self.__course_name = course_name
        self.__course_id = course_id

    def getCid(self):
        return self.__course_id
    
    def getCName(self):
        return self.__course_name
    
    def setCName(self, course_name):
        self.__course_name = course_name
    
    def setCID(self, course_id):
        self.__course_id = course_id
    
    def __course_str__(self):
        return f"{self.__course_name} id: {self.__course_id}"

class University:
    def __init__(self):
        self.__student = {}
        self.__course = {}
        self.__mark = {}

    def add_student(self):
        student_name = input("enter name of student")
        student_id  = input("enter id of student")
        DoB = input("enter DoB")
        student = Student(student_id, student_name, DoB)
        self.student[student_id] = student
    
    def add_course(self):
        course_name = input("enter course name")
        course_id = input("enter course id")
        course = Course(course_name, course_id)
        self.course[course_id] = course

    def set_mark(self):
        course_id = input("enter course id to input mark")
        if course_id not in self.course:
            print("course not found")
            return
        
        student_id = input("enter student id to input mark")
        if student_id not in self.student:
            print("student not found")
            return
        
        mark = input("input mark:")
        self.mark[course_id][student_id] = mark

    def show_data(self):
        print("\n Student:")
        for student in self.__student.values():
            print(student)
        print("\n Course:")
        for course in self.__course.values():
            print(course)
        print("\n Marks:")
        for cid, mark_data in self.__marks.items():
            print(f"Course: {self.__course[cid].getCName()}")
            for sid, mark in mark_data.items():
                print(f"  Student {self.__studens[sid].getSName()}: {mark}")

system = University()

NumOfStudents = int(input("Enter number of students: "))
for _ in range(NumOfStudents):
    system.add_student()

NumOfCourses = int(input("Enter number of courses: "))
for _ in range(NumOfCourses):
    system.add_course()

system.input_mark()
system.show_data()