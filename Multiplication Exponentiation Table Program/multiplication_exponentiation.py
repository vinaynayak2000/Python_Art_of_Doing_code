print("Welcome to the Multiplication/Exponent Table App")
#Takes user input
name = input("What is your name: ")
number = float(input("What number would you like to work with: "))
message = name + " Math is cool!"

print("\nMultiplication Table For "+str(number))
#multiplication table
print("\n1.0 * "+str(number)+" = "+str(round((1.0*number),4)))
print("2.0 * "+str(number)+" = "+str(round((2.0*number),4)))
print("3.0 * "+str(number)+" = "+str(round((3.0*number),4)))
print("4.0 * "+str(number)+" = "+str(round((4.0*number),4)))
print("5.0 * "+str(number)+" = "+str(round((5.0*number),4)))
print("6.0 * "+str(number)+" = "+str(round((6.0*number),4)))
print("7.0 * "+str(number)+" = "+str(round((7.0*number),4)))
print("8.0 * "+str(number)+" = "+str(round((8.0*number),4)))
print("9.0 * "+str(number)+" = "+str(round((9.0*number),4)))

print("\nExponent Table For "+str(number))
#Exponential table
print("\n"+str(number)+" ** 1 = "+str(round((number**1),4)))
print(str(number)+" ** 2 = "+str(round((number**2),4)))
print(str(number)+" ** 3 = "+str(round((number**3),4)))
print(str(number)+" ** 4 = "+str(round((number**4),4)))
print(str(number)+" ** 5 = "+str(round((number**5),4)))
print(str(number)+" ** 6 = "+str(round((number**6),4)))
print(str(number)+" ** 7 = "+str(round((number**7),4)))
print(str(number)+" ** 8 = "+str(round((number**8),4)))
print(str(number)+" ** 9 = "+str(round((number**9),4)))
#Print showing different methods
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())


