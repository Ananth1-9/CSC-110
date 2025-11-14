'''Ananth Mugundhan
CSC 110
Project - 5
A program that calculates the number of months
 to save for a down payment on a house
'''
def calculate_months(annual_salary, portion_saved, 
                     total_cost, semi_annual_raise):
    '''
    This function calculates the number of months
      to save for a down payment on a house
    Args:
        annual_salary (int): annual salary
        portion_saved (float): portion of salary to be saved
        total_cost (int): total cost of the house
        semi_annual_raise (float): semi annual raise
    Returns:
        returns the number of months to save for
          a down payment on a house'''
    current_savings = 0
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary * portion_saved
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment
    r = 0.04
    months = 0
    #The while loop runs until the current 
    # savings is less than the down payment
    # If the number of months is a multiple of 6, 
    # the monthly salary is increased by the semi annual raise

    while current_savings < down_payment:
        if months%6 == 0 and months !=0:
            monthly_salary = monthly_salary *(1+ semi_annual_raise)
            monthly_savings = monthly_salary * portion_saved
        current_savings += current_savings * r / 12
        current_savings += monthly_savings
        months += 1
    return months
    
