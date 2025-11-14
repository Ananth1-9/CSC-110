'''
Ananth Mugundhan
CSC 110
Project -3
A program that calculates letter grades and 
pass/fail status based on numerical scores.
'''
def letter_grade(score):
    '''
    Tells what letter grade a score corresponds to.
    Args:
        takes a number between 0 and 100
    Returns:
        a string representing the letter grade
    '''
    # Determine letter grade based on score 
    if 100 >= score >= 90:
        return 'A'
    elif 90 > score >= 80:
        return 'B'
    elif 80 > score >= 70:
        return 'C'
    elif 70 > score >= 60:
        return 'D'
    elif 0 <= score < 60:
        return 'E'
    else:
        return 'X'  # Invalid score indicator
    
def pass_or_fail(grade):
    '''
    Tells whether a letter grade is passing 
    or failing.
    Args:
        takes a letter grade 
    Returns:
        a string which mentions if the grade is
        passing or failing
    '''
    # Determine pass/fail status based on letter grade 
    if grade in ['A', 'B', 'C', 'D']:
        return 'Pass'
    elif grade == 'E':
        return 'Fail'
    else:
        return 'Error: Invalid grade'
    
def point_grade(score, total_points):
    '''
    calculates the percentage score based on
    points earned and total points possible.
    Args:
        2 nubers, score and total_points
    Returns:
        a number representing the percentage score
    '''
    #calculates percentage score and rounds to 2 decimal places

    percent_grade = (score / total_points) * 100
    percent_grade = round(percent_grade, 2)
    return percent_grade

def get_grade_results(score, total_points):
    '''
    combines the results of the other functions 
    to give a full grade report.
    Args:
        2 numbers, score and total_points
    Returns:
        a string summarizing the percentage score, letter grade
        , and pass/fail status
    '''
    percent = point_grade(score, total_points)
    grade = letter_grade(percent)
    pass_fail = pass_or_fail(grade)
    return 'Your grade is {} ({} - {})'.format(percent, grade, pass_fail)

print(get_grade_results(37, 40))