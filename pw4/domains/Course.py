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