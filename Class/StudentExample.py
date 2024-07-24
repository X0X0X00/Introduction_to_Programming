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

    def info(self):
        print('Student name is', self.name, self.surname)
        print('Id number:', self.ID)
        print('Currently at year' , self.year)
        for course in self.courses:
            print(course[0]+': '+ course[1])

    def email(self):
        return self.name[0] + str(self.ID) + '@ur.rochester.edu'

    def getGPA(self):
        total_number_of_courses = 0
        total = 0
        for course in self.courses:  # e.g. course = ['CSC 161', 'A']
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

    def add_course(self, course):
        self.courses.append(course)
                
        
        

    

        
    
if __name__=='__main__':
    Sally = Student('Sally', 'Computer', 123456, 2, [['CSC 161', 'A'],['CSC 280' , 'A'], ['CSC 171' , 'A'],
                                                     ['CSC 171' , 'A']] )
    Rob = Student('Rob', 'Star', 234567, 2, [['CSC 161', 'A'],['CSC 280' , 'A'], ['CSC 171' , 'C'],['CSC 172' , 'A']])
    Mike = Student('Mike', 'Lake', 345678, 1, [['CSC 161', 'A'],['CSC 280' , 'A'], ['CSC 171' , '']] )
    Mike.info()
    # print(Rob.email())
    # print(Sally.getGPA())
    Mike.add_course(['CSC 172', ''])
    Mike.info()
    


    
