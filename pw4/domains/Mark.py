import math
import numpy as np
from domains import Course as Cour
from domains import Student as Stu

class Mark_for_Student:
    def __init__(self):
        self.__student = {}
        self.__course = {}
        self.__mark = {}
        self.__GPA = {}

    def cal_GPA(self):
        for student_id in self.__mark.keys():
            total_mark = 0
            total_credit = 0

            for course_id in self.__mark.keys():
                total_mark = np.add(total_mark, self.__mark[student_id][course_id])
                total_credit = np.add(total_credit, self.__course[course_id].getCCredit())

            GPA_mark = np.divide(total_mark, total_credit)
            self.__GPA[student_id] = GPA_mark