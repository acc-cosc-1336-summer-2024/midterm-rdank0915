#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_bonus_pay_amount(sales): #Defines the parameter which will be used to determine the bonus percentage
    if(sales < 0):
        return("Invalid Arguments")      #All of these
    if(sales >= 0 and sales <= 499):     #lines outline
        bonus_percent = 0.05             #the ranges for
    if(sales > 499 and sales <= 999):    #the various
        bonus_percent = 0.06             #bonus percent
    if(sales > 999 and sales <= 1499):   #levels
        bonus_percent = 0.07
    if(sales > 1499 and sales <= 1999):
        bonus_percent = 0.08
    if(sales > 1999):
        return("Invalid Arguments")
    
    bonus = sales * bonus_percent #This calculates the total bonus earned
    return(bonus)