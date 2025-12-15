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