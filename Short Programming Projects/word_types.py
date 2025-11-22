def count_word_type(filename):
    counts = {'capitalized': 0, 'punctuated': 0, 'other': 0}
    
    try:
        with open(filename, 'r') as f:
            content = f.read()
            words = content.split()
            
            for word in words:
                if word[0].isupper():
                    counts['capitalized'] += 1
                elif not word.isalpha():
                    counts['punctuated'] += 1
                else:
                    counts['other'] += 1
                    
    except FileNotFoundError:
        print("Error")
        
    return counts

def print_plot(counts):
    total_words = sum(counts.values())
    
    if total_words == 0:
        print("No words found.")
        return

    categories = ['capitalized', 'punctuated', 'other']
    
    for category in categories:
        count = counts.get(category, 0)
        percentage = (count / total_words) * 100
        num_hashes = int(percentage) 

        print(f"{category:<14}{percentage:>6.2f}% {'#' * num_hashes}")
