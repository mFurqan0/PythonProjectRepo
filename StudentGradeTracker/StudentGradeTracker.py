class Student:
    def __init__(self,name,id):
        self.name = name 
        self.id = id
        self.grades =  []

    def add_grade(self,grade):
        self.grades.append(grade)

    def get_avg(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.id)
        print("Grades List:", self.grades)
    
        total = sum(self.grades)
        count = len(self.grades)
        print("Total Marks:", total)
        print("Number of Subjects:", count)
        print("Average:", total/count if count > 0 else 0)

s1 = Student("FURQAN",303111)

s1.add_grade(85)
s1.add_grade(84)
s1.add_grade(78)
s1.add_grade(96)
s1.add_grade(80)
s1.add_grade(76)

s1.display_info()