
# A simple grading system that allows user to input their score
#  and return the appropriate grade based off their score

# Create a function to get user's input
def get_score():
    # Creating an infinite loop until user enter's the correct value format
    while True:
        try:
            user_score= float(input("Enter your score (0-100): "))

            # If user inputs a score less than 0 the loop still continues to run
            if user_score<0:
                print("Score cannot be less than zero. Please try again")
                continue
            if user_score>100:
                print("Score cannot be greater than 100. Please try again")
                continue
            # Return the score if it is within the correct range
            return user_score
        except ValueError:
            print("Not what is expected. Please try again")

# Create a function to determine the user grade based off the user input
def get_grade(user_score):
    if user_score>=80 and user_score<=100:
        grade="A"
    elif user_score>=60 and user_score<=79:
        grade="B"
    elif user_score>=50 and user_score<=59:
        grade="C"
    elif user_score>=40 and user_score<=49:
        grade="D"
    elif user_score>=30 and user_score<=39:
        grade="E"
    elif user_score>=0 and user_score<=29:
        grade="F"

    return grade

# Your main function
def main():
    # Assigns the returned score from the function get_score() to score variable
    score=get_score()
    # Assigns the returned grade from the function get_grade to grade variable
    grade=get_grade(score)
    print(f"Your Score is {score} and your grade is {grade}")

main()

