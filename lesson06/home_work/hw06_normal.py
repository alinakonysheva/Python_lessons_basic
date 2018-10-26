# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# ---------------------------------------------------------------
# Учителя, родители и дети -- люди с ФИО, поэтому делаем класс,
# People, от которого будут дочерние классы


class People:
    def __init__(self, name, surname, middlename):
        self.name = name
        self.surname = surname
        self.middlename = middlename

# класс для учителей


class Teacher(People):
    def __init__(self, name, surname, middlename, subject):
        People.__init__(self, name, surname, middlename)
        self.subject = subject

# для родителей


class Parent(People):
    def __init__(self, name, surname, middlename):
        People.__init__(self, name, surname, middlename)

# класс для учеников


class Student(People):
    def __init__(self, name, surname, middlename, dad, mom):
        People.__init__(self, name, surname, middlename)
        self.dad = dad
        self.mom = mom

    def get_name(self):
        return [self.surname, self.name, self.middlename]

# класс для класса в школе


class Group:
    def __init__(self, number):
        self.number = number
        self.students = set()
        self.teachers = set()

    def get_number(self):
        return self.number

    def add_teacher(self, teacher):
        self.teachers.add(teacher)

    def add_student(self, student):
        self.students.add(student)

    def get_students(self):
        return self.students


class Subject:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self):
        self.groups = set()

    def add_group(self, group):
        self.groups.add(group)

    def get_all_classes(self):
        groups = []
        for g in self.groups:
            groups.append(g.get_number())
        return groups

    def get_students_classes(self, group):
        for g in self.groups:
            if g == group:
                return g.get_students()


school = School()

mom1 = Parent("MomName1", "MomSurname1", "MomMid1")
dad1 = Parent("DadName1", "DadSurname1", "DadMid1")
stud1 = Student("DadName1", "DadSurname1", "DadMid1", mom1, dad1)

mom2 = Parent("MomName2", "MomSurname2", "MomMid2")
dad2 = Parent("DadName2", "DadSurname2", "DadMid2")
stud2 = Student("DadName2", "DadSurname2", "DadMid2", mom2, dad2)

mom3 = Parent("MomName3", "MomSurname3", "MomMid3")
dad3 = Parent("DadName3", "DadSurname3", "DadMid3")
stud3 = Student("DadName3", "DadSurname3", "DadMid3", mom3, dad3)

mom4 = Parent("MomName4", "MomSurname4", "MomMid4")
dad4 = Parent("DadName4", "DadSurname4", "DadMid4")
stud4 = Student("DadName4", "DadSurname4", "DadMid4", mom4, dad4)

subjMath = Subject("Math")
teacher1 = Teacher("TName1", "TSurname1", "TMid1", subjMath)

subjPhysics = Subject("Physics")
teacher2 = Teacher("TName2", "TSurname2", "TMid2", subjPhysics)

subjChemistry = Subject("Chemistry")
teacher3 = Teacher("TName3", "TSurname3", "TMid3", subjChemistry)

group1 = Group("Class#1")
group1.add_student(stud1)
group1.add_teacher(teacher1)
group1.add_student(stud2)
group1.add_teacher(teacher2)

group2 = Group("Class#2")
group2.add_student(stud3)
group2.add_teacher(teacher1)
group2.add_student(stud4)
group2.add_teacher(teacher3)

school_1 = School()
school_1.add_group(group1)
school_1.add_group(group2)


# список всех классов
print(school_1.get_all_classes())

# список учеников, выводится как список Фамилий
for s in school.get_students_classes(group1):
    print(s.get_name())

# Получить список всех предметов указанного ученика

# Узнать ФИО родителей указанного ученика

# Получить список всех Учителей, преподающих в указанном классе