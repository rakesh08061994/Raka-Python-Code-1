# If Condition
# Create a program to ask the user to enter a vowel and print a string if the input meets the conditions:

vowel = ["a","e","i","o","u","A","E","I","O","U"]
letter = input("Enter a vowel: ")
if letter in vowel:
    print("You press", letter)
print("Done ! ")
