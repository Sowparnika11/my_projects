# Write a function to parse a log file & extract details of Errors & Warnings recorded into a separate file.

#test.log is the log file
#warning_message.txt is used to store warning messages
#error_message.txt is used to store error messages
def write_file(log_data,file_name):
    destination_file =open(file_name,'a')
    destination_file.write(log_data)
    destination_file.close()

if __name__ == '__main__':
    import re
    file  =open('test.log','r')
    data = file.readlines()
    file.close()

    for line in data:
        if re.match("^WARNING.*",line):
            write_file(line,'warning_message.txt')
            
        elif re.match("^ERROR.*",line):
            write_file(line,'error_message.txt')
        else:
            continue

