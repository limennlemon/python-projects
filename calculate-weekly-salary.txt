# Purpose: Calculate the weekly salary of a newspaper delivery person
# Course: CMIS 102 6988 Introduction to Problem Solving and Algorithm Design
# Date: June 25, 2023

def main():
    #Initialize variables
    costPerNewspaper = 3.50   # cost per newspaper $3.50
    rateCommission = 0.05   # commission rate is 5%

    #Display welcome message
    print("\nWelcome to the Daily Express!")
    print("Please enter your information for week ending June 25, 2023 to calculate your salary.")

    # Prompt\get input from newspaper delivery person
    numDaysPerWeek = int(input("\nHow many days did you deliver newspapers this week? "))
    numDeliveredPerDay = int(input("How many papers did you deliver each day? "))
    amountTipReceived = float(input("How much tip did you receive? "))

    # Calculate the total number of newspapers delivered this week
    totalNewspapers = numDaysPerWeek * numDeliveredPerDay

    # Calculate the total cost of newspapers delivered this week
    totalCostNewspapers = costPerNewspaper * totalNewspapers

    # Calculate the total amount of commission for week  
    totalCommission = totalCostNewspapers * rateCommission 
 
    # Calculate the total salary for week (total commission + tip) 
    grandTotal = totalCommission + amountTipReceived
   
    # Display the results
    print("\nSalary for week ending June 25, 2023: ")
    print("\tTotal number of newspapers delivered:", totalNewspapers)
    print("\tWeekly Salary: $", totalCommission)
    print("\tTip: $", amountTipReceived)
    print("\tTotal Salary: $", grandTotal)

#--- Execute --------------------------------------------------------
main()
