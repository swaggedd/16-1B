class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def __str__(self):
        pass

class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study
    def study(self):
        print(f'Ученик {self.name} учится в {self.group_where_study}')
    def __str__(self):
        return f'Ученик: {self.name}, Email: {self.email}, Номер: {self.phone}, ID: {self.student_id}, Группа: {self.group_where_study}'

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach
    def teach(self):
        print(f'Учитель {self.name} преподает в группе {self.group_where_teach}')
    def __str__(self):
        return f'Учитель: {self.name}, Email: {self.email}, Номер: {self.phone}, ID: {self.teacher_id}, Группа: {self.group_where_teach}'

class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id
    def create_group(self):
        print("Создана новая группа")
    def __str__(self):
        return f'Админ: {self.name}, Email: {self.email}, Номер: {self.phone}, ID: {self.admin_id}'
        
class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)
    def __str__(self):
        return f'Ментор: {self.name}, Email: {self.email}, Номер: {self.phone}, ID ученика: {self.student_id}, Группа в которой учится: {self.group_where_study}, ID учителя: {self.teacher_id}, Группа в которой преподает: {self.group_where_teach}'
    
student1 = Student("Rustam", "rustam22@gmail.com", "0700321231", "12345", "16-1B")
teacher1 = Teacher("Syimyk", "syimyk123@gmail.com", "0500500500", "67890", "16-1b")
admin1 = Admin("admin", "admin@gmail.com", "0700700700", "54321")

print(student1)
print(teacher1)
print(admin1)
student1.study()
teacher1.teach()
admin1.create_group()

mentor1 = Mentor("Nurai", "nurai3312@gmail.com", "0555123321", "12345", "16-1B", "67890", "16-1B")
print(mentor1)


