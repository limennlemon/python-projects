# Purpose: Program to calculate each person's share to cover their expenses for a group vacation. 
# Course: CMIS 102 6988 Introduction to Problem Solving and Algorithm Design
# Date: July 30, 2023

def main():

    # Initialize variables
    foodList = list()
    gasList = list()

    # Display welcome message
    print("""Welcome! This program calculates the cost per person
to cover the cost of food and gas for a group vacation.\n""")

    # Prompt user for number of people
    numPeople = int(input("Please enter the number of people: "))

    # Prompt user for number of days
    numDays = int(input("Please enter the number of days: "))

    # Prompt user for the cost of food for each day
    for i in range(numDays):
        costFood = float(input("\nPlease enter the cost of food per day: "))
        foodList.append(costFood)
        #Prompt user for the cost of gas for each day                       
        for i in range(1):
            costGas = float(input("Please enter the cost of gas per day: "))
            gasList.append(costGas)

    totalCostFood = sum(foodList)
    totalCostGas = sum(gasList)
    totalCostVacation = totalCostFood + totalCostGas
    shareVacationCost = totalCostVacation / numPeople
    
    # Display output
    print("\nTotal cost for food is: ", "{0:.2f}".format(totalCostFood))
    print("Total cost for gas is: ", "{0:.2f}".format(totalCostGas))
    print("The total cost of the vacation is: ", "{0:.2f}".format(totalCostVacation))
    print("Number of people: ", numPeople)
    print("Share for each person: ", "{0:.2f}".format(shareVacationCost))

#--- Execute --------------------------------------------------------
    
main()
