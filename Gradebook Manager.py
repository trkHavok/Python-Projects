classes = {"English": [90,95,91],
           "Math": [85,81,99],
           "History": [100,81,91,85],
           "Science": [71,90,85,88]
          }
def average(grades):
    num_scores = len(grades)
    avg = sum(grades) / num_scores
    return avg

def bestGrade(grades):
     answer = max(grades)
     return answer

def worstGrade(grades):
     answer = min(grades)
     return answer
    
def gradelist(grades):
    for i in grades:
        print("Scores:", i)

def delete(grades):
    global subject
    newGrade = int(input("what grade should we delete:"))
    if newGrade not in grades:
        print("-- ERROR - that score doesn't exist")
        print("New scores for",subject,":", grades)
    else:
        grades.remove(newGrade)
        print("New scores for",subject,":", grades,"\n")
    return grades

def add(grades):
    newGrade = int(input("what is the new score:"))
    grades.append(newGrade)
    return grades

def replace(grades, oldNum, newNum):
    grades.remove(oldNum)
    grades.append(newNum)
    return grades
        
def update(grades):
    global subject
    print("Your Scores in ", subject, "\n", grades)
    nextOption = input("what would you like to do (add, update, delete or done): ")
    while nextOption != "done":
        if nextOption == "add":
            newGrades = add(grades)
            print("New scores for", subject, ":", newGrades)
            grades = newGrades
            nextOption = input("what would you like to do (add, update, delete or done): ")
        elif nextOption == "update":
            oldScore = int(input("what score should be updated:"))
            if oldScore in grades:
                newScore = int(input("what should it be replaced with:" ))
                grades = replace(grades, oldScore, newScore)
                print("New scores for",subject,":", grades)
                nextOption = input("what would you like to do (add, update, delete or done): ")        
            else:
                print("-- ERROR - that score doesn't exist")
                print("New scores for",subject,":", grades)
        elif nextOption == "delete":
            newGrades = delete(grades)
            grades = newGrades
            nextOption = input("what would you like to do (add, update, delete or done): ")
        else:
            print("-- ERROR - that command doesn't exist")
            nextOption = input("what would you like to do (add, update, delete or done): ")            
   
 

print("| Welcome to gradebook manager! | \n")
print("You are enrolled in:")
for key in classes:
    print(key)

subject = input("What subject (or 'done'):")
while subject not in classes:
    if subject == "done":
        quit()
    else:
        print("-- ERROR - that class doesn't exist")
        subject = input("What subject (or 'done'):")

userInput = input("what would you like (avg, best, worst, list, update or done):")

while userInput != "done":
    if userInput == "avg":
        print("your average is:", average(classes[subject]) )
        userInput = input("what would you like (avg, best, worst, list, update or done):")
    elif userInput == "best":
        print("your best grade is:", bestGrade(classes[subject]) )
        userInput = input("what would you like (avg, best, worst, list, update or done):")
    elif userInput == "worst":
        print("your worst grade is:", worstGrade(classes[subject]) )
        userInput = input("what would you like (avg, best, worst, list, update or done):")
    elif userInput == "list":
        gradelist(classes[subject])
        userInput = input("what would you like (avg, best, worst, list, update or done):")
    elif userInput == "update":
        update(classes[subject])
        userInput = input("what would you like (avg, best, worst, list, update or done):")
    else:
        print("-- ERROR - that command doesn't exist")
        userInput = input("what would you like (avg, best, worst, list, update or done):")
    


