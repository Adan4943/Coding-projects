
# Program Description 

# This program will allow the user to enter the types of fruit and how many pounds of fruit there are for each type
# program will then display info in the form of fruit, weight, one fruit type per line

# User greeting / Program Description
print('This program will let you create a list of fruits and how many ')
print('pounds there are of each and then display them back to you.')
print('When you are done, please press return/enter without entering a fruit.')

print()

# Program loops for appending to list / list creation (memory spot assignment)
fruitList = []
weightList = []
message = 'lbs.'

# initiate program loop (while)
run = True
# start input loop
while run == True:

    # get user input for fruit
    newFruit = input('Please enter a type of fruit: ').title()
   
   # if/else statement for loop  exit/continuation / check user input
    if newFruit == '':
        run = False
    else:
         newWeight = float(input('Please enter the weight of the fruit in pounds: '))
        
        # add input to list
         fruitList.append(newFruit)
         weightList.append(newWeight)

    print()


# initiate index variable to control print loops (allow program to iterate through fruits/weights)
index = 0

# iterate through the lists and display fruit and weight
# add index of 1 for every appended fruit (0 + 1), (1 + 1), (2 + 1), .......
while index < len(fruitList):
    print(format(fruitList[index], '<10') , format(weightList[index],'>11''.2f'), message)

    index = index + 1

print()

# user choice to run program
choice = input('Would you like to enter more fruits? (y or n): ')
while choice not in ('y' , 'n'):
    choice = input('Error, please choose a "y" for yes or "n" for no: ')
if choice in ('n'):
        run = False


# exit message
print()
print('Have a nice day!!!!')
