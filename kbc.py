import time
import random

# Sample questions
questions = [
    ["Which programming language is known as the backbone of web development?", "HTML", "CSS", "JavaScript", "Ruby", 3],
    ["What does the acronym 'HTTP' stand for in web technology?", "HyperText Transmission Protocol", "HyperText Transfer Protocol", "HyperText Translation Protocol", "HyperText Transaction Protocol", 2],
    ["Who is known as the father of the World Wide Web?", "Tim Berners-Lee", "Steve Jobs", "Bill Gates", "Mark Zuckerberg", 1],
    ["Which company developed the popular video game 'Fortnite'?", "Blizzard Entertainment", "Epic Games", "Valve Corporation", "Electronic Arts", 2],
    ["What was the first programmable computer called?", "ENIAC", "UNIVAC", "Colossus", "Z3", 4],
    ["In which year was the first iPhone released?", "2007", "2008", "2009", "2010", 1],
    ["Which of the following is a database management system?", "Python", "MySQL", "HTML", "CSS", 2],
    ["Which of the following is not a programming language?", "Python", "Swift", "Ruby", "PhotoShop", 4],
    ["What is the main function of a router in a computer network?", "To store data", "To connect devices wirelessly", "To manage traffic between networks", "To protect against viruses", 3],
    ["Which of the following is used to style web pages?", "HTML", "CSS", "XML", "JavaScript", 2]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

# Lifelines
lifelines = {
    "50-50": 1,
    "Audience Poll": 1,
    "Phone a Friend": 1
}

def use_lifeline(lifeline, question):
    if lifeline == "50-50":
        options = [question[5] - 1]
        while len(options) < 2:
            opt = random.randint(0, 3)
            if opt != question[5] - 1:
                options.append(opt)
        options_text = [question[i + 1] for i in options]
        print(f"50-50 Lifeline used! The options are: {options_text}")
    elif lifeline == "Audience Poll":
        print("Audience Poll Lifeline used! The audience suggests the correct answer is option", question[5])
    elif lifeline == "Phone a Friend":
        print("Phone a Friend Lifeline used! Your friend suggests the correct answer is option", question[5])

def ask_question(question, level):
    print(f"\n\nQuestion for Rs.{level}")
    print(f"Q: {question[0]}")
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    start_time = time.time()
    reply = input("Enter your answer (1-4) or type 'lifeline' to use a lifeline: ").strip()
    if reply.lower() == "lifeline":
        print("Available lifelines:", [lifeline for lifeline, count in lifelines.items() if count > 0])
        chosen_lifeline = input("Which lifeline would you like to use? ").strip()
        if chosen_lifeline in lifelines and lifelines[chosen_lifeline] > 0:
            use_lifeline(chosen_lifeline, question)
            lifelines[chosen_lifeline] -= 1
            reply = input("Enter your answer (1-4): ").strip()
        else:
            print("Invalid or used lifeline! Please answer the question.")
            reply = input("Enter your answer (1-4): ").strip()
    elapsed_time = time.time() - start_time
    if elapsed_time > 30:
        print("Time's up! You didn't answer in time.")
        return False
    return int(reply) == question[-1]

for i in range(0, len(questions)):
    if ask_question(questions[i], levels[i]):
        print(f"Correct answer, you have won {levels[i]}")
        if i == 4:
            money = levels[4]
        elif i == 9:
            money = levels[9]
    else:
        print("Wrong answer or time out.")
        break

print(f"Your take-home money is Rs.{money}")

