print("Welcome to the MPH to MPS Conversion App")
#Takes the user input
mph=input("\nWhat is your speed in miles per hour: ")
#Converts into float
fmph=float(mph)
#Calculation of miles per hour to meters per second
mps=fmph*0.44704
#Rounds the value upto 2 decimal point.
fmps=round(mps,2)
#prints the output
print("Your speed in meters per second is",str(fmps))
