# We are using open(), built in functionality from Python to open files

try:  # Tries to run the block of code
    file = open('order.txt', 'r')
    file_line_list = file.readlines()
    # print(file)
    # print(type(file_line_list))
    for line in file_line_list:
        print(line.rstrip('\n'))

    file.close()  # If you don't close the file, it can cause a lock
except FileNotFoundError as errmsg:  # If it fails, then it will run this block of code
    print("File could not be opened, please see below")
    print(errmsg)  # Captured error message in line
    raise  # Sends the default error and crucially stops the code - Line 9 will not run
    print('Hey')
    # print('PANIC!!! ERRORS!!! PANIC NOW!!!!')
