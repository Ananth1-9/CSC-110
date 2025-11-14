def validate_age(age):
    if age.isnumeric() == True:
        return True
    else:
        return False

def check_eligibility(age):
    if age>=18:
        return True
    else:
        return False
    

    
