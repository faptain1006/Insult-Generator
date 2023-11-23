from random import choice 

# get all the inputs
def getInput():
    flag = False
    while (flag == False):
        name = input("Please input the victim's name: ")
        if (name.strip() == ""):
            print("\u001b[31mVictim's name must not be empty or contain only spaces.\033[0m")
        else:
            flag = True        
    
    flag = False
    while (flag == False):
        numberInsults = input("Please input the number of insults: ")
        if (numberInsults.isdecimal() == False) or (int(numberInsults) <= 0):
            print("\u001b[31mThe number of insults must be an integer of one or greater\033[0m")
        else:
            flag = True

    flag = False
    while (flag == False):
        numberAdj = input("Please input the number of adjectives: ")
        if (numberAdj.isdecimal() == False) or (int(numberAdj) <= 0) or (int(numberAdj) > 3):
            print("\u001b[31mThe number of adjectives must be 1, 2, or 3\033[0m")
        else:
            flag = True
    
    return name, int(numberInsults), int(numberAdj)

# object picker function
def objectPicker(object):
    if (object == "adjectives"):
        return choice(("arrogant foolish naive impolite nasty cowardly grumpy boastful ugly useless").split())
    elif (object == "noun"):
        return choice(("bastard jerk cunt wanker ninny dickhead").split())
    elif (object == "color"):
        return choice(("\u001b[31m \u001b[32m \u001b[34m \033[0;36m \033[0;35m \033[1;33m \033[0;33m").split())

# process the insults
def processInsults(name,numberInsults,numberAdj,play):
    
    if (play == True):
        # repeat depending on the number of insults
        for _ in range(numberInsults):

            # loop this process based on selected number of adj
            selectedAdj = ""
            for _ in range(numberAdj):
                adjective = objectPicker("adjectives")
                selectedAdj += adjective + " "
            selectedAdj = selectedAdj.rstrip()
            
            # select the noun
            selectedNoun = objectPicker("noun") 

            #print the output with randomized color
            print(f"{objectPicker('color')}{name} is a {selectedAdj} {selectedNoun}!\033[0m")

    else:
        print(f"{objectPicker('color')}Bye {objectPicker('adjectives')} {objectPicker('noun')}!\033[0m")
 
def main(): 
    play = True
    while play == True:
        # store the inputs in these variables
        name, numberInsults, numberAdj = getInput()

        # process the output
        processInsults(name,numberInsults,numberAdj,play)
        
        # repeat or exit the game
        repeat = input("Type \033[0;33my\033[0m if you want play again: ")
        if (repeat.lower() != "y"): 
            play = False
            processInsults(name,numberInsults,numberAdj,play)
            break
main()
