def greeting():
    """Returns a greeting message with the full name."""
    first_name = input('Enter your first name - ')
    last_name = input('Enter your last name - ')
    full_name = first_name + " " + last_name
    return "Hello, " + full_name 

print(greeting())
