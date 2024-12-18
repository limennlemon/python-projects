# Purpose: Program to compute the cost for house cleaning services using functions
# Course: CMIS 102 6988 Introduction to Problem Solving and Algorithm Design
# Date: July 6, 2023

def main():
    
    # Display welcome message and prompt customer for their name
    customerName = welcomeMessage()

    # Prompt customer for the size of home, level of cleaning, and optional add on services
    homeSize, frequencyCleaning, optionalAddOns = getUserInput()

    # Calculate the price according to the specifications (inputs) provided by the customer
    priceHomeSize, priceFrequency, priceAddOns, finalServicesPricing = calculateCleaningSvsPrice(homeSize, frequencyCleaning, optionalAddOns)

    # Display the information provided by the customer and estimated price for cleaning
    displayCleaningSvsEstimate(customerName, homeSize, frequencyCleaning, optionalAddOns, priceHomeSize, priceFrequency, priceAddOns, finalServicesPricing) 

# Functions ---------------------------------------------------------

def welcomeMessage():
    
    # Display welcome message 
    print("Welcome to UMGC Cleaning Services!")
    
    # Prompt customer for their name
    customerName = input("Please enter your name: ")
    return(customerName)

# -------------------------------
def getUserInput():

    # Prompt customer for the size of home (number of rooms)
    # 1 = small (1-7 rooms) medium (8-15 rooms) 3 = large (15-25 rooms)
    print("Please provide the number of rooms in your house (Enter 1-3): ")
    print("1 = small (1-7 rooms) \n2 = medium (8-15 rooms) \n3 = large (15-25 rooms)")
    homeSize = int(input())
            
    # Prompt customer for the level of cleaning (frequency)
    # 1 = weekly 2 = bi-weekly 3 = monthly
    print("Please provide frequency for the services (Enter 1-3): ")
    print("1 = weekly \n2 = bi-weekly \n3 = monthly")
    frequencyCleaning = int(input())
            
    # Prompt customer for optional add on services
    # 0 = none 1 = carpet steam cleaning 2 = windows 3 = other
    print("Please select optional add on services (Enter 0-3): ")
    print("0 = none \n1 = carpet steam cleaning \n2 = windows \n3 = other")
    optionalAddOns = int(input())
        
    return(homeSize, frequencyCleaning, optionalAddOns)
    
# -------------------------------
def calculateCleaningSvsPrice(homeSize, frequencyCleaning, optionalAddOns):

    # Calculate home size to determine the base price
    if (homeSize == 1):
        priceHomeSize = 50
    elif (homeSize == 2):
        priceHomeSize = 85
    else: 
        priceHomeSize = 125

    # Calculate the price based on the frequency of cleaning
    if (frequencyCleaning == 1):
        priceFrequency = priceHomeSize * 0.25
    elif (frequencyCleaning == 2):
        priceFrequency = priceHomeSize * 0.35
    else:
        priceFrequency = priceHomeSize * 0.45

    # Calculate the price of add ons
    if (optionalAddOns == 0):
        priceAddOns = 0
    elif (optionalAddOns == 1):
        priceAddOns = 150
    elif  (optionalAddOns == 2):
        priceAddOns = 200
    else:
        priceAddOns = 0

    # Calculate the final price


    return(priceHomeSize, priceFrequency, priceAddOns, finalServicesPricing)

# -------------------------------
def displayCleaningSvsEstimate(customerName, homeSize, frequencyCleaning, optionalAddOns, priceHomeSize, priceFrequency, priceAddOns, finalServicesPricing):

    # Display final cost of the cleaning services
    # If customer selects "3 = Other" for add ons, customer service will call them
    # to determine the type of job and associated pricing
    if (optionalAddOns == 3):
        print("Customer service will contact you to determine the cost for cleaning your home.")
    # For all other requests, the pricing will be displayed on the screen
    else:
        print("You selected the following options: ")
        print("Base pricing for your home: $", format(priceHomeSize, ".2f"))
        print("Additional surcharge based on frequency: $", format(priceFrequency, ".2f"))
        print("Cost for add ons: $", format(priceAddOns, ".2f"))
        print("Your total cost will be: $", format(finalServicesPricing, ".2f"))
        print("We will be in touch soon to schedule a date and time.")
        # Thank customer for their business
        print("Thank you for your business,", customerName, "!")   

#--- execute --------
main()


