"""
Ananth Mugundhan
CSC 110
Project - 8
A program to check benfords law on given 
data in a csv file
"""
import csv

def csv_to_list(file_name):
    """
    Reads a CSV file, skips the header, and returns a list of
    all valid number strings from the file.

    Args:
        file_name (str): The name of the CSV file to read.
    Returns:
        list: A list of strings representing valid numbers.
    """
    lst = []
    try:
        f = open(file_name, 'r')
        reader = csv.reader(f)
        next(reader, None)
        
        for row in reader:
            # Loop through every item in the row
            for item in row:
                value = item.strip()
                
                if value:
                    try:
                        cleaned_value = value.replace(",", "").replace("$", "")
                        float(cleaned_value)
                        lst.append(value)
                    except ValueError:
                        continue
                    
        f.close()
    #Checks for errors
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return lst

def count_start_digits(list_digits):
    """
    Counts the occurrences of the first non-zero digit (1-9) for each
    number string in the list.

    Args:
        list_digits (list): A list of strings representing numbers.
    Returns:
        dict: A dictionary with keys 1-9 and their corresponding counts.
    """
    dictionary_count = {1: 0, 2: 0, 3: 0 , 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    
    # Loop through each number string in the list
    for num_str in list_digits:
        if num_str:
            for char in num_str:
                if char.isdigit() and char != '0':
                    dictionary_count[int(char)] += 1
                    break
    return dictionary_count

def digit_percentages(counts):
    """
    Takes a dictionary of counts and returns a new dictionary
    with the percentage of each count, rounded to two decimal places.

    Args:
        counts (dict): A dictionary with keys 1-9 and their counts.
    Returns:
        dict: A dictionary with keys 1-9 and their corresponding percentages.
    """
    percentages = {
    1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0}
    total = 0
    for i in range(1,10):
        total += counts[i]

    if total == 0:
        return percentages

    for i in range(1, 10):
        count = counts[i]
        percentages[i] = round((count / total) * 100, 2)
    return percentages

def print_plot(percentages):
    """
    Prints a bar chart of the percentages.
    The number of '#' is the integer part of the percentage.

    Args:
        percentages (dict): A dictionary with keys 1-9 and their percentages.
    Returns:
        None
    """
    for i in range(1,10):
        print('{} | {}'.format(i, '#' * int(percentages[i])))


def check_benfords_law(percentages):
    """
    Checks if the percentages follow Benford's Law within the
    specified tolerances (-5% to +10%).

    Args:
        percentages (dict): A dictionary with keys 1-9 and their percentages.
    Returns:
        bool: True if the percentages follow Benford's Law, False otherwise.
    """
    # The expected percentages for Benford's Law
    benford_law = {1: 30, 2: 17, 3: 12, 4: 9, 5: 7, 6: 6, 7: 5, 8: 5, 9: 4}
    
    for i in range(1, 10):
        percent = percentages[i]
        expected = benford_law[i]
        
        lower_bound = expected - 5
        upper_bound = expected + 10
        
        if not (lower_bound <= percent <= upper_bound):
            return False
            
    # If all digits are within the range, it follows the law
    return True