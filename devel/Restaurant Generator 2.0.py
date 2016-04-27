# Final Project - Random Restaurant Generator
# Chelsea Holbrook

import random

tryAgain = True

AmcnFd = ['310 Lakeside', 'American Kitchen Bar & Grill', 'Artisans Table', "B.B. King's Blues Club",
    'Canvas Restaurant', 'Citron, An American Brasserie']
AznFd = ['Amura', 'Benihana', 'Kabooki Sushi', 'Kobe Steakhouse',
    'Mikado Japanese Steakhouse', 'Morimoto Asia']
IndnFd = ['Aashirwad', 'Bombay Cafe', 'Mynt', 'Saffron Insian Cuisine', 'Shalimar Classic Indian Restaurant',
    'Tamarind Indian Cuisine']
ItlnFd = ['Adriatico Trattoria Italiana', 'Andiamo', 'BRAVO Cucina Italiana', 'BRIO Tuscan Grille',
    'Buca di Beppo', 'Cafe Trastevere']
LtnFd = ['Bandeja Paisa', 'Bongos', 'Cocina 214', 'Cuba Libre', 'Gallettos Spanish & Portuguese Cuisine',
    "Pepe's Cantina"]
MedFd = ['Carmel Kitchen', 'Krazy Greek Kitchen', 'The Peppy Bistro', 'Shiraz Grill',
    'Taverna Opa', 'Villa de Flora']
Any = ['310 Lakeside', 'Aashirwad', 'Adriatico Trattoria Italiana',
    'American Kitchen Bar & Grill', 'Amura', 'Andiamo', 'Artisans Table',
    "B.B. King's Blues Club", 'Bandeja Paisa', 'Benihana', 'Bombay Cafe',
    'Bongos', 'BRAVO Cucina Italiana', 'BRIO Tuscan Grille',
    'Buca di Beppo', 'Cafe Trastevere', 'Canvas Restaurant', 'Carmel Kitchen',
    'Citron, An American Brasserie', 'Cocina 214', 'Cuba Libre',
    'Gallettos Spanish & Portuguese Cuisine', 'Kabooki Sushi', 'Kobe Steakhouse',
    'Krazy Greek Kitchen', 'Mikado Japanese Steakhouse',
    'Morimoto Asia', 'Mynt', "Pepe's Cantina", 'Saffron Insian Cuisine',
    'Shalimar Classic Indian Restaurant', 'Shiraz Grill',
    'Tamarind Indian Cuisine', 'Taverna Opa', 'The Peppy Bistro', 'Villa de Flora']

ZipCodes = ['32746', '32789', '32801', '32803', '32804', '32809', '32811',
'32819', '32821', '32827', '32830', '32837', '34746']


FourSix = ['Krazy Greek Kitchen', 'Mikado Japanese Steakhouse']
EightNine = ['BRIO Tuscan Grille', 'Carmel Kitchen', 'Cocina 214', 'Mynt',
"Pepe's Cantina", 'Tamarind Indian Cuisine']

OhOne = ['310 Lakeside', 'Artisans Table', 'Amura']
OhThree = ['Cafe Trastevere', 'Kabooki Sushi']
OhFour = ['Adriatico Trattoria Italiana', 'The Peppy Bistro']
OhNine = ['Bombay Cafe', 'Buca di Beppo']
OneOne = 'Gallettos Spanish & Portuguese Cuisine'
OneNine = ['Aashirwad', "B.B. King's Blues Club", 'BRAVO Cucina Italiana',
    'Cuba Libre', 'Kobe Steakhouse', 'Saffron Indian Cuisine',
    'Shalimar Classic Indian Restaurant', 'Taverna Opa']
TwoOne = ['Benihana', 'Shiraz Grill']
TwoSeven = 'Canvas Restaurant'
ThreeOh = ['American Kitchen Bar & Grill', 'Andiamo', 'Bongos', 'Morimoto Asia']
ThreeSev = ['Bandeja Paisa', 'Citron, An American Brasserie']
ThreeFour = 'Villa de Flora'





def generatorType():
    print('Please choose from these types of restaurants:')
    print('American, Asian, Indian, Italian, Latin, Mediterranean, or any of these.')
    choice = input()
    if choice == 'American':
        print(AmcnFd[random.randint(0, len(AmcnFd) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == 'Asian':
        print(AznFd[random.randint(0, len(AznFd) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == 'Indian':
        print(IndnFd[random.randint(0, len(IndnFd) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == 'Italian':
        print(ItlnFd[random.randint(0, len(ItlnFd) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == 'Latin':
        print(LtnFd[random.randint(0, len(LtnFd) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == 'Mediterranean':
        print(MedFd[random.randint(0, len(MedFd) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()
        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == 'Any':
        print(Any[random.randint(0, len(Any) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Please enter a valid choice, try again.')
            input()

def generatorZip():
    print('What is your zip code?')
    choice = input()

    if choice not in ZipCodes:
        print('Please choose from these zip codes:')
        print('32746,', ' 32789,', ' 32801,', ' 32803,', ' 32804,', ' 32809,',
        ' 32811,', ' 32819,', ' 32821,', ' 32827,', ' 32830,', ' 32837,', ' or 34746.')
        choice = input()


    if choice == '32746':
        print(FourSix[random.randint(0, len(FourSix) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32789':
        print(EightNine[random.randint(0, len(EightNine) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32801':
        print(OhOne[random.randint(0, len(OhOne) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32803':
        print(OhThree[random.randint(0, len(OhThree) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32804':
        print(OhFour[random.randint(0, len(OhFour) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()

        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32809':
        print(OhNine[random.randint(0, len(OhNine) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()
        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32811':
        print(OneOne[random.randint(0, len(OneOne) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()
        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32819':
        print(OneNine[random.randint(0, len(OneNine) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()
        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32821':
        print(TwoOne[random.randint(0, len(TwoOne) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()
        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32827':
        print(TwoSeven[random.randint(0, len(TwoSeven) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()
        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32830':
        print(ThreeOh[random.randint(0, len(ThreeOh) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()
        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '32837':
        print(ThreeSev[random.randint(0, len(ThreeSev) - 1)])
        print('Is this okay?')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()
        else:
            print('Press Enter to go back to the beginning.')
            input()

    elif choice == '34746':
        print(ThreeFour)
        print('Is this okay? I hope so, because it is the closest one to you!')
        answer = input()

        if answer == 'Yes':
            tryAgain = False
            print('Great! Enjoy your meal! See README for the address.')
            input()
            exit()
        else:
            print('Press Enter to go back to the beginning.')
            input()


    else:
        print('Please enter a valid choice, try again.')
        input()


def welcome():
    print('Welcome to the Restaurant Generator!')
    print('We solve debates in a matter of seconds!')
    print('Would you like to choose by type of meal or location?')
    answer = input()

    if answer == 'Type':
        generatorType()
    elif answer == 'Location':
        generatorZip()
    else:
        return "Please use the words 'Type' or 'Location'"

welcome()
while tryAgain:
    welcome()
