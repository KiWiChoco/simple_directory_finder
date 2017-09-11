import os


def change_directory(a):
    print("current directory : " ,a)
    # print(os.path.isdir(a))

    # if os.path.isdir(a):

    print("enter '..' for the parent dir, and q to exit ")
    input_path = input('enter a directory or path : ')

    if not os.path.isdir(input_path):
        print('That is wrong dir')

    if input_path == '..':
        os.chdir("..")
        print(os.getcwd())

    if os.path.isdir(input_path):
        os.chdir(a + '\\' + input_path)
        print(os.getcwd())
        a = os.getcwd()

        print(os.listdir(a))





