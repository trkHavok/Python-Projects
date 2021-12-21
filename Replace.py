vowels = ['a', 'e', 'i', 'o', 'u', 'y']
dash = "-"
user_input = input("Please enter a word:")
word = list(user_input)

for letter in word:
    if(letter in vowels):
        letter = dash
    print(letter, end = "")

        

    