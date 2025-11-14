def feet_to_inches(feet):
    """
    Convert feet to inches.
    """
    inches = round(feet * 12)
    return inches

def feet_to_meters(feet):
    """
    Convert feet to meters.
    """
    meters = round(feet/3.281, 2)
    return meters

print(feet_to_inches(1))
print(feet_to_inches(2.5))
print(feet_to_inches(5.4))
print(feet_to_meters(1))
print(feet_to_meters(5))
print(feet_to_meters(20))