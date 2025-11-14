'''
Ananth Mugundhan
CSC 110
Project -9
A simple spellcheck progam
'''

def read_spellings():
    """
    This function reads the 'misspellings.txt' file and constructs a dictionary
    Args:
        None
    Returns:
        dict: A dictionary where keys are misspelled words (lowercase) and values
              are the correct spellings (lowercase).
    """
    misspellings = {}
    try:
        with open('misspellings.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split('->')
                if len(parts) == 2:
                    incorrect = parts[0].strip().lower()
                    correct = parts[1].strip().lower()
                    misspellings[incorrect] = correct
    except FileNotFoundError:
        print(f"Error: Required file '{'misspellings.txt'}' not found.")
        return {}
    return misspellings

def process_word(word, spell_dict):
    """
    Checks a single word against the misspellings dictionary, handling 
    capitalization and trailing punctuation, and returns the corrected word.
    Args:
        word (str): The word to be checked and corrected.
        spell_dict (dict): The dictionary of misspellings.
    Returns:
        str: The corrected word with original capitalization and punctuation.
    """
    punctuation = {'.', ',', ';', '?', '!'}
    if not word:
        return ""

    trailing_punctuation = ""
    original_word = word
    
    if original_word[-1] in punctuation:
        trailing_punctuation = original_word[-1]
        if len(original_word) > 1:
            word_without_punc = original_word[:-1]
        else:
            word_without_punc = ""
            
    else:
        word_without_punc = original_word

    if not word_without_punc:
        return trailing_punctuation

    is_capitalized = False
    
    if word_without_punc and word_without_punc[0].isupper():
        is_capitalized = True
    
    lookup_word = word_without_punc.lower()
    
    corrected_word_base = lookup_word

    if lookup_word in spell_dict:
        corrected_word_base = spell_dict[lookup_word]

    if is_capitalized:
        final_word = corrected_word_base.capitalize()
    else:
        final_word = corrected_word_base

    final_word += trailing_punctuation

    return final_word

def correct_spelling(input_filename, spell_dict):
    """
    Reads an input text file, corrects misspellings using the dictionary,
    and writes the result to an output file.

    Args:
        input_filename (str): The name of the file to be spell-checked.
        spell_dict (dict): The dictionary of misspellings.
    """
    output_filename = f"output_{input_filename}"
    output_lines = []

    try:
        with open(input_filename, 'r') as infile:
            for line in infile:
                original_line_ending = line[len(line.rstrip()):]

                content = line.strip() 

                if not content:
                    output_lines.append('\n')
                    continue

                words = content.split(' ')
                
                new_line_words = []
                for word in words:
                    if word:
                        corrected_word = process_word(word, spell_dict)
                        new_line_words.append(corrected_word)

                output_lines.append(' '.join(new_line_words) + original_line_ending)
        
        with open(output_filename, 'w') as outfile:
            outfile.writelines(output_lines)

    except:
        print('ERROR')
