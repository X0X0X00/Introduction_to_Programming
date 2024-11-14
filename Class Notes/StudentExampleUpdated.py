"""
mkp
Week 11 Live Coding Example 3 Monday

Grades:
A	90–100%	4.0
B	80–89%	3.0
C	70–79%	2.0
D	60–69%	1.0
F	0–59%	0.0

[['CSC 161', 'A'],['CSC 280' , 'B']]
"""

class Student:
    def __init__(self,name, surname, ID, year, courses):
        self.name = name
        self.surname = surname
        self.ID = ID
        self.year = year
        self.courses = courses
        self.GPA = getGPA(courses)
        
    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_GPA(self):
        return self.GPA
    
    def info(self):
        print('Student name is', self.name, self.surname)
        print('Id number:', self.ID)
        print('Currently at year' , self.year)
        for course in self.courses:
            print(course[0]+': '+ course[1])
        print('GPA', self.GPA)

    def email(self):
        return self.name[0] + str(self.ID) + '@ur.rochester.edu'


    def add_course(self, course):
        self.courses.append(course)
        self.GPA = getGPA(self.courses)
        

                
        
def getGPA(list_of_courses):
    total_number_of_courses = 0
    total = 0
    for course in list_of_courses:  # e.g. course = ['CSC 161', 'A']
        if course[1]== 'A':
            total_number_of_courses += 1
            total += 4
        elif course[1]== 'B':
            total_number_of_courses += 1
            total += 3
        elif course[1]== 'C':
            total_number_of_courses += 1
            total += 2
        elif course[1]== 'D':
            total_number_of_courses += 1
            total += 1
        elif course[1]== 'F':
            total_number_of_courses += 1
            total += 0
        elif course[1]== '':
            pass
        else:
            print('Incorrect grade format')
    return total/total_number_of_courses               

def read_data(file_name):
    fd = open(file_name)
    students = []
    for line in fd:
        #print(line)
        line = line.split()
        #print(line)
        name = line[0]
        surname = line[1]
        ID = line[2]
        year =  line[3]
        list_of_courses = line[4:]
        courses = []
        n = len(list_of_courses)
        print(list_of_courses)
        for i in range(0,n,2):
            courses.append( [list_of_courses[i], list_of_courses[i+1]] ) # ['CSC 161', 'A']
        students.append(Student(name, surname, ID, year, courses))
    return students
        
def max_grade(students):
    """
finds max GPA
    """
    max = 0
    best_student = ""
    for stu in students:
        if max < stu.GPA:
            max = stu.GPA
            best_student = stu
    print('Max GPA:', max)
    best_student.info()
            
    
if __name__=='__main__':
    students = read_data('stu_data.txt')
    max_grade(students)
    print(max_grade.__doc__)
    


    
