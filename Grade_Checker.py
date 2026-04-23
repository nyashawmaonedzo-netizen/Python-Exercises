score = int(input("Enter your score (0-100): "))

if score >= 90:
    letter = 'A'
elif score >= 80:
    letter = 'B'
elif score >= 70:
    letter = 'C'
elif score >= 60:
    letter = 'D'
else:
    letter = 'F'
print(f"Your score {score} is Equivalent to the {letter} Grade.")   