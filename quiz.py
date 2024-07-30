



questions = [
    {
        "prompt": "Who is the first President of India?",
        "options": ["A. APJ Abdul kalam", "B. Narendra Modi", "C. Jawaharlal Nehru ", "D. Rajendra Prasad"],
        "answer": "D"
    },
    {
        "prompt": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. None"],
        "answer": "A"
    },
    {
        "prompt": "What is the primary language  of India?",
        "options": ["A. English", "B. Hindi", "C. Urdu", "D. Arabic"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote Romeo and Juliet?",
        "options": ["A. William Shekspeare", "B. Premchand", "C. Kiosaki", "D. Charles Dickens"],
        "answer": "A"
    },
    {
        "prompt": "What is the smallest prime no ?",
        "options": ["A. 1", "B. 0", "C. 2", "D. -1"],
        "answer": "C"
    },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter you Answer (A, B, C or D): ").upper()
        if answer == question["answer"]:
            print("Corrrect wowww!\n")
            score += 1
        else:
            print("wrong Looooser!!!  The corrent answer was", question["answer"],  "\n")
        

  


    print(f"You got {score} out of {len(questions)} questions correct")
    


run_quiz(questions)