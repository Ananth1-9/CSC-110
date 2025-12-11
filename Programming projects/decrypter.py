'''
Ananth Mugundhan
CSC110
Project - 13
This program decrypts a text file using a key file.
It restores the original order of the shuffled lines.
'''

def decrypt_file(text_file, key_file):
    '''
    Reads encrypted text and key, restores order, and saves to file.
    Args:
    text_file: the name of the encrypted file.
    key_file: the name of the index key file.
    Returns:
    None.
    '''
    # open the encrypted text file
    f = open(text_file, 'r')
    raw_lines = f.readlines()
    f.close()
    
    # Clean the lines to remove newlines
    encrypted_lines = []
    for line in raw_lines:
        if len(line) > 0 and line[-1] == '\n':
            encrypted_lines.append(line[:-1])
        else:
            encrypted_lines.append(line)
            
    # open the index key file
    f = open(key_file, 'r')
    index_lines = f.readlines()
    f.close()
    
    count = len(encrypted_lines)
    
    # create a list of the correct size filled with placeholders
    decrypted_lines = []
    for i in range(count):
        decrypted_lines.append("")
        
    # loop through the encrypted lines and place them in correct spots
    for i in range(count):
        current_line = encrypted_lines[i]
        idx_str = index_lines[i].strip()
        if len(idx_str) > 0:
            original_index = int(idx_str) - 1
            decrypted_lines[original_index] = current_line
        
    f = open("decrypted.txt", "w")
    for i in range(count):
        f.write(decrypted_lines[i])
        if i < count - 1:
            f.write("\n")
    f.close()
