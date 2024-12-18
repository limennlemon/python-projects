# Purpose: Program to compute the cost for house cleaning services
# Course: CMIS 102 6988 Introduction to Problem Solving and Algorithm Design
# Date: July 2, 2023

def main():
    
# Display welcome message 
    print("Welcome to UMGC Cleaning Services!")

# Prompt customer for their name
    customerName = input("\nPlease enter your name: ")

# Prompt customer for the size of home (number of rooms)
# 1 = small (1-7 rooms) medium (8-15 rooms) 3 = large (15-25 rooms)
    print("Please provide the number of rooms in your house (Enter 1-3): ")
    print("1 = small (1-7 rooms) \n2 = medium (8-15 rooms) \n3 = large (15-25 rooms)")
    homeSize = int(input())
        # Validate user response
    if ((homeSize < 1) or (homeSize > 3)):
        # Display error message and reprompt
        homeSize = int(input("Invalid response. Please enter 1-3: "))

# Prompt customer for the level of cleaning (frequency)
# 1 = weekly 2 = bi-weekly 3 = monthly
    print("Please provide frequency for the services (Enter 1-3): ")
    print("1 = weekly \n2 = bi-weekly \n3 = monthly")
    frequencyCleaning = int(input())
    # Validate user response
    if ((frequencyCleaning < 1) or (frequencyCleaning > 3)):
        # Display error message and reprompt
        frequencyCleaning = int(input("Invalid response. Please enter 1-3: "))

# Prompt customer for optional add on services
# 0 = none 1 = carpet steam cleaning 2 = windows 3 = other
    print("Please select optional add on services (Enter 0-3): ")
    print("0 = none \n1 = carpet steam cleaning \n2 = windows \n3 = other")
    addOns = int(input())
    # Validate user response
    if ((addOns < 0) or (addOns > 3)):
        # Display error message and reprompt
        addOns = int(input("Invalid response. Please enter 0-3: "))

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
    if (addOns == 0):
        priceAddons = 0
    elif (addOns == 1):
        priceAddons = 150
    elif (addOns == 2):
        priceAddons = 200
    else:
        priceAddons = 0

# Calculate the final price
    finalServicesPricing = priceHomeSize + priceFrequency + priceAddons

# Display final cost of the cleaning services
    # If customer selects "3 = Other" for add ons, customer service will call them
    # to determine the type of job and associated pricing
    if (addOns == 3):
        print("Customer service will contact you to determine the cost for cleaning your home.")
    # For all other requests, the pricing will be displayed on the screen
    else:
        print("You selected the following options: ")
        print("Base pricing for your home: $", priceHomeSize)
        print("Additional surcharge based on frequency: $", priceFrequency)
        print("Cost for add ons: $", priceAddons)
        print("Your total cost will be: $", finalServicesPricing)
        print("We will be in touch soon to schedule a date and time.")
# Thank customer for their business
    print("Thank you for your business,", customerName, "!")   

#--- execute --------
main()

