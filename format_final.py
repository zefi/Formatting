def fix(initial_sentence):
    answer = initial_sentence.capitalize()
    for char in "abcdefghijklmnopqrstuvwxyz":
        answer = answer.replace(". " + char, ". " + char.upper())    
    answer = answer.replace(" i ", " I ")
    answer = answer.replace(" i.", " I.")
    return answer


initial_sentence = input("\nEnter the word you want to change: ") 
fixed = fix(initial_sentence)
print("Your changed text is:", fixed)

input("\n\nPress enter to exit.")