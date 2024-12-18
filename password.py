# Purpose: Prompt user for a new password and evaluate the password to
# ensure it meets the following requirements: between 8-20 characters,
# no empty spaces, and at least one alphabetical character and one number.
# Course: CMIS 102 6988 Introduction to Problem Solving and Algorithm Design
# Date: July 23, 2023

def main():

    # Initialize variable
    # Display welcome message
    print("Welcome!\n")

    # Prompt user for password
    userPW = input ("""Please enter a new password: 
 - Must be between 8 – 20 characters
 - Must contain at least one alphabetical character
 - Must contain at least one number
 - No empty spaces\n""")

    pwLengthValidation = validatePWLength(userPW)
    pwEmptySpaceValidation = validateEmptySpaces(userPW)
    flag_l = validatePWAlpha(userPW)
    flag_n = validatePWNum(userPW)

    # Display output
    if pwLengthValidation and flag_l and flag_n and pwEmptySpaceValidation:
        print("Success! Your password meets all the requirements.")
    else:
        print("The password you entered does not meeting the following requirements:")
        if pwLengthValidation == False:
            print(""" - Your password is either too short or too long.
   It must be between 8-20 characters.""")
        if pwEmptySpaceValidation == False:
            print(""" - Your password contains an empty character.
   Empty characters are not permitted""")
        if flag_l == False:
            print(" - Your password must contain at least one letter.")
        if flag_n == False:
            print(" - Your password must contain at least one number.")

# Functions ---------------------------------------------------------

def validatePWLength(userPW):
    userPWLength = len(userPW)
    if userPWLength < 8:
        pwLengthValidation = False
    elif userPWLength > 20:
        pwLengthValidation = False
    else: 
        pwLengthValidation = True
    return(pwLengthValidation)

def validateEmptySpaces(userPW):
    pwEmptySpace = userPW.find(" ")
    if pwEmptySpace != -1:
        pwEmptySpaceValidation = False
    else:
        pwEmptySpaceValidation = True
    return(pwEmptySpaceValidation)

def validatePWAlpha(userPW):
    # initializing flag variable
    flag_l = False
    # checking for letter and numbers in string
    for i in userPW:
        # if string has letter
        if i.isalpha():
            flag_l = True
        else:
            flat_l = False
    return(flag_l) 

def validatePWNum(userPW):
    # initializing flag variable
    flag_n = False
    # checking for letter and numbers in string
    for i in userPW:
        # if string has number
        if i.isdigit():
            flag_n = True
        else:
            flat_n = False
    return(flag_n)

#--- Execute --------------------------------------------------------
main()
    
