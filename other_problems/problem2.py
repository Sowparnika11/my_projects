# Write a function that checks if a given word is a palindrome. Character case should be ignored.

def check_palindrome(data):
    actual_string = data
    reverse = data[::-1]
    if reverse == actual_string:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_word = input("Enter the word to be checked : ")
    result = check_palindrome(input_word.lower())
    if result :
        print ("Given word is a palindrome")
    else:
        print ("Given word is not a palindrome")

######### o/p##############
# test case 1:
# Enter the word to be checked : SoS
# Given word is a palindrome

#test case 2
# Enter the word to be checked : sos
# Given word is a palindrome