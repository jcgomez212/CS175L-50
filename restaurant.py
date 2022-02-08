#CS175L_50
#Juliana Gomez
#restaurant.py

vegetarian = False
vegan = False
gluten_free = False

response = input('Is anyone in your party vegetarian? ')
if response == 'yes':
    vegetarian = True

response = input('Is anyone in your party vegan? ')
if response == 'yes':
    vegan = True

response = input('Is anyone in your party gluten-free? ')
if response == 'yes':
    gluten_free = True

print('Here are your restaurant choices: ')

if vegetarian == False and vegan == False and gluten_free == False:
    print("Joe's Gourmet Burgers")
    print("Main Street Pizza Company")
    print("Corner Café")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")

if vegetarian == True and vegan == False and gluten_free == True:
    print("Main Street Pizza Company")

if vegetarian == True and vegan == True and gluten_free == True:
    print("Corner Café")
    print("The Chef's Kitchen")

if vegetarian == True and vegan == False and gluten_free == False:
    print("Mama's Fine Italian")
    
    
