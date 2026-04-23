print(" Student Score Tracker: Enter student names and their scores.")

def get_student_scores():
    student_scores = {}
    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            score = float(input(f"Enter score for {name}: "))
            student_scores[name] = score
        except ValueError:
            print("Please enter a valid score.")
    return student_scores
def display_scores(student_scores):
    print("\nStudent Scores:")
    for name, score in student_scores.items():
        print(f"{name}: {score}")
scores = get_student_scores()
display_scores(scores)
