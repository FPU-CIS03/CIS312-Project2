#CIS_312_Week6_PythonProject2_Jaramillo

posole_servings=20

print("Every year for the Winter Holidays I make Chicken Tomatillo Posole. The recipe calls for \
1 lb small tomatillos, 1 lb Pasilla Chiles, one 5lb can of mexican style hominy, 3 garlic cloves, 1 tsp salt, \
1/2 gallon of water, 1 tsp of black ground pepper, 1 bushel of cilantro, 2 tbls of olive oil, and 1 large onion, 3 lbs of chicken breast \
and 1/2 gallon of chicken stock. The provided recipe is for 20 servings. This progam is designed to allow the cook to enter the number of servings desired \
ingredients required and the projected total cost of the ingredients ")

print()

#Prompts the user for the number of servings desired.
servings=input("Enter number of desired servings: ")

print()

#set total cost to zero.
totalCost = 0

#sets desired servings as the variable integer y.
y=(int(posole_servings))

#Based on original recipe, calculates amount necessary of each ingredient based on user input.
pasilla_chiles=(y/5)*1
tomatillos=(y/5)*1
hominy=(y/20)*1
garlic=(y/20)*3
salt=(y/5)*(1/8)
water=(y/5)*(1/2)
pepper=(y/1)*(1/8)
cilantro=(y/20)*1
olive_oil=(y/5)*(1/8)
chicken=(y/20)*3
onion=(y/1)*1
stock=(y/20)*1

# Used to calculate the price of each ingredient based on prices and quanitities 
costofpasilla_chiles=(y/1)*1
costoftomatillos=(y/1)*1
costofhominy=(y/4)*1
costofgarlic=(y/1)*3
costofsalt=(y/1)*(1/8)
costofwater=(y/2)*(1/2)
costofpepper=(y/1)*(1/8)
costofcilantro=(y/1)*1
costofolive_oil=(y/1)*(1/8)
costofchicken=(y/10)*3
costofonion=(y/1)*1
costofstock=(y/4)*1

    
print()

#Lists quantity needed of each item as well as individual and total costs.
print("You will need: " "\n"
      +str(pasilla_chiles) + " pounds of pasilla chiles will cost" + " $"+str(format(costofpasilla_chiles,".2f"))+ "\n"
      +str(tomatillos) + "pounds of tomatillos will cost" + " $"+str(format(costoftomatillos,".2f")) + "\n"
      +str(hominy) + " cans of hominy will cost" + " $"+str(format(costofhominy,".2f")) + "\n"
      +str(salt) + " teaspoons of salt will cost" + " $"+str(format(costofsalt, ".2f")) + "\n"
      +str(water) + " gallons of water will cost" + " $"+str(format(costofwater, ".2f")) + "\n"
      +str(pepper) + " teaspoons of pepper will cost" + " $"+str(format(costofpepper, ".2f")) + "\n"
      +str(cilantro) + " bushels of cilantro will cost" + " $"+str(format(costofcilantro,".2f")) + "\n"
      +str(olive_oil) + " teaspoons of olive oil will cost" + " $"+str(format(costofolive_oil,".2f")) + "\n"
      +str(chicken) + " pounds of chicken will cost " + " $"+str(format(costofchicken,".2f")) + "\n"
      +str(onion) + " pounds of onion will cost " + " $"+str(format(costofonion,".2f")) + "\n"
      +str(stock) + " cups of chicken stock will cost " + " $"+str(format(costofstock,".2f")) + "\n"
      +"For a grand total of:" + " $"+str(format(totalCost,".2f")) + "\n"
      +"\n"
      +(" Grill tomatillos and chiles and blend with water. Blend garlic, onion and cilantro with chile and tomatillo mix.")
      +(" Boil chiken until cooked and add hominy and green tomatillo mix along with chicken stock, pepper and salt. Serve hot and enjoy"))
