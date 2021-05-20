"""Implement a group_by_owners function that:

·         Accepts a dictionary containing the file owner name for each file name.

·         Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
the group_by_owners function should return 
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}."""


def group_by_owners(data):
    result = dict()
    for f_name,owner in data.items():
        if owner in result:
          result[owner].append(f_name) 
        else:
            result.update({owner:[f_name]})
    return result
            
    pass
if __name__ == '__main__':
    total_file_count = int(input("Enter the total number of files : "))
    files_data = dict()
    for file in range(total_file_count):
        file_name = input("entwr the file name:")
        owner_name = input("entwr the file name:")
        files_data[file_name] = owner_name
    owners_list = group_by_owners(files_data)
    print ("files name  grouped by owners : " ,owners_list )


    #################Output ##############
# Enter the total number of files : 3
# enter the file name:inuput.txt
# enter the file name:randy
# enter the file name:code.py
# enter the file name:stan
# enter the file name:output.txt
# enter the file name:randy
# files name  grouped by owners :  {'randy': ['inuput.txt', 'output.txt'], 'stan': ['code.py']}

    