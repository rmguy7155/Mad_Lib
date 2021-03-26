# Name: Rebecca Guy
# Course: COP1500
# Description: Word Lib and fun conversations for the family.

###############################################################################
import random


def main():

    # begin introduction ########################################################

    # prompt user for their name and store to variable name
    name = input("Hey there. What's your name? ")
    # prompt user for last name, this will be used within the story
    # capitalize first letter of the name

    last_name = input("What's your last name? ")

    print("\nHey,", name.capitalize(), last_name.capitalize() + ", nice name you've got there.")

    # prompt user to name the program for entertainment
    my_name = input("I don't have a name yet. What should I be called? ")
    # print statement thanking user for name choice
    print("\nThanks! I love it. '", my_name.capitalize(), "' is great!", sep='')

    # ask for age
    age = int(input("How old are you " + '' + name.capitalize() + "? "))
    # to incorporate multiplication, addition, and division
    print("That's awesome! I'm ", format(age*11+7/3 - 4**2%1//3, '.2f'), "years old!")
    # ask user for favorite letter, this will be used in the story
    letter = input("What is your favorite letter of the alphabet? ")

    # define function,do_you_know: opens text file to explain what a Mad Lib
    def do_you_know():
        text = open('DoYouKnow.txt').read()
        return text

    # asks user if they've ever heard of Mad Libs
    answer1 = input("So, this program is a Mad Lib. Have you heard of Mad Libs? ")
    while True:
        # if user enters yes, the program will move on
        if answer1.lower() == 'yes':
            print(" ")
            print("Great! Let's fill in the blanks for some wordy fun!")
            print("After we choose the words, \nI will show you our story!")
            break
        # if the user enters no, it will explain what a Mad Lib is
        elif answer1.lower() == 'no':
            print(" ")
            print(open('DoYouKnow.txt').read())
            break
        else:
            # this will prompt if user doesn't answer 'yes' or 'no'
            print("I'm not sure what you meant.")
            answer1 = input("Have you heard of Mad Libs? You can type 'yes' or 'no'. ")

    answer2 = input("\nSo, are you ready to get started? ")
    if answer2.lower() == 'yes':
        print("Okay, ", name.capitalize(), "! Let's have some fun!", sep='')
    else:
        print("Well... ", name.capitalize(), ", here we go anyways!", sep='')

    # end introduction ###############################################################

    # definition of adjectives and nouns #############################################

    print("\nFor our story, we will need adjectives and nouns. ")
    # ask user if they would like to know what an adjective is
    adjective_question = input("Would you like to know what an adjective is? ")
    # if user selects yes, print the definition of adjective with an example
    if adjective_question.lower() == 'yes':
        print("\nAn adjective is a word used to describe a person, a place, or a thing.")
        print("For example: The 'red' car. The 'smelly' dog. Both 'red' and 'smelly' are adjectives.\n")
    # ask user if they would like to know what an noun is
    noun_question = input("Would you like to know what a noun is? ")
    # if user selects yes, print the definition of noun with an example
    if noun_question.lower() == 'yes':
        print("\nA noun is a word used to name a person, a place, or a thing.")
        print("For example: The red 'car'. The smelly 'dog'. Both 'car' and 'dog' are nouns.\n")


    proceed = input("When you're ready to begin, type 'yes'. ")
    while proceed.lower() != 'yes':
        proceed = input("Type 'yes' to continue. ")

    print("\nOkay, whenever you would like me to choose a word, type 'you choose'.")

    def countdown(n):
        if n == 0:
            print("Let's go!")
        else:
            print(n)
            countdown(n - 1)

    countdown(3)
    print(" ")

    # choosing words for the story ####

    def random_adj():  # define function to call random adjective from adjectives.txt
        # open list, assign random element to random_adjective
        random_adjective = random.choice(list(open('adjectives.txt')))
        # return value for random_adjective and removes the space after the final letter
        return random_adjective.rstrip()

    def random_nouns():  # function to call random noun from nouns.txt
        # open list, assign random element to random_nouns
        random_noun = random.choice(list(open('nouns.txt')))
        # return value for random_noun and removes the space after the final letter
        return random_noun.rstrip()

    def random_plural_nouns():  # function to call random noun from nouns.txt
        # open list, assign random element to random_nouns
        random_plural_noun = random.choice(list(open('pluralNouns.txt')))
        # return value for random_noun and removes the space after the final letter
        return random_plural_noun.rstrip()

    def random_exp():
        random_expression = random.choice(list(open('expressions.txt')))
        return random_expression.rstrip()

    story = open('story.txt', 'r')
    new_story = open("new_story.txt", "w")

    noun_list = []
    adj_list = []
    for line in story:
        if '(adj)' in line:
            adjective = input("Choose an adjective: ")
            if adjective == 'you choose':
                adjective = random_adj()
                print(random_exp(), " '", adjective, "' ", sep="")
            new_story.write(line.replace('(adj)', adjective))
            adj_list.append(adjective)
        elif '(noun)' in line:
            noun = input("Choose a noun: ")
            if noun == 'you choose':
                noun = random_nouns()
                print(random_exp(), " '", noun, "' ", sep="")
            new_story.write(line.replace('(noun)', noun))
            noun_list.append(noun)
        elif '(plural_noun)' in line:
            plural_noun = input("Choose a plural noun. (Plural means more than one): ")
            if plural_noun == 'you choose':
                plural_noun = random_plural_nouns()
                print(random_exp(), " '", plural_noun, "' ", sep="")
            new_story.write(line.replace('(plural_noun)', plural_noun))
            noun_list.append(plural_noun)
        elif '(letter)' in line:
            new_story.write(line.replace('(letter)', letter.capitalize()))
        elif '(last_name)' in line:
            new_story.write(line.replace('(last_name)', last_name.capitalize()))
        else:
            new_story.write(line)



    print("\nGreat choices! Our adjectives are:")
    print(*adj_list, sep= ", ")
    print(" ")

    print("\nAnd our nouns are:")
    print(*noun_list, sep= ", ")
    print(" ")

    story.close()
    new_story.close()

    print("Okay! Our story is ready. ")
    proceed_story = input("Are you ready to read our story? Type 'yes' to proceed. ")

    while proceed_story.lower() != 'yes':
        proceed_story = input("Type 'yes' to continue. ")
    print(" ")
    print(" ")

    read_story = open('new_story.txt', 'r')
    print(read_story.read())

    for i in range(3, 0, -1):
        print(i)
    print("The End!")

main()




