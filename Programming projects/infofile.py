'''
Ananth Mugundhan
CSC110
Project - 10
A program that reads a text file and produces
an information file based on the text
'''
def text_to_list(filename):
    """
    Reads the file, strips newlines, and splits lines by whitespace
    to create a list of all words.
    Args:
        filename (str): The name of the file to read.
    Returns:
        list: A list of words from the file.
    """
    words = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line_words = line.strip().split()
                words.extend(line_words)
    except FileNotFoundError:
        print("Error")
    return words

def count_words(word_list):
    """
    Counts the occurrences of each word in the list.
    Args:
        word_list (list): A list of words.
    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    counts = {}
    for word in word_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def most_frequent(word_counts):
    """
    Finds the most frequent small (0-4), medium (5-7),
    and large (8+) words.
    Args:
        word_counts (dict): A dictionary with
        words as keys and their counts as values.
    Returns:
        tuple: A tuple containing the most frequent
        small, medium, and large words.
    """
    small = (None, -1)
    medium = (None, -1)
    large = (None, -1)

    for word, count in word_counts.items():
        length = len(word)
        
        if 0 <= length <= 4:
            if count > small[1]:
                small = (word, count)
        elif 5 <= length <= 7:
            if count > medium[1]:
                medium = (word, count)
        elif length >= 8:
            if count > large[1]:
                large = (word, count)

    return (small[0], medium[0], large[0])

def count_sizes(word_counts):
    """
    Counts the number of UNIQUE words in each size category.
    Args:
        word_counts (dict): A dictionary with words
        as keys and their counts as values.
    Returns:
        tuple: A tuple containing counts of
        small, medium, and large words.
    """
    s, m, l = 0, 0, 0
    for word in word_counts:
        length = len(word)
        if 0 <= length <= 4:
            s += 1
        elif 5 <= length <= 7:
            m += 1
        elif length >= 8:
            l += 1
    return (s, m, l)

def count_capitalized(word_counts):
    """
    Counts the number of UNIQUE capitalized and 
    non-capitalized words.
    Args:
        word_counts (dict): A dictionary with words
        as keys and their counts as values.
    Returns:
        tuple: A tuple containing counts of
        capitalized and non-capitalized words.
    """
    cap = 0
    non_cap = 0
    for word in word_counts:
        if len(word) > 0 and word[0].isupper():
            cap += 1
        else:
            non_cap += 1
    return (cap, non_cap)

def count_punctuated(word_counts):
    """
    Counts the number of UNIQUE punctuated (ends with . or ,) and 
    non-punctuated words.
    Args:
        word_counts (dict): A dictionary with words
        as keys and their counts as values.
    Returns:
        tuple: A tuple containing counts of
        punctuated and non-punctuated words.
    """
    punc = 0
    non_punc = 0
    for word in word_counts:
        if word.endswith('.') or word.endswith(','):
            punc += 1
        else:
            non_punc += 1
    return (punc, non_punc)

def write_results(word_counts, filename):
    """
    Calculates statistics and writes the formatted results to a new file.
    Args:
        word_counts (dict): A dictionary with words
        as keys and their counts as values.
        filename (str): The name of the original file.
    Returns:
        None
    """
    total_unique = len(word_counts)
    
    if total_unique == 0:
        return

    most_freq = most_frequent(word_counts) 
    sizes = count_sizes(word_counts)       
    caps = count_capitalized(word_counts)  
    puncs = count_punctuated(word_counts)  

    if '.' in filename:
        out_name = filename.rsplit('.', 1)[0] + "_results.txt"
    else:
        out_name = filename + "_results.txt"

    with open(out_name, 'w') as f:
        f.write(f"Total number of unique words: {total_unique}\n")
        
        f.write("Most frequent words by size:\n")
        f.write(f"* Small: {most_freq[0]}\n")
        f.write(f"* Medium: {most_freq[1]}\n")
        f.write(f"* Large: {most_freq[2]}\n\n")

        def get_stats(count, total, char):
            val = (count / total) * 100
            pct_str = f"{round(val, 2)}%"
            bar_len = round((count / total) * 50)
            return pct_str, char * bar_len

        s_pct, s_bar = get_stats(sizes[0], total_unique, '#')
        m_pct, m_bar = get_stats(sizes[1], total_unique, '%')
        l_pct, l_bar = get_stats(sizes[2], total_unique, '*')

        f.write("Length:\n")
        f.write(f"* Small: {sizes[0]} ({s_pct})\n")
        f.write(f"* Medium: {sizes[1]} ({m_pct})\n")
        f.write(f"* Large: {sizes[2]} ({l_pct})\n")
        f.write(f"{s_bar}{m_bar}{l_bar}\n\n")

        c_pct, c_bar = get_stats(caps[0], total_unique, '#')
        nc_pct, nc_bar = get_stats(caps[1], total_unique, '%')

        f.write("Capitalization:\n")
        f.write(f"* Capitalized: {caps[0]} ({c_pct})\n")
        f.write(f"* Non-capitalized: {caps[1]} ({nc_pct})\n")
        f.write(f"{c_bar}{nc_bar}\n\n")

        p_pct, p_bar = get_stats(puncs[0], total_unique, '#')
        np_pct, np_bar = get_stats(puncs[1], total_unique, '%')

        f.write("Punctuation:\n")
        f.write(f"* Punctuated: {puncs[0]} ({p_pct})\n")
        f.write(f"* Non-punctuated: {puncs[1]} ({np_pct})\n")
        f.write(f"{p_bar}{np_bar}")