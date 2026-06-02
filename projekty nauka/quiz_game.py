
questions = ("What is the capital of France?",
              "What is the largest planet in our solar system?", 
              "What is the chemical symbol for gold?", 
              "Who painted the Mona Lisa?", 
              "What is the longest river in the world?")

options = (("A. London", "B. Berlin", "C. Paris", "D. Madrid"),
           ("A. Jupiter", "B. Saturn", "C. Mars", "D. Venus"),
           ("A. Ag", "B. Au", "C. Al", "D. Fe"),
           ("A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"),
           ("A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"))

answers = ("C", "A", "B", "C", "B")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)

    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer is {answers[questions_num]}")
    questions_num += 1

print("-----------------------------")
print("        Quiz completed!")
print("-----------------------------")
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = score / len(questions) * 100
print(f"Your score is: {score}%")