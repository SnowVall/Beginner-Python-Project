def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    
    if answer == guess:
        print("Benar!")
        return 1
    
    else:
        print("Salah!")
        return 0

def display_score(correct_guesses, guesses):

    print("------------------------")
    print("RESULTS\n")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ",)
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def play_again():
    
    replay = input("Do you want to play again?(Y/n): ").upper()

    if replay == "Y":
        return True
    
    elif replay == "N":
        return False
    
    else:
        print("Yes or no!")
        return play_again()
        

questions = {
    "Bahasa inggris Ikan?:": "A",
    "Bahasa inggris Roda?:": "B",
    "Bahasa inggris Meja?:": "C",
    "Bahasa inggris Makan?:": "C",
}

options = [
    ("A. Fish", "B. Fill", "C. Figure", "D. Sheep"),
    ("A. Road", "B. Wheel", "C. Car", "D. Watch"),
    ("A. Chair", "B. Book", "C. Table", "D.Tall"),
    ("A. Sleep", "B. All", "C. Eat", "D. End")
]

new_game()

while play_again():
    new_game()
