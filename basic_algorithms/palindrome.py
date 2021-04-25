def is_Palindrome(string):
    string = string.caseflod()
    string_rev = string[::-1]

    if string == string_rev:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome!")
