#write functions here, don't add input('') statements here!

def get_miles_per_hour(kilometers, minutes): #Write function to get miles per hour using parameters kilometers and minutes
    
    miles = kilometers * 0.621371 #Equation to get miles
    hour = minutes / 60 #Equation to get hours

    miles_per_hour = miles / hour #Equation to get miles per hour

    if(miles_per_hour < 0):
        return("Invalid Arguments")
    else:
        return(miles_per_hour)