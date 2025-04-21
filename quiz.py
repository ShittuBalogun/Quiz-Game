def quiz():
    score = 0
    print("Welcome to the Quiz Game!")
    print("Please type the letter of your answer (a, b, c, or d) or True/False where applicable.\n")

    # Question 1
    print("1. What is the capital of Nigeria?")
    print("a) Berlin\nb) Madrid\nc) Abuja\nd) Rome")
    answer1 = input("Your answer: ").lower()
    if answer1 == 'c':
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is c) Paris.\n")

    # Question 2
    print("2. Python is a type of snake. (True/False)")
    answer2 = input("Your answer: ").capitalize()
    if answer2 == "True":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is True.\n")

    # Question 3
    print("3. Which planet is known as the Red Planet?")
    print("a) Earth\nb) Mars\nc) Jupiter\nd) Saturn")
    answer3 = input("Your answer: ").lower()
    if answer3 == 'b':
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is b) Mars.\n")

    # Question 4
    print("4. The square root of 64 is:")
    print("a) 6\nb) 8\nc) 7\nd) 9")
    answer4 = input("Your answer: ").lower()
    if answer4 == 'b':
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is b) 8.\n")

    # Question 5
    print("5. Water boils at 100 degrees Celsius. (True/False)")
    answer5 = input("Your answer: ").capitalize()
    if answer5 == "True":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is True.\n")

    # Final score
    print(f"Quiz Complete! Your final score is: {score} out of 5.")
    if score == 5:
        print("Excellent! 🎉")
    elif score >= 3:
        print("Good job! 👍")
    else:
        print("Do better next time! 💪")

# Run the quiz
quiz()

