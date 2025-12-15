from domains import Mark
import output
import input

def main():
    system = Mark.Mark_for_Student()
    number_of_stu = input("enter number of student")
    for _ in range(number_of_stu):
        input.add_student(system)
    
    number_of_cour = input("enter number of student")
    for _ in range(number_of_cour):
        input.add_course(system)
    
    output.output(system)