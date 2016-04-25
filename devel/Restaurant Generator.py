# Final Project - Random Restaurant Generator
# Chelsea Holbrook

import random

tryAgain = True
def generator():
    print('Welcome to the Restaurant Generator!')
    print('We solve debates in a matter of seconds!')
    print('Please choose from these types of restaurants:')
    print('American, Asian, Indian, Italian, Latin, Mediterranean, or Any')

    choice = input()
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
            print('Press Enter to go back to the beginning.')
            input()


while tryAgain:
    generator()
