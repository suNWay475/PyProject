class Student:
    def __init__(self ,name , grade ):
        self.name = name
        self.__grade = grade
    def get_grade(self):
        print(f"{self.__grade}")
    
    def set_grade(self , grade):
        if 1 <=  grade <= 12:
            self.__grade = grade 
            print(f'Оцінка змінена на {grade}')
        else:
            print('Оцінка має бути від 1 до 12')


student = Student('Віталій', 10)
student.get_grade()          # 10
student.set_grade(12)        # Оцінка змінена на 12
student.set_grade(15)        # Оцінка має бути від 1 до 12
student.get_grade()
