print("Welcome to the Letter Counter App")
#Takes user name and prints the name 
name = input("What is your name: ").title().strip()
print("Hello",name,"!")
#Takes the message and ask for the letter for which the occurrences is to be found
print("I will count the number of times that a specific letter occurs in a message.")
message = input("\nPlease enter a message: ").lower()
letter = input("Which letter would you like to count the occurrences of: ").lower()
#counts and prints
letter_count = message.count(letter)
print("\n"+name+", your message has",str(letter_count),letter+"'s in it.")