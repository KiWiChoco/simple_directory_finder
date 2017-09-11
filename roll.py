from change_directory import *
from search_file import *
from delete_directory import *
from quit import *
import os


def login():
    os.chdir('C:\\Users\\User')
    curr_path = os.getcwd()


    print("Welcome")
    print(" 1 : change directory\n"
          " 2 : search file\n"
          " 3 : delete directory or file\n"
          " 4 : quit")

    do = int(input("please input number want to do : "))

    switcher = {
        1: change_directory,
        2: search_file,
        3: delete_directory,
        4: quit
    }

    role_menu = switcher.get(do)
    a = curr_path

    role_menu(a)

login()