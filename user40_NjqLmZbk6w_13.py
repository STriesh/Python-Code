# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """
    :param name: is one of the strings from the following list:
    {"rock", "Spock", "paper", "lizard", "scissors"}
    :return: a number in the range of 0-4 representing the name(guess)

    """
    # delete the following pass statement and fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    
    throw_number = None
    
    if name == "rock":
        throw_number = 0
    elif name == "Spock":
        throw_number = 1
    elif name == "paper":
        throw_number = 2
    elif name == "lizard":
        throw_number = 3
    elif name == "scissors":
        throw_number = 4
    else:
        print "Error: " , name, " is an Invalid guess!"
        print "Valid guess list: " , "rock, Spock, paper, lizard, scissors"

    return throw_number
 

def number_to_name(number):
    
    """
    :param number: is an integer whose value is one of the following:
    {0,1,2,3,4}
    :return: a string representing a guess whose value is one of the following:
     {"rock", "Spock", "paper", "lizard", "scissors"}

    """
    # delete the following pass statement and fill in your code below
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    throw_name = None
    if number == 0:
        throw_name = "rock"
    elif number == 1:
        throw_name = "Spock"
    elif number == 2:
        throw_name = "paper"
    elif number == 3:
        throw_name = "lizard"
    elif number == 4:
        throw_name = "scissors"
    else:
        print "Error: " , number, " is outside of range!"
        print "Valid range: " , "0, 1, 2, 3, 4"

    return throw_name
    
    

def rpsls(player_choice): 
    """
    :param player_choice: valid guess whose value is one of the following:
    {"rock", "Spock", "paper", "lizard", "scissors"}
    :return:
    prints player guess, computer guess, and result of game

    """
    # delete the following pass statement and fill in your code below
    
    import random
    
    # print a blank line to separate consecutive games
    
    print ""
    
    # print out the message for the player's choice
    
    print "Player Chooses", player_choice

    # convert the player's choice to player_number using the function name_to_number()

    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()

    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    
    name_comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    
    print "Computer Chooses", name_comp_choice

    # compute difference of comp_number and player_number modulo five

    game_result = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message

    if game_result >= 1 and game_result <= 2 :
        print "Computer wins!"
    elif game_result >= 3 :
        print "Player wins!"
    else:
        print "Player and computer tie!"
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


