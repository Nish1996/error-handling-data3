# We are using open(), built in functionality from Python to open files

def open_and_print(file_to_open):
    try:  # Tries to run the block of code
        file = open(file_to_open, 'r')
        file_line_list = file.readlines()

        for line in file_line_list:
            print(line.rstrip('\n'))

        file.close()
    except FileNotFoundError as errmsg:  # If it fails, then it will run this block of code
        print("File could not be opened, please see below")
        print(errmsg)

open_and_print('order.txt')