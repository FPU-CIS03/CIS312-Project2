#Mayra Merino
#Ingredient adjuster
print("Nestle Chocolate Chip cookies")

cookies = float(input('How many chocolate chip cookies do you want to make?'))

print("To make", cookies, "chocolate chip cookies you will need the following items:")

#Recipe calculations
import math

flour_cups = 2.25/60 * cookies

bakingsoda_tsp = 1/60 * cookies

salt_tsp = 1/60 * cookies

butter_cups = 1/60 * cookies

granulated_sugar_cups = .75/60 * cookies

brown_sugar_cups = .75/60 * cookies

vanilla_tsp = 1/60 * cookies

eggs = 2/60 * cookies

chocolate_chips_oz = 12/60 * cookies

#Cost of ingredients
cost_flour = 1.89/4 * flour_cups

cost_baking_soda = 1.48/96 * bakingsoda_tsp

cost_salt = .89/156 * salt_tsp

cost_butter = 2.88/1 * butter_cups

cost_granulated_sugar = 2.56/8 * granulated_sugar_cups

cost_brown_sugar = 1.74/4 * brown_sugar_cups

cost_vanilla = 6.92/12 * vanilla_tsp

cost_eggs = 2.99/12 * eggs

cost_chocolate_chips = 2.69/12 * chocolate_chips_oz

#total equation
total_cost = cost_flour + cost_baking_soda + cost_salt + cost_butter + cost_granulated_sugar + cost_brown_sugar + cost_vanilla + cost_eggs + cost_chocolate_chips

#Display adjusted ingredients
print(format(flour_cups, '.2f'),"cups of flour. It will cost you about $",format(cost_flour, '.2f'))
print(format(bakingsoda_tsp,'.2f'),"teaspoons of baking soda. It will cost you about $", format(cost_baking_soda, '.2f'))
print(format(salt_tsp,'.2f'), "teaspoons of salt. It will cost you about $", format(cost_salt, '.2f'))
print(format(butter_cups, '.2f'), "cups of butter. It will cost you about $", format(cost_butter, '.2f'))
print(format(granulated_sugar_cups,'.2f'), "cups of granulated sugar. It will cost you about $", format(cost_granulated_sugar, '.2f'))
print(format(brown_sugar_cups, '.2f'), "cups of brown sugar. It will cost you about $", format(cost_brown_sugar, '.2f'))
print(format(vanilla_tsp, '.2f'), "teaspoons of vanilla. It will cost you about $", format(cost_vanilla, '.2f'))
print(math.ceil(eggs),'eggs. They will cost you about $', format(cost_eggs, '.2f'))
print(format(chocolate_chips_oz, '.2f'), "oz of chocolate chips. It will cost you about $", format(cost_chocolate_chips, '.2f'))
print("The total cost to make",cookies,"cookies is: $", format(total_cost, '.2f'))
print("______________________________________________________________________")

#original recipe
recipe = input("Would you like to see the original Nestle Chocolate Chip cookie recipe? Enter yes or no.\n ")
if recipe == 'yes':
    print("The following recipe is the original and will make 5 dozen chocolate chip cookies")
    print("2.25 cups of flour")
    print("1 teaspoon of baking soda")
    print("1 teaspoon of salt")
    print("1 cup of butter")
    print(".75 cups of granulated sugar")
    print(".75 cups of brown sugar")
    print("1 teaspoon of vanilla extract")
    print("2 eggs")
    print("2 cups of Nestle Toll House chocolate chips")
else:
    print("Enjoy your cookies!")
        





