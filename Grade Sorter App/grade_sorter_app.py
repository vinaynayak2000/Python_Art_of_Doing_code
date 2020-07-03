print("Welcome to the Grade Sorter App")
#Empty list
grades=[]
#user input for grades
grade_1=int(input("\nWhat is your first grade (0-100): "))
grade_2=int(input("What is your second grade (0-100): "))
grade_3=int(input("What is your third grade (0-100): "))
grade_4=int(input("What is your fourth grade (0-100): "))
#grades entered in the list
grades=[grade_1,grade_2,grade_3,grade_4]
print("\nYour grades are: "+str(grades))
#reversed
grades.sort(reverse=True)
print("\nYour grades from highest to lowest are: "+str(grades))
#grades removed
print("\nThe lowest two grades will now be dropped.")
r_grade_1= grades.pop()
r_grade_2=grades.pop()
#print
print("Removed grade: "+str(r_grade_1))
print("Removed grade: "+str(r_grade_2))
print("\nYour remaining grades are: "+str(grades))
print("Nice work! Your highest grade is a "+str(grades[0]))
