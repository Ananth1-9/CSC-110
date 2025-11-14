def verse(a):
    '''
    This is a function that takes a string and inputs it into a verse and returns the verse
    '''
    verse = 'The {} spider climbed up the waterspout.\nDown came the rain and washed the spider out.\nOut came the sun and dried up all the rain.\nThe {} spider climbed up the waterspout.\n'.format(a, a)
    print(verse)

def main():
    '''
    calls the main_verse function three times with different strings
    '''
    verse('itsy bitsy')
    verse('big hairy')
    verse('teeny tiny')

main()