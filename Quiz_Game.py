#Python QUIZ GAME

#---------------------

def new_game():
    
#Creating a LIST called "guesses"

    guesses = []
    correct_guesses = 0
    question_num = 1

# for loop which prints the keys from questions dictionary

    for key in questions:
        print("---------------------")
        print(key)

# Nested for loop to print out options per question. Since the first
# index starts at 0, we set the question_num variable to 1 (above) and
# will subtract 1 to start at index 0

        for i in options[question_num-1]:
            print(i)

        guess = input("Enter (A, B, C, or D: )")

# Setting guess to equal guess input with upper method to alleviate case-sensitive error

        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

#---------------------

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

#---------------------

def display_score(correct_guesses, guesses):
    print("---------------------")
    print("RESULTS")
    print("---------------------")
    for i in guesses:
        print(questions.get(i), end=" ")

    print()

    score = int((correct_guesses/len(questions))* 100)
    print("Your score is: " +str(score)+ "%")

#---------------------

def play_again():

    response = input("Do you want to play again? (yes/no)")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# Using a DICTIONARY collection/data structure to hold <K,V> pairs
# We create a dictionary entitled "questions" which holds our key
# in the form of questions

questions = {

    "Who created Python?": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group? ": "C",
    "Is the Earth round?: ": "A"
}

# Next we utitlize an additional collection to hold all the possible answers. In this case,
# we'll rely on the LIST. A 2D list to be exact (list of lists)

options = [[
            "A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           [ "A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           [ "A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           [ "A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

# Here we call new game function to decide whether to play again

while play_again():
    new_game()
    

print("Goodbye!")
