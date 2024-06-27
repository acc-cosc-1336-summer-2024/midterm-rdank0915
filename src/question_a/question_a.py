#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_bonus_pay_amount(sales): #Defines the parameter which will be used to determine the bonus percentage
    if(sales < 0):
        return("Invalid Arguments")
    if(sales >= 0 and sales <= 499):
        bonus_percent = 0.05
    if(sales > 499 and sales <= 999):
        bonus_percent = 0.06
    if(sales > 999 and sales <= 1499):
        bonus_percent = 0.07
    if(sales > 1499 and sales <= 1999):
        bonus_percent = 0.08
    if(sales > 1999):
        return("Invalid Arguments")
    
    bonus = sales * bonus_percent
    return(bonus)