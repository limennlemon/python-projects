# Purpose: Program to compute the weighted average grade and highest grade of four students
# Course: CMIS 102 6988 Introduction to Problem Solving and Algorithm Design
# Date: July 17, 2023

def main():
    # Initialize 
    names = ['Mike', 'Mary', 'Tom', 'Jane'] # Student's names
    highestGrade = -999

    # Display welcome message
    print("Welcome to the UMGC Grading Center!")
    print("This program calculates each student's weighted average and the score/student name of the highest overall grade")
          
    # Loop for each of the student's names
    for name in names:
        
        #get the total weight of patron
        totalGrade = getTotalGrades(name)

        #Determine highest
        if (totalGrade > highestGrade):
          highestGrade = totalGrade     # Save grade
          highestGradeName = name       # Same name

    # Display output
    print("")
    print(highestGradeName, "achieved the highest grade of", highestGrade)

# Functions ---------------------------------------------------------

def getTotalGrades(name):
    
    totalStudentGrade = 0
   
    print("\nPlease enter grades for",name,": ")

    #Loop for 3 grades
    cnt = 1
    while (cnt <= 1):
        
        #Prompt the user for discussion grade
        discussion_grade = float(input("Discussion grade: "))
        #Validate discussion grade (>=0)
        if (discussion_grade < 0):
            discussion_grade = float(input("Discussion grade: "))
        quiz_grade = float(input("Quiz grade: "))
        #Validate quiz grade (>=0)
        if (quiz_grade < 0):
            quiz_grade = float(input("Quiz grade: "))
        assignment_grade = float(input("Assignment grade: "))
        #Validate assignment grade (>=0)
        if (assignment_grade < 0):
            assignment_grade = float(input("Assignment grade: "))
        
        cnt = cnt + 1

        # Calculate weighted average grade
        # Discussion - 15% of grade, Quiz - 35% of grade, Assignment - 50% of grade
        wtAvgGrade = (discussion_grade * 0.15) + (quiz_grade * 0.35) + (assignment_grade * 0.5)

    #Display totalWgtlost
    print("Weighted average grade: ", wtAvgGrade)

    return(wtAvgGrade)

#--- Execute --------------------------------------------------------
main()
    
