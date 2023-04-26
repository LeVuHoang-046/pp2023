import math
import numpy as np
import curses
from curses import wrapper
from curses.textpad import Textbox,rectangle
from input import *
from input import _students
from input import _courses
from input import _marks


_GPA = {}
#show student
def list_st():
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
        for student in _students:
            stdscr.addstr( column + 2,row + 6,f"--Student {cnt}--")
            stdscr.addstr( column + 3,row + 2,f"• ID:   {_students[student].getSt_id()}",curses.A_BOLD)
            stdscr.addstr( column + 4,row + 2,f"• Name: {_students[student].getSt_name()}",curses.A_BOLD)
            stdscr.addstr( column + 5,row + 2,f"• Dob:  {_students[student].getSt_dob()}",curses.A_BOLD)
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
def list_course():
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
        for course in _courses:
            stdscr.addstr(column + 2,row + 6,f"--Course No.{cnt}--")
            stdscr.addstr(column + 3,row + 2,f"• ID:     {_courses[course].getCourse_id()}")
            stdscr.addstr(column + 4,row + 2,f"• Course: {_courses[course].getCourse_name()}")
            stdscr.addstr(column + 5,row + 2,f"• Credit: {_courses[course].getCredit()}")
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
def list_mark():
        while True:
            course_ID = input("Enter ID of the course: ")
            if _marks == {}:
                print("\n===================\nMark Has Not Been Entered")
                print("Return To Choosen (1) to Enter Mark\n===================")
                return 0
            elif course_ID not in _courses :
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
        for st_Id in _students:
            stdscr.addstr(column + 3,row + 2,f"• Student: {_students[st_Id].getSt_name()}")
            stdscr.addstr(column + 4,row + 2,f"• Course:  {_courses[course_ID].getCourse_name()}") 
            stdscr.addstr(column + 5,row + 2,f"• Mark:    {_marks[st_Id][course_ID]}")
            stdscr.attron(magenta_black)
            rectangle(stdscr, 1, 1, 7,row1 + 29) #top-left-col-row
            stdscr.attroff(magenta_black)
            row += 27
            row1 += 29
        stdscr.addstr(8,4,"-----Press any key to continue...",green_black)
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()
#function to calculate the GPA
def input_gpa():
        #creat a mark array, credit array              
        _list_gpa = []
        _list_credit = [] 
        while True:
            stu_id = input("Enter Student's ID: ")
            if _marks == {}:
                print("\n===================\nMark Has Not Been Entered")
                print("Return To Choosen (1) to Enter Mark\n===================")
                return 0
            elif stu_id not in _students:
                print("\n==========\nThe ID is not exist\n==========")
                return 0
            else:
                break
        for course_ID in _courses:    
            _list_gpa.append(_marks[stu_id][course_ID])
            _list_credit.append(_courses[course_ID].getCredit())

        #add mark,credit to array           
        mark_array = np.array(_list_gpa)
        credit_array = np.array(_list_credit)

        #calculate GPA:
        gpa = (np.sum(mark_array*credit_array))/(np.sum(credit_array))
        average_gpa = math.floor(gpa)
        # print average GPA:
        if stu_id in _students:
            if average_gpa not in _GPA:
                _GPA[stu_id] = {}
            _GPA[stu_id] = average_gpa
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
        stdscr.addstr(4,50,f"The GPA is: [{_GPA[stu_id]}/20]",curses.A_BOLD)
        stdscr.addstr(9,40,"-----Press any key to continue...",green_black)
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()
#=========================================================================================
    # Sort student:
def Sort_st():
        list_sort = []
        count = 0
        for student in _students:
            list_sort.append((_students[student].getSt_id(),_students[student].getSt_name(),_GPA[student]))
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