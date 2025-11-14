def kg_to_lbs():
    kgint = float(input('Enter the weight of object in Kg - '))
    lbs = kgint * 2.205
    lbs = round(lbs, 2)
    return lbs
    
def liters_to_gallons():
    literint = float(input('Enter the volume of liquid in Litres - '))
    gallons = literint / 3.785
    gallons = round(gallons, 2)
    return gallons

if __name__ == '__main__':
    print(kg_to_lbs())
    print(liters_to_gallons())