# Adan Landeros
# Lab Section 4
# Final Project
# 11/19/25

# Program Description
# This program will allow the user to enter products to be shipped, including quantity, weight, and cost. Then it will calculate the subtotal, tax, shipping and handling, and the total due. 
# Also, if user enters 'CA" as the state abbreviation, an 8% tax will be applied to the subtotal



# Create functions 
# user greeting function 
def user_greeting():
    print('This program lets the user enter products to be shipped and calculates the')
    print('subtotal, tax, shipping and handling, and the total due.')
    print()
# state abbreviation list
statesList = ('AL','AK', 'AZ', 'AR', 'CA' , 'CO' , 'CT' , 'DE' , 'FL' , 'GA' , 'HI' ,'ID' , 'IL' , 'IN' , 'IA' , 'KS' , 'KY' , 'LA' , 'ME' , 'MD' , 'MA' , 'MI' , 'MN' ,'MS' , 'MO' , 'MT' , 'NE' , 'NV' , 'NH' , 'NJ' , 'NM' , 'NY' , 'NC' , 'ND' , 'OH' ,'OK' , 'OR' , 'PA' , 'RI' , 'SC' , 'SD' , 'TN' , 'TX' , 'UT' , 'VT' , 'VA' , 'WA' ,'WV' , 'WI' , 'WY')
# function for state abbreviations/error check
def error_check_state():
    while True:
        # get state user input/error check state
        state = input('Please enter the 2 letter abbreviation of the state you are shipping to: ').upper()
        while state not in statesList:
           # if state abbreviation is invalid prompt user to re enter (error check user input)
           state = input('ERROR - Please enter the 2 letter abbreviation of the state you are shipping to: ').upper()
        else:
            # if user input is valid, value will be returned to state variable
            return state
        
        
# function error check itemWeight and itemCost
def error_check_items(value, identifier):
    while True:
        try:
            # get user input for the item weight
           ## itemWeight = float(input('Enter the weight of one item in lbs: '))
            value = float(value)
           
            # get user input for the item cost
            ##itemCost = float(input('Enter the cost of one item in dollars and cents:'))
            # return valid input after error check into itemWeight and itemCost within function
            
            # error check identifier to determine which value to parce/return
            return value
        # except block for invalid input/errorchecking    
        except ValueError:
            if identifier == 'item weight':
                value = input('ERROR - Please enter a valid number for weight: ')
            elif identifier == 'item cost':
                value = input('ERROR - Please enter a valid number for cost: ')
            continue
        



# function for getting product info 
def get_product_info():
    # create lists for item info
    product_info_list = []
    # set variabe to control loop
    listAgain = True
    # initiate loop for getting product info
    while listAgain == True:
        # get user input for item quantity that will be stored in itemQuantityList
        itemQuantity = (input('Enter quantity of item(enter 0 if done): '))
        itemQuantity = error_check_item_quantity(itemQuantity)
        # if statement to exit loops if user enters 0
        if itemQuantity == 0:
            listAgain = False
        # user is prompted to enter item weight and cost if quantity is not 0
        else:
            itemWeight = input('Enter the weight of one item in lbs: ')
            itemWeight = error_check_items(itemWeight, 'item weight')
            itemCost = input('Enter cost of one item in dollars and cents: ')
            itemCost = error_check_items(itemCost, 'item cost')
           ## error_check_items(itemWeight, itemCost)
            # append user input to lists that were previously created 
            product_info_list.append([itemQuantity, itemWeight, itemCost])   
            print()
    # return product info list to main program  
    return product_info_list

        
# function for error checking item quantity input using try/except
def error_check_item_quantity(itemQuantity):
    while True:
        try:
            itemQuantity = int(itemQuantity)
            return itemQuantity
        except ValueError:
            itemQuantity = input('ERROR - Please enter a valid number for quantity: ')
            continue
# function for calculations of subtotal, shipping and handling
def calculations(productInfoList):
    subtotal = 0
    boxweight = 0
    shipping_handling = 0

    # iterate through productInfoList to calculate subtotal, boxweight, shipping, and handling using index numbers to access those values 
    for i in range(len(productInfoList)):
        quantity = productInfoList[i][0]
        weight = productInfoList[i][1]
        cost = productInfoList[i][2]
        boxweight += (quantity * weight)
        subtotal += (quantity * cost)

        # calculate shipping 
        shipping = boxweight * 0.25

        # handling costs determination/calculation
        if boxweight < 10:
            handling = 1.00
        elif boxweight > 100:
            handling = 5.00
        else:
            handling = 3.00
        
        # calculate shipping and handling    
        shipping_handling = shipping + handling

        print()
    # retrun subtotal and shipping/handling outside of function (back into list variable in main program)
    return [subtotal, shipping_handling]

# function for user option to run program again/fulfill another order
def user_option():
    choice = input('Would you like to fullfill another order? (y/n): ').lower()
    # error check user input for choice
    while choice not in ('y' ,'n'):
        choice = input('ERROR - Please enter "y" or "n": ').lower()
    if choice in ('y'):
            return True
    return False


        
    

#----------Main-------------
# calling user greeting function
user_greeting()
# create program loop
run = True
# initiate main program loop
while run == True:
    # call function to get product info and set it = to variable to store returned list/value
    productInfoList = get_product_info()
    
    # call calculations function and set returned values to results variable (shipping/handling and subtotal calculations)
    subTotalMain, shippingHandlingMain = calculations(productInfoList)
   
    # state/select & error check state abbreviation function call (if user input is valid, value will be returned to stateSelect variable)
    stateSelect = error_check_state()
    print()
    # if/else statement to determine tax based on state abbreviation (CA = 8% tax, all others = 0% tax)
    if stateSelect == 'CA':
        tax = subTotalMain * 0.08
    else:
        tax = 0.00
     # calculate total due
     # total_due = subtotal + tax + shipping_handling
    total_due = tax + subTotalMain + shippingHandlingMain
    # print results w/ formatting (decimal places, commas, etc)   
    print(format('Subtotal:','<25'), format(subTotalMain, '>10,.2f'))
    print(format('Tax:','<25'), format(tax, '>10,.2f'))
    print(format('Shipping and Handling:','<25'), format(shippingHandlingMain, '>10,.2f'))
    print(format('Total Due:','<25'), format(total_due, '>10,.2f'))
    
    print()
    print()
    # call user option function to determine if program will run again
    run = user_option()
    print()
# user exit message
print()
print('Have a great day!')



    