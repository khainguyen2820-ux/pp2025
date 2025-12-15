import domains

def output(self):
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