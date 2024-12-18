# Purpose: Program to calculate the cost for home cleaning or yard services
# Course: CMIS 102 6988 Introduction to Problem Solving and Algorithm Design
# Date: August 8, 2023

def main():

    # Display welcome message
    print("""Welcome to UMGC Home Cleaning & Yard Services!""")

    Invalid = True
    while(Invalid):
        # Prompt user for type of services (home cleaning or yard services)
        typeService = int(input("""Please select the type of service.
Enter '1' for home cleaning and '2' for yard services.  \n"""))
        # Display error message and reprompt if user enters an incorrect response
        if (typeService != 1) and (typeService != 2):
            print("""\n***Invalid response*** Please try again. Enter '1' for home cleaning
or '2' for yard services.  \n""")
        else:
            Invalid = False

    Invalid2 = True
    while(Invalid2):
        # Prompt user to indicate whether they qualify for the senior citizens discount
        typeSeniorDiscount = str(input("""We offer a 5% discount to senior citizens. Are you 65 or older?
Please enter 'Y' for yes or 'N' for no.  """))
        # Display error message and reprompt if user enters an incorrect response
        if (typeSeniorDiscount.upper() != "Y") and (typeSeniorDiscount.upper() != "N"):
            print("""\n***Invalid response*** Please try again. """)
        else:
            Invalid2 = False

    # Test if customer entered "Y" and if they did print message that they will receive discount
    if (typeSeniorDiscount.upper() == "Y"):
        print("""
***You qualify for our senior citizen discount.***\n""")
    else:  
        print("")

    # If customer selected 1 for home cleaning services run the following functions
    if (typeService == 1): 
        print("Choose from the following home cleaning service options:\n")
        # Get user input about home size, frequency, and add-ons
        homeSize, homeSizeTxt, homeFrequency, homeFrequencyTxt, homeOptions, homeOptionsTxt = inputHomeCleaning()
        # Calculate price based on customer input
        homeSizePrice, homeFrequencyPrice, homeOptionsPrice, homeFinalPrice = calculateHomeCleaningSvs(homeSize, homeFrequency, homeOptions)
        # Calculate senior discount (if applicable)
        typeSeniorDiscountPrice, homeFinalPrice = calculateHomeSeniorDiscount(typeSeniorDiscount, homeFinalPrice)
        # Display estimate
        displayHomeCleaningEst(typeSeniorDiscount, typeSeniorDiscountPrice, homeSize, homeSizeTxt, homeFrequency, homeFrequencyTxt, homeOptions, homeOptionsTxt, homeSizePrice, homeFrequencyPrice, homeOptionsPrice, homeFinalPrice) 

    # If customer selected 2 for yard services run the following functions
    elif (typeService == 2): 
        print("Choose from the following yard service options:\n")
        # Get user input about lawn SF, eding linear footage, and number of shrubs
        yardSqFtMowing, yardLinearFtEdging, yardNumShrub = inputYardSvs()
        # Calculate price based on customer input
        yardSqFtMowingPrice, yardLinearFtEdgingPrice, yardNumShrubPrice, yardFinalPrice = calculateYardSvs(yardSqFtMowing, yardLinearFtEdging, yardNumShrub)
        # Calculate senior discount (if applicable)
        typeSeniorDiscountPrice, yardFinalPrice = calculateYardSeniorDiscount(typeSeniorDiscount, yardFinalPrice)
        # Display estimate
        displayYardEst(typeSeniorDiscount, typeSeniorDiscountPrice, yardSqFtMowing, yardLinearFtEdging, yardNumShrub, yardSqFtMowingPrice, yardLinearFtEdgingPrice, yardNumShrubPrice, yardFinalPrice)

    # Display thank you message
    print("")
    print("Thank you for your business!") 
    
#--- Functions ------------------------------------------------------ 

# Home Cleaning Services
# -------------------------------
def inputHomeCleaning():

    # Prompt customer for the size of home (number of rooms)
    # 1 = small (1-7 rooms) medium (8-15 rooms) 3 = large (15-25 rooms)
    print("Please provide the number of rooms in your house (Enter 1-3): ")
    print("1 = small (1-7 rooms) \n2 = medium (8-15 rooms) \n3 = large (15-25 rooms)")
    homeSize = int(input())
    if homeSize == 1:
        homeSizeTxt = "small"
    elif homeSize == 2:
        homeSizeTxt = "medium"
    else:
        homeSizeTxt = "large"
            
    # Prompt customer for the level of cleaning (frequency)
    # 1 = weekly 2 = bi-weekly 3 = monthly
    print("Please provide frequency for the services (Enter 1-3): ")
    print("1 = weekly \n2 = bi-weekly \n3 = monthly")
    homeFrequency = int(input())
    if homeFrequency == 1:
        homeFrequencyTxt = "weekly"
    elif homeFrequency == 2:
        homeFrequencyTxt = "bi-weekly"
    else:
        homeFrequencyTxt = "monthly"
            
    # Prompt customer for optional add on services
    # 0 = none 1 steam cleaning carpets 2 = windows 3 = other
    print("Please select optional add on services (Enter 1-3): ")
    print("1 = steam clean carpets \n2 = window cleaning \n3 = none")
    homeOptions = int(input())
    if homeOptions == 1: 
        homeOptionsTxt = "(steam carpets)     "
    elif homeOptions == 2: 
        homeOptionsTxt = "(windows)           "
    else: 
        homeOptionsTxt = "(none)              "
      
    return(homeSize, homeSizeTxt, homeFrequency, homeFrequencyTxt, homeOptions, homeOptionsTxt)

# -------------------------------
def calculateHomeCleaningSvs(homeSize, homeFrequency, homeOptions):   

    # Calculate home size to determine the base price
    if (homeSize == 1):
        homeSizePrice = 50
    elif (homeSize == 2):
        homeSizePrice = 85
    else: 
        homeSizePrice = 125

    # Calculate the price based on the frequency of cleaning
    if (homeFrequency == 1):
        homeFrequencyPrice = homeSizePrice * 0.25
    elif (homeFrequency == 2):
        homeFrequencyPrice = homeSizePrice * 0.35
    else:
        homeFrequencyPrice = homeSizePrice * 0.45

    # Calculate the price of add ons
    if (homeOptions == 1):
        homeOptionsPrice = 150
    elif (homeOptions == 2): 
        homeOptionsPrice = 200
    else:
        homeOptionsPrice = 0
 
    # Calculate the final price
    homeFinalPrice = homeSizePrice + homeFrequencyPrice + homeOptionsPrice

    return(homeSizePrice, homeFrequencyPrice, homeOptionsPrice, homeFinalPrice)

# -------------------------------
def calculateHomeSeniorDiscount(typeSeniorDiscount, homeFinalPrice):
    if (typeSeniorDiscount.upper() == "Y"): # Calculate senior citizen discount if applicable
        typeSeniorDiscountPrice = homeFinalPrice * 0.05
        homeFinalPrice = homeFinalPrice - typeSeniorDiscountPrice
    else:
        typeSeniorDiscountPrice = 0
    return(typeSeniorDiscountPrice, homeFinalPrice)

# -------------------------------
def displayHomeCleaningEst(typeSeniorDiscount, typeSeniorDiscountPrice, homeSize, homeSizeTxt, homeFrequency, homeFrequencyTxt, homeOptions, homeOptionsTxt, homeSizePrice, homeFrequencyPrice, homeOptionsPrice, homeFinalPrice):

    # Display final cost of the cleaning services
    print(" ")
    print("""Estimate for home cleaning services: \n""")
    print("Base price for", homeSizeTxt,"home \t\t\t$", format(homeSizePrice, ">6.2f"))
    print("Frequency surcharge for", homeFrequencyTxt, "cleaning \t$", format(homeFrequencyPrice, ">6.2f"))
    print("Add-ons selected",homeOptionsTxt,"\t\t$", format(homeOptionsPrice, ">6.2f"))
    if (typeSeniorDiscount.upper() == "Y"): # Display senior citizen discount if applicable
        print("Senior Citizen discount (subtract) \t\t$", format(typeSeniorDiscountPrice, ">6.2f"))    
    print("\t\t\t\t\t\t---------")
    print("GRAND TOTAL  \t\t\t\t\t$", format(homeFinalPrice, ">6.2f"))
    print("\t\t\t\t\t\t---------")

# Yard Services
# -------------------------------
def inputYardSvs():

    # Prompt customer for square footage of the lawn 
    print("Please provide the square footage of your lawn: ")
    yardSqFtMowing = int(input())
            
    # Prompt customer for linear footage of edging
    print("Please provide the linear footage of your edging: ")
    yardLinearFtEdging = int(input()) 
            
    # Prompt customer for optional add on services
    print("Please provide the number of shrubs to trim: ")
    yardNumShrub = int(input())
        
    return(yardSqFtMowing, yardLinearFtEdging, yardNumShrub)

# -------------------------------
def calculateYardSvs(yardSqFtMowing, yardLinearFtEdging, yardNumShrub):   

    # Calculate cost for mowing based on square footage
    yardSqFtMowingPrice = 25 + (yardSqFtMowing * 0.02)

    # Calculate cost for edging based on lineare square feet
    yardLinearFtEdgingPrice = 10 + (yardLinearFtEdging * 0.05)

    # Calculate cost of shrub trimming based on number of shrubs
    yardNumShrubPrice = 20 + (yardNumShrub * 0.1)

    # Calculate the final price
    yardFinalPrice = yardSqFtMowingPrice + yardLinearFtEdgingPrice + yardNumShrubPrice

    return(yardSqFtMowingPrice, yardLinearFtEdgingPrice, yardNumShrubPrice, yardFinalPrice)

# -------------------------------
def calculateYardSeniorDiscount(typeSeniorDiscount, yardFinalPrice):
    if (typeSeniorDiscount.upper() == "Y"): # Calculate senior citizen discount if applicable
        typeSeniorDiscountPrice = yardFinalPrice * 0.05
        yardFinalPrice = yardFinalPrice - typeSeniorDiscountPrice
    else:
        typeSeniorDiscountPrice = 0
    return(typeSeniorDiscountPrice, yardFinalPrice)

# -------------------------------
def displayYardEst(typeSeniorDiscount, typeSeniorDiscountPrice, yardSqFtMowing, yardLinearFtEdging, yardNumShrub, yardSqFtMowingPrice, yardLinearFtEdgingPrice, yardNumShrubPrice, yardFinalPrice):

    # Display final cost of the cleaning services
    print(" ")
    print("""Estimate for yard services: \n""")
    print("Mowing for", yardSqFtMowing, "square feet \t\t\t$", format(yardSqFtMowingPrice, ">6.2f"))
    print("Edging for", yardLinearFtEdging, "linear square feet \t\t$", format(yardLinearFtEdgingPrice, ">6.2f"))
    print("Shrub trimming for", yardNumShrub, "shrubs \t\t\t$", format(yardNumShrubPrice, ">6.2f"))
    if (typeSeniorDiscount.upper() == "Y"): # Display senior citizen discount if applicable
        print("Senior Citizen discount (subtract) \t\t$", format(typeSeniorDiscountPrice, ">6.2f"))   
    print("\t\t\t\t\t\t---------")
    print("GRAND TOTAL  \t\t\t\t\t$", format(yardFinalPrice, ">6.2f"))
    print("\t\t\t\t\t\t---------")



#--- Execute --------------------------------------------------------
    
main()
