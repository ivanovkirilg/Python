'''
Created on Apr 28, 2021

@author: kivag
'''

class Person():

    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name
    
    def print_name(self):
        print(self.f_name, self.l_name)


courses = ['English', 'Maths', 'Computer Science']

def gen_faculty_num(course):
    curr_num = 1
    
    while True:
        if course == courses[0]:
            new_num = 1000
        elif course == courses[1]:
            new_num = 2000
        else:
            new_num = 3000
        
        new_num += curr_num
        curr_num += 1
        yield new_num


new_fac_nums = [gen_faculty_num(courses[0]), 
                gen_faculty_num(courses[1]), 
                gen_faculty_num(courses[2]) ]

class Student(Person):
    
    def enroll(self, course_id):
        self.course = courses[course_id]
        self.fac_num = new_fac_nums[course_id].__next__()
    
    def print_info(self):
        self.print_name()
        print(self.course, self.fac_num)
        

mathematician = Student('Mark', 'Peterson')
mathematician.enroll(1)

mathematician.print_info()


programmer = Student('David', 'Jagerhoff')
programmer.enroll(2)        
        
programmer.print_info()


geek = Student('Jack', 'Johnson')
geek.enroll(1)
        
geek.print_info()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        