vowels = ['a', 'e', 'i', 'o', 'u', 'y']

letter = ""
while letter != '0':
    letter = input("Enter a letter:")
    if(letter in  vowels):
        print("This letter is a vowel:", letter)
   
