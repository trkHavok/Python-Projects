classAvg = {'English': (85),
            'I/T': (92),
            'Math': (74),
            'Science': (79),
            'basketweaving': (70)}

classes = input("What class are you looking for?")
grade = classAvg[classes]
if  93 <= grade <= 100:
    letter_grade = 'A'
elif 90 <= grade <= 92:
    letter_grade = 'A-'
elif 87 <= grade <= 89:
    letter_grade = 'B+'
elif 83 <= grade <= 86:
    letter_grade = 'B'
elif 80 <= grade <= 82:
    letter_grade = 'B-'
elif 76 <= grade <= 79:
    letter_grade = 'C+'
elif 70 <= grade <= 75:
    letter_grade = 'C'
elif 67 <= grade <= 69:
    letter_grade = 'C-'
elif 63 <= grade <= 66:
    letter_grade = 'D+'
elif 60 <= grade <= 62:
    letter_grade = 'D'
elif 0 <= grade <= 59:
    letter_grade = 'F'

print("The class you choose was", classes, "and the letter grade is",letter_grade,", with an average of:",classAvg[classes])