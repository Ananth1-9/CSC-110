def read_words(filename):
    wordbank = []
    f = open(filename, 'r')
    for line in f:
        wordbank.append(line.strip())
    f.close()
    return wordbank

def read_puzzle(filename):
    f = open(filename, 'r')
    puzzle = []
    for line in f:
        puzzle.append(line.strip().split())
    f.close()
    return puzzle

def search(puzzle, words_to_search):
    result = {}
    for i in range(len(puzzle)):
        sublst = puzzle[i]
        tempstr = ''
        for char in sublst:
            tempstr += char.lower()
        for word in words_to_search:
            if word in tempstr:
                result[word] = [i, tempstr.find(word)]
                
    return result

