def is_even():
    number = int(input("Enter a number - "))
    if number % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_even())