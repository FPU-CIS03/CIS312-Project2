#Angel Quezada
#Week6
#Mini Project 6.2
import math

pbutter= .95
butter = .5
sugar = .17
egg = .17
flour = .8
vanilla = .35
chips = 1.5


print('Program will display cookie recipe ingredients\n')
print('Type `choco` for chocolate chip, `peanut`')
print('for peanut butter, and `sugar` for sugar\n')
repeat = 'y'

while repeat == 'y':

    choice= str(input('Please enter your choice of cookie recipe\n'))
    amount=int(input('How many cookies would you like to bake?\n'))
    
    if choice == 'choco':
        print('To make ', amount, ' chocolate chip cookies you will need:\n' )
        print('*'*50, '\n')
        print(format((amount*(.5/48)), '.2f'),' cups Butter, will cost approximately $', format((amount*(.5/48))*butter, '.2f') )
        print(format((amount*(1.667/48)), '.2f'),' cups Sugar, will cost approximately $', format((amount*(1.667/48))*sugar, '.2f') )
        print(math.ceil(amount*(2/48)),'    Eggs, will cost approximately $', format((amount*(2.75/48))*egg, '.2f') )
        print(format((amount*(1/48)), '.2f'), ' teaspoons of Vanilla, will cost approximately $', format((amount*(1/48))*vanilla, '.2f') )
        print(format((amount*(2/48)), '.2f'), ' cups of flour, will cost approximately $', format((amount*(2/48))*flour, '.2f') )
        print(format((amount*(2/48)), '.2f'), ' cups of chocolate chips, will cost approximately $', format((amount*(1.667/48))*chips, '.2f'), '\n')
        print('*'*50, '\n')
        
        total = (amount*(.5/48))*butter + (amount*(1.667/48))*sugar + (amount*(2.75/48))*egg + (amount*(1/48))*vanilla + (amount*(2/48))*flour + (amount*(1.667/48))*chips
        print('Total cost for ingredients is: $', format(total, '.2f')
              , '\n')
        print('*'*50, '\n')

        print( 'Recipe can be found at: ')
        print( '\nhttp://www.myrecipes.com/recipe/easiest-ever-chocolate-chip-cookies\n')


        
    elif choice == 'peanut':
        print('To make ', amount, ' peanut butter cookies you will need:\n' )
        print('*'*50, '\n')
        print(format((amount*(1/30)), '.2f'),' cups  Peanut Butter, will cost approximately $', format((amount*(1/30))*pbutter, '.2f') )
        print(format((amount*(1/30)), '.2f'),' cups Sugar, will cost approximately $', format((amount*(1/30))*sugar, '.2f') )
        print(math.ceil(amount*(1/30)),'    Eggs, will cost approximately $', format((amount*(1/30))*egg, '.2f') )
        print(format((amount*(1/30)), '.2f'), ' teaspoons of Vanilla, will cost approximately $', format((amount*(1/30))*vanilla, '.2f') )
        print('*'*50, '\n')
        
        total = (amount*(1/30))*pbutter + (amount*(1/30))*sugar + (amount*(1/30))*vanilla + (amount*(1/30))*egg
        print('Total cost for ingredients is: $', format(total, '.2f')
              , '\n')
        print('*'*50, '\n')

        print( 'Recipe can be found at: ')
        print( '\nhttp://www.myrecipes.com/recipe/easiest-peanut-butter-cookies\n')


    elif choice == 'sugar':
        print('To make ', amount, ' chocolate chip cookies you will need:\n' )
        print('*'*50, '\n')
        print(format((amount*(1/36)), '.2f'),' cups Butter, will cost approximately $', format((amount*(1/36))*butter, '.2f') )
        print(format((amount*(.75/36)), '.2f'),' cups Sugar, will cost approximately $', format((amount*(.75/36))*sugar, '.2f') )
        print(math.ceil(amount*(1/36)),'    Eggs, will cost approximately $', format((amount*(1/36))*egg, '.2f') )
        print(format((amount*(1/36)), '.2f'), ' teaspoons of Vanilla, will cost approximately $', format((amount*(1/36))*vanilla, '.2f') )
        print(format((amount*(2.5/36)), '.2f'), ' cups of flour, will cost approximately $', format((amount*(2.5/36))*flour, '.2f') )
        print('*'*50, '\n')
        
        total = (amount*(1/36))*butter + (amount*(.75/36))*sugar + (amount*(1/36))*egg + (amount*(1/36))*vanilla + (amount*(2.5/36))*flour 
        print('Total cost for ingredients is: $', format(total, '.2f')
              , '\n')
        print('*'*50, '\n')

        print( 'Recipe can be found at: ')
        print( '\nhttp://www.myrecipes.com/recipe/sugar-cookies-5\n')

        
    else:
        print('Invalid Entry')

    print('*'*50, '\n')

    repeat = str(input('Would you like to try again, `y` for yes, `n` for no\n'))
    


















