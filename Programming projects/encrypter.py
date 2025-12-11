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

def encrypt_file(filename):
    '''
    Reads a file, shuffles its lines, 
    and saves the result and key.
    Args:
    filename: The name of the file to encrypt.
    Returns:
    None.
    '''
    # open the file 
    f = open(filename, 'r')
    rlines = f.readlines()
    f.close()

    linesl = []
    for line in linesl:
        if len(line) > 0 and line[-1] == '\n':
            linesl.append(line[:-1])
        else:
            linesl.append(line)
    
    # create a list line numbers
    line_indices = []
    count = len(linesl)
    
    for i in range(count):
        line_indices.append(i + 1)
        
    random.seed(125)
    
    # swap lines 
    swaps = count * 5
    for i in range(swaps):
        # pick two random indexes
        idx1 = random.randint(0, count - 1)
        idx2 = random.randint(0, count - 1)
        
        # swap the text lines
        temp_line = linesl[idx1]
        linesl[idx1] = linesl[idx2]
        linesl[idx2] = temp_line
        
        # swap the corresponding line numbers
        temp_index = line_indices[idx1]
        line_indices[idx1] = line_indices[idx2]
        line_indices[idx2] = temp_index
        
    # write the encrypted lines to a new file
    f = open("encrypted.txt", "w")
    for i in range(count):
        f.write(linesl[i])
        if i < count - 1:
            f.write("\n")
    f.close()
    
    f = open("index.txt", "w")
    for idx in line_indices:
        f.write(str(idx) + "\n")
    f.close()