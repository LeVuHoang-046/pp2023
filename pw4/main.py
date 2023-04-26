from input import *
from output import *


input_st()
input_course()

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
            input_mark()

        elif choice == 2:
            list_st()

        elif choice == 3 :
            list_course()

        elif choice == 4 :
            list_mark()
        
        elif choice == 5:
            input_gpa()

        elif choice == 6:
            Sort_st() 

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