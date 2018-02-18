print("This is the ingredients list to make 48 Ultimate chocolate chip cookies: ")
print()
print("3/4 cup granulated sugar")
print("1 cup butter or margarine, softened")
print("1 teaspoon vanilla")
print("1 egg")
print("2 1/4 cup all-purpose flour")
print("1 teaspoon baking soda")
print("1/2 teaspoon salt")
print("1 cup coarsely chopped nuts")
print("1 package (12 ounces) semisweet chocolate chips (2 cups)")

BatchOfCookies = 48
cupsOfGranulatedSugarPer48Cookies = .75
cupsOfBrownSugarPer48Cookies = .75
cupsOfButterPer48Cookies = 1
teaspoonsOfVanilla = 1
eggsPer48Cookies = 1
cupsOfFlourPer48Cookies = 2.25
teaspoonsOfBakingSodaPer48Cookies = 1
teaspoonsOfSaltPer48Cookies = .5
cupsOfNuts = 1
packagesOfChocolateChips = 1
print ()
userNumberOfCookies = int( input( "How many cookies do you want to make: ") )

expectedCupsOfGranulateSugar = ( userNumberOfCookies / BatchOfCookies ) * \
                      cupsOfGranulatedSugarPer48Cookies
expectedCupsOfBrownSugar = ( userNumberOfCookies / BatchOfCookies ) * \
                           cupsOfBrownSugarPer48Cookies
expectedTeaspoonsOfVanilla = ( userNumberOfCookies / BatchOfCookies ) * \
                             teaspoonsOfVanilla
expectedEggs = (userNumberOfCookies / BatchOfCookies ) * \
               eggsPer48Cookies

expectedCupsOfButter = ( userNumberOfCookies / BatchOfCookies ) * \
                       cupsOfButterPer48Cookies

expectedCupsOfFlour = ( userNumberOfCookies / BatchOfCookies ) * \
                      cupsOfFlourPer48Cookies
expectedTeaspoonsOfBakingSoda = ( userNumberOfCookies / BatchOfCookies ) * \
                                teaspoonsOfBakingSodaPer48Cookies
expectedTeaspoonsOfSalt = (userNumberOfCookies / BatchOfCookies ) * \
                          teaspoonsOfSaltPer48Cookies
expectedCupsOfNuts = (userNumberOfCookies / BatchOfCookies ) * \
                     cupsOfNuts
expectedPackagesOfChocolateChips = (userNumberOfCookies / BatchOfCookies) * \
                                   packagesOfChocolateChips
                               
print( "To Make " + str(userNumberOfCookies ) + " cookies, you will need: \n" + \
       format(expectedCupsOfGranulateSugar, ".2f")  + " cups of granulated sugar \n" + \
       format(expectedCupsOfBrownSugar, ".2f") + " cups of brown sugar \n " + \
       format(expectedTeaspoonsOfVanilla, ".2f") + " teaspoon(s) of vanilla \n " + \
       format(expectedEggs, ".2f") + " egg(s) \n" + \
       format(expectedCupsOfButter, ".2f" ) + " cup(s) of butter \n" + \
       format(expectedCupsOfFlour, ".2f" ) + " cup(s) of flour \n " + \
       format(expectedTeaspoonsOfBakingSoda, ".2f") + " teaspoon(s) of baking soda \n" + \
       format(expectedTeaspoonsOfSalt, ".2f") + " teaspoon(s) of salt \n " + \
       format(expectedCupsOfNuts, ".2f" ) + " cup(s) of nuts and \n" + \
       format(expectedPackagesOfChocolateChips, ".2f" ) + " package(s) of chocolate chips" )



granulatedSugarPackCost = 1.99
brownSugarPackCost = 1.79
butterPackCost= 4.99
bottleOfVanillaCost = 4.99
caseOfEggsCost = 3.99
bagOfFlourCost = 1.99
bakingSodaBoxCost = 1.00
saltCost = 2.50
bagOfNuts = 10.00
packagesOfChocolateChipsCost = 2.50

cupsOfSugarPerPack =2
cupsOfBrownSugarPerPack = 3.5
cupsOfButterPerPack= 2
teaspoonsOfVanillaPerBottle= 12
eggsPerCase=12
cupsOfFlourPerBag=7
teaspoonsOfBakingSodaPerBox=91
teaspoonsOfSaltPerContainer=130
cupsOfNutsPerBag=7
cupsOfChocolateChipsPerBag=2

expectedGranulatedSugarPackCost = ((expectedCupsOfGranulateSugar / cupsOfSugarPerPack) * \
                                  granulatedSugarPackCost) + granulatedSugarPackCost
expectedBrownSugarPackCost = ((expectedCupsOfBrownSugar / cupsOfBrownSugarPerPack) * \
                             brownSugarPackCost) + brownSugarPackCost 
expectedButterPackCost=( (expectedCupsOfButter / cupsOfButterPerPack) * \
                        butterPackCost) + butterPackCost
expectedBottleOfVanillaCost = ((expectedTeaspoonsOfVanilla / teaspoonsOfVanillaPerBottle ) * \
                              bottleOfVanillaCost) + bottleOfVanillaCost
expectedCaseOfEggsCost = ((expectedEggs / eggsPerCase) * caseOfEggsCost) + caseOfEggsCost
expectedBagOfFlourCost = ((expectedCupsOfFlour / cupsOfFlourPerBag) * bagOfFlourCost) + bagOfFlourCost
expectedBakingSodaBoxCost = ((expectedTeaspoonsOfBakingSoda /teaspoonsOfBakingSodaPerBox) * \
                            bakingSodaBoxCost) + bakingSodaBoxCost
expectedSaltCost = ((expectedTeaspoonsOfSalt / teaspoonsOfSaltPerContainer) * saltCost) + saltCost
expectedBagOfNuts = ((expectedCupsOfNuts / cupsOfNutsPerBag)*bagOfNuts) + bagOfNuts
expectedPackagesOfChocolateChipsCost = ((expectedPackagesOfChocolateChips/cupsOfChocolateChipsPerBag)*\
                                       packagesOfChocolateChipsCost) + packagesOfChocolateChipsCost

if userNumberOfCookies <=48:
    print()
    print( "To make " + str(userNumberOfCookies ) + " cookies, you will pay: \n" + \
       "$", format(granulatedSugarPackCost, ".2f" ) + " for granulated sugar \n" + \
       "$", format(brownSugarPackCost, ".2f") + " for brown sugar \n " + \
       "$", format(bottleOfVanillaCost, ".2f") + " for vanilla \n " + \
       "$", format(caseOfEggsCost, ".2f") + " for eggs \n" + \
       "$", format(butterPackCost, ".2f" ) + " for butter \n" + \
       "$", format(bagOfFlourCost, ".2f" ) + "for flour \n " + \
       "$", format(bakingSodaBoxCost, ".2f") + "f or baking soda \n" + \
       "$", format(saltCost, ".2f") + " for salt \n " + \
       "$", format(bagOfNuts, ".2f" ) + " for nuts and \n" + \
       "$", format(packagesOfChocolateChipsCost, ".2f" ) + " for chocolate chips" )
else:
    print()
    print( "To make " + str(userNumberOfCookies ) + " cookies, you will pay: \n" + \
       "$", format(expectedGranulatedSugarPackCost, ".2f" ) + " for granulated sugar \n" + \
       "$", format(expectedBrownSugarPackCost, ".2f") + " for brown sugar \n " + \
       "$", format(expectedBottleOfVanillaCost, ".2f") + " for vanilla \n " + \
       "$", format(expectedCaseOfEggsCost, ".2f") + " for eggs \n" + \
       "$", format(expectedButterPackCost, ".2f" ) + " for butter \n" + \
       "$", format(expectedBagOfFlourCost, ".2f" ) + " for flour \n " + \
       "$", format(expectedBakingSodaBoxCost, ".2f") + " for baking soda \n" + \
       "$", format(expectedSaltCost, ".2f") + " for salt \n " + \
       "$", format(expectedBagOfNuts, ".2f" ) + " for nuts and \n" + \
       "$", format(expectedPackagesOfChocolateChipsCost, ".2f" ) + " for chocolate chips" )
print()
print("You estimated total cost is:$", format(expectedGranulatedSugarPackCost + expectedBrownSugarPackCost + \
                                        expectedBottleOfVanillaCost + expectedCaseOfEggsCost + \
                                        expectedButterPackCost + expectedBagOfFlourCost + \
                                        expectedBakingSodaBoxCost + expectedSaltCost + \
                                        expectedBagOfNuts + expectedPackagesOfChocolateChipsCost, ".2f"))


