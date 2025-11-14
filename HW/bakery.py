def calculate_tax(p, b = 0.07):
    final_price = p+ (p * 0.07)
    return final_price

def calculate_total(a, b, c):
    cupcake_price = a*3.5
    cupcake_total = calculate_tax(cupcake_price)
    croissant_price = b*5
    croissant_total = calculate_tax(croissant_price)
    bagel_price = c*2.5
    bagel_total = calculate_tax(bagel_price)
    total_price = cupcake_total + croissant_total + bagel_total
    total_price = round(total_price, 2)
    return total_price


total_after_tax = calculate_total(5,1,6)
print(total_after_tax)
print(calculate_total (0,3,0))

