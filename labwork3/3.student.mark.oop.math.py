import math
import numpy as np
import curses
from curses import wrapper
from curses.textpad import Textbox,rectangle

class Student:
    def __init__(self,st_id,st_name,st_dob):
        self.st_id = st_id
        self.st_name = st_name
        self.st_dob = st_dob
    
    def getSt_id(self):
        return self.st_id
    
    def getSt_name(self):
        return self.st_name
    
    def getSt_dob(self):
        return self.st_dob

class Course:

    def __init__(self,course_id,course_name,credit):
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit
    
    
    def getCourse_id(self):
        return self.course_id
    
    def getCourse_name(self):
        return self.course_name
    
    def getCredit (self):
        return self.credit

class School:
    def __init__(self):
        self._students = {}
        self._courses = {}
        self._marks = {}
        self._GPA = {}
#=========================================================================================
    def input_st(self):
        while True:
            n = int(input("Enter Number of Students: "))
            if n <= 0:
                print("Enter at Least 1 Student")
            else:
                break
        for i in range(n):
            st_Id = input(f"Enter Student's ID No.{i+1}: ")
            st_Name = input(f"Enter Name of Student No.{i+1}: ")
            st_Dob = input("Enter DoB (DD/MM/YYYY): ")
            self._students[st_Id] = Student(st_Id,st_Name,st_Dob)
#=========================================================================================
    def input_course(self):
        while True:
            n = int(input("Enter Number of Courses: "))
            if n <=0 :
                print("Enter at least 1 Course!!")
            else:
                break
        for i in range(n):
            course_ID = input(f"Enter Course's ID No.{i+1}: ")
            course_Name = input(f"Enter Course's Name No.{i+1}: ")
            course_credit = float(input(f"Enter Number of Credit's Course No.{i+1}: "))
            self._courses[course_ID] = Course(course_ID,course_Name,course_credit)
#=========================================================================================
    def input_mark(self):
        while True:
            course_ID = input("Enter ID's Course: ")
            if course_ID not in self._courses:
                print("\n=========\nThe Couse's ID is not exist!!\n Please try again!!\n=========\n")
            else: 
                break
        
        for student in self._students:
            mark = float(input(f"Enter Mark(0-20) for {self._students[student].getSt_name()}: "))
            if mark > 20 or mark <0:
                print("\n==========\nThe Mark not in (0-20). Please try again!!\n==========")
            if student not in self._marks:
                self._marks[student] = {}
            self._marks[student][course_ID] = mark
#=========================================================================================
    #show student
    def list_st(self):
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        magenta_black = curses.color_pair(1)
        green_black = curses.color_pair(2)
        stdscr.erase()
        
        stdscr.addstr(0,50,"-----List student-----",curses.A_BOLD)
        column = 0
        row = 0
        cnt = 1
        for student in self._students:
            stdscr.addstr( column + 2,row + 6,f"--Student {cnt}--")
            stdscr.addstr( column + 3,row + 2,f"• ID:   {self._students[student].getSt_id()}",curses.A_BOLD)
            stdscr.addstr( column + 4,row + 2,f"• Name: {self._students[student].getSt_name()}",curses.A_BOLD)
            stdscr.addstr( column + 5,row + 2,f"• Dob:  {self._students[student].getSt_dob()}",curses.A_BOLD)
            stdscr.attron(magenta_black)
            rectangle(stdscr, 1, 1, 6,row + 26) #top-left-col-row
            stdscr.attroff(magenta_black)
            cnt += 1
            row += 27
        stdscr.addstr(8,4,"-----Press any key to continue...",green_black)
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()
#=========================================================================================
    #show course
    def list_course(self):
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        magenta_black = curses.color_pair(1)
        green_black = curses.color_pair(2)
        stdscr.erase()

        stdscr.addstr(0,50,"-----List Course-----",curses.A_BOLD)
        column = 0
        row = 0
        cnt = 1
        for course in self._courses:
            stdscr.addstr(column + 2,row + 6,f"--Course No.{cnt}--")
            stdscr.addstr(column + 3,row + 2,f"• ID:     {self._courses[course].getCourse_id()}")
            stdscr.addstr(column + 4,row + 2,f"• Course: {self._courses[course].getCourse_name()}")
            stdscr.addstr(column + 5,row + 2,f"• Credit: {self._courses[course].getCredit()}")
            stdscr.attron(magenta_black)
            rectangle(stdscr, 1, 1, 6,row + 26) #top-left-col-row
            stdscr.attroff(magenta_black)
            cnt += 1
            row += 27
        stdscr.addstr(8,4,"-----Press any key to continue...",green_black)
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()
#=========================================================================================
    #show mark for chosen course
    def list_mark(self):
        while True:
            course_ID = input("Enter ID of the course: ")
            if self._marks == {}:
                print("\n===================\nMark Has Not Been Entered")
                print("Return To Choosen (1) to Enter Mark\n===================")
                return 0
            elif course_ID not in self._courses :
                print("\n===========\nThe ID course not exist!! \nPlease try again!!\n===========\n")
            else: 
                break   
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        magenta_black = curses.color_pair(1)
        green_black = curses.color_pair(2)
        stdscr.erase()

        stdscr.addstr(0,50,"-----List Mark-----",curses.A_BOLD)
        column = 0
        row = 0
        row1 = 0
        for st_Id in self._students:
            stdscr.addstr(column + 3,row + 2,f"• Student: {self._students[st_Id].getSt_name()}")
            stdscr.addstr(column + 4,row + 2,f"• Course:  {self._courses[course_ID].getCourse_name()}") 
            stdscr.addstr(column + 5,row + 2,f"• Mark:    {self._marks[st_Id][course_ID]}")
            stdscr.attron(magenta_black)
            rectangle(stdscr, 1, 1, 7,row1 + 29) #top-left-col-row
            stdscr.attroff(magenta_black)
            row += 27
            row1 += 29
        stdscr.addstr(8,4,"-----Press any key to continue...",green_black)
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()
#==============================================================================================
    #function to calculate the GPA
    def input_gpa(self):
        #creat a mark array, credit array              
        _list_gpa = []
        _list_credit = [] 
        while True:
            stu_id = input("Enter Student's ID: ")
            if self._marks == {}:
                print("\n===================\nMark Has Not Been Entered")
                print("Return To Choosen (1) to Enter Mark\n===================")
                return 0
            elif stu_id not in self._students:
                print("\n==========\nThe ID is not exist\n==========")
                return 0
            else:
                break
        for course_ID in self._courses:    
            _list_gpa.append(self._marks[stu_id][course_ID])
            _list_credit.append(self._courses[course_ID].getCredit())

        #add mark,credit to array           
        self.mark_array = np.array(_list_gpa)
        self.credit_array = np.array(_list_credit)

        #calculate GPA:
        gpa = (np.sum(self.mark_array*self.credit_array))/(np.sum(self.credit_array))
        average_gpa = math.floor(gpa)
        # print average GPA:
        if stu_id in self._students:
            if average_gpa not in self._GPA:
                self._GPA[stu_id] = {}
            self._GPA[stu_id] = average_gpa
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)

        magenta_black = curses.color_pair(1)
        green_black = curses.color_pair(2)
        blue_black = curses.color_pair(3)

        stdscr.erase()
        stdscr.attron(magenta_black)
        rectangle(stdscr, 1, 40, 7,80) #top-left-col-row
        stdscr.attroff(magenta_black)
        stdscr.attron(blue_black)
        rectangle(stdscr, 3, 48, 5,70) #top-left-col-row
        stdscr.attroff(blue_black)
        stdscr.addstr(4,50,f"The GPA is: [{self._GPA[stu_id]}/20]",curses.A_BOLD)
        stdscr.addstr(9,40,"-----Press any key to continue...",green_black)
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()
#=========================================================================================
    # Sort student:
    def Sort_st(self):
        list_sort = []
        count = 0
        for student in self._students:
            list_sort.append((self._students[student].getSt_id(),self._students[student].getSt_name(),self._GPA[student]))
            count += 1
        sort_array = np.array(list_sort)
        sort_array = sort_array[np.argsort(sort_array[:,2])[:: -1]]
        #count the dimension in sort_array

        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)

        magenta_black = curses.color_pair(1)
        green_black = curses.color_pair(2)
        blue_black = curses.color_pair(3)

        stdscr.erase()
        stdscr.attron(magenta_black)
        rectangle(stdscr, 1, 1, 7,70) #top-left-col-row
        stdscr.attroff(magenta_black)
        stdscr.attron(blue_black)
        i = 0
        column = 0
        row = 0
        cnt = 1
        stdscr.addstr(column , row + 25,"-----Student List Sort by GPA Descending-----")
        stdscr.addstr(column + 2, row + 7,f"STT        ID                NAME                 GPA")
        for i in range (count):
            stdscr.addstr(column + 3, row + 8,f"{cnt}",curses.A_BOLD)
            stdscr.addstr(column + 3, row + 15,f"{sort_array[i,0]}",curses.A_BOLD)
            stdscr.addstr(column + 3, row + 30,f"{sort_array[i,1]}",curses.A_BOLD)
            stdscr.addstr(column + 3, row + 55,f"[{sort_array[i,2]}/20]",curses.A_BOLD)
            i += 1
            column += 1
            cnt += 1
        stdscr.addstr(9,25,"-----Press any key to continue...",green_black)
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()
#=========================================================================================
system = School()
system.input_st()
system.input_course()

while True:
    print("1. Enter Mark for course")
    print("2. List Student")
    print("3. List Course")
    print("4. List Mark for chosen course")
    print("5. List GPA")
    print("6. Sort Student")
    print("0. Exit")
    try:
        choice = int(input("Enter your choice(0-6): "))

        if choice == 1:
            system.input_mark()

        elif choice == 2:
            system.list_st()

        elif choice == 3 :
            system.list_course()

        elif choice == 4 :
            system.list_mark()
        
        elif choice == 5:
            system.input_gpa()

        elif choice == 6:
            system.Sort_st() 

        elif choice == 0:
            break
        else:
            stdscr = curses.initscr()
            curses.start_color()
            curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
            magenta_black = curses.color_pair(1)
            cyan_black = curses.color_pair(3)
            stdscr.erase()
            stdscr.addstr(5,45,"Please try again, choose [0-6]",magenta_black)
            stdscr.addstr(8,40,"-----Press any key to continue...",cyan_black)
            stdscr.refresh()
            stdscr.getch()
            curses.endwin()

    except ValueError:
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        magenta_black = curses.color_pair(1)
        cyan_black = curses.color_pair(3)
        stdscr.erase()
        stdscr.addstr(5,45,"Please try again, choose [0-6]",magenta_black)
        stdscr.addstr(8,40,"-----Press any key to continue...",cyan_black)
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()
        


        
    
    


    


