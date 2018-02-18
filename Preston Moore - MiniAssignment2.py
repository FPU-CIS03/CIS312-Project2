#MiniAssignment2 - By Preston Moore

print("Welcome to Big Soft Ginger Cookies Cost Calculator! - By Preston Moore")
print("______________________________________________________________________\n")
num = int(input("How many Big Soft Ginger Cookies would you like to bake? "))


#ingredient list below itemized by the ratio of how much/two doven * num to find amout for any amout of cookies
flo = float(format(((2.25/24)*num),".2f"))
floCost = float(format((flo*.20),".2f"))
gin = float(format(((2/24)*num),".2f"))
ginCost = float(format((gin*.03),".2f"))
bakS = float(format(((1/24)*num),".2f"))
bakSCost = float(format((bakS*.03),".2f"))
cin = float(format(((.75/24)*num),".2f"))
cinCost = float(format((cin*.1),".2f"))
salt = float(format(((.25/24)*num),".3f"))
saltCost = float(format((salt*.02),".2f"))
marg = cin
margCost = float(format((marg*.8),".2f"))
sug = float(format(((2/24)*num),".2f"))
sugCost = float(format((sug*.75),".2f"))
egg = float(format(((1/24)*num),".0f"))

#must utilize at least a single egg, even if a low number of cookies is desired
if egg == 0 and num > 0 :
    egg = 1
eggCost = float(format((egg*.5),".2f"))
cost = float(format((floCost+ginCost+bakSCost+saltCost+margCost+sugCost+eggCost),".2f"))

print("Your recipe requires :\n\t",flo," cups of flour, costing approximately $",floCost,sep="")
print("\t",gin," teaspoons of ginger, costing approximately $",ginCost,sep="")
print("\t",bakS," teaspoons of baking soda, costing approximately $",bakSCost,sep="")
print("\t",cin," teaspoons of cinnemon, costing approximately $",cinCost,sep="")
print("\t",salt," teaspoons of salt, costing approximately $",saltCost,sep="")
print("\t",marg," cups of margin, costing approximately $",margCost,sep="")
print("\t",sug," cups of sugar, costing approximately $",sugCost, sep="")
print("\t",egg," eggs, costing approximately $",eggCost, sep="")

print("\t","\nYour total ingredient cost is approximately $",cost, sep="")

#optional frosting add on
nice = input("\nWould you like to add frosting? Enter y for yes or n for no. ")

#user must choose y or n, any other input trigers continuous loop
while nice != 'y' and nice != 'n' :
  nice = input("Invalid input! Please enter 'y' for yes or 'n' for no. ")
if nice == 'y' :
  frostCost = float(format(float(num*(3.00/24)),".2f"))
  print("\nThis will cost an additional $",frostCost," bringing your total cost to $",float(format((cost+frostCost),".2f")),sep="")
elif nice == 'n' :
    print("No frosting? No problem. Read below for baking instructions.")
else :
    
    print("Invalid Please")
    
#instructions below, conditional for frosting option
print("\n1) Preheat oven to 350 degrees F (175 degrees C). Sift together the flour, ginger, baking soda, cinnamon, cloves, and salt. Set aside.")
print("\n2) In a large bowl, cream together the margarine and 1 cup sugar until light and fluffy. Beat in the egg, then stir in the water and molasses. Gradually stir the sifted ingredients into the molasses mixture. Shape dough into walnut sized balls, and roll them in the remaining 2 tablespoons of sugar. Place the cookies 2 inches apart onto an ungreased cookie sheet, and flatten slightly.")
print("\n3) Bake for 8 to 10 minutes in the preheated oven. Allow cookies to cool on baking sheet for 5 minutes before removing to a wire rack to cool completely. Store in an airtight container.")

if nice == 'y':
    print("\n 4) Spread frosting evenly over cookies while warm and enjoy!")

truth = input("\nWould you like to enter feedback? Enter 'y' for yes or 'n' for no! ")
while truth != 'y' and truth != 'n' :
  truth = input("Invalid input! Enter 'y' for yes or 'n' for no! ")
if truth == 'y' :
  input("We value your feedback! Enter your feedback.")
  print("Thank you for your feedback and using Big Soft Ginger Cookies Cost Calculator! Please come again!")
else :
  print("Thank you for using Big Soft Ginger Cookies Cost Calculator! Please come again!")
