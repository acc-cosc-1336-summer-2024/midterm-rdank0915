#add import

import question_b

kilometers = int(input("Enter the kilometers: ")) #Write code to prompt the user for kilometers
minutes = int(input("Enter the minutes: ")) #Write code to prompt the user for minutes

miles_per_hour = question_b.get_miles_per_hour(kilometers, minutes)

print("Your speed in mph is: ")
print(miles_per_hour)