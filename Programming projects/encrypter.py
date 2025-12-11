'''
Ananth Mugundhan
CSC110
Project - 13
This program encrypts a text file by shuffling
its lines randomly.
It saves the encrypted text and a key
file to reconstruct the original order.
'''
import random


import random

def encrypt_file(file_name):
    """
    Encrypt a text file.
    Args:
    file_name: The inputted text file.
    Returns:
    None: Output goes to encrypted.txt and index.txt.
    """

    # Read the lines from the inputted file. 
    lines = []
    f = open(file_name, 'r')
    for line in f:
        line = line.rstrip('\n')
        lines.append(line)
    f.close()

    # Create the indexes. 
    original_indexes = []
    i = 0
    while i < len(lines):
        original_indexes.append(i)
        i += 1

    # The given seed for test cases.
    random.seed(125)

    # Encrypt the lines and indexes. 
    line_count = len(lines)
    i = 0
    while i < line_count * 5:
        a = random.randint(0, line_count - 1)
        b = random.randint(0, line_count - 1)
        temp_line = lines[a]
        lines[a] = lines[b]
        lines[b] = temp_line

        temp_index = original_indexes[a]
        original_indexes[a] = original_indexes[b]
        original_indexes[b] = temp_index
        i += 1

    # Write and export the text to a text file. 
    f = open("encrypted.txt", "w")
    i = 0
    while i < line_count:
        if i < line_count - 1:
            f.write(lines[i] + "\n")
        else:
            f.write(lines[i])
        i += 1
    f.close()

    # Write and export the indexes to an index key file. 
    f = open("index.txt", "w")
    i = 0
    while i < line_count:
        number_to_write = original_indexes[i] + 1
        if i < line_count - 1:
            f.write(str(number_to_write) + "\n")
        else:
            f.write(str(number_to_write))
        i += 1
    f.close()