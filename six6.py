from __future__ import print_function # use Python 3.0 printing 

def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
    
def report_grade(percent): 
    '''Step 6b if-else'''
    MASTERY_LIMIT = 80          # convention: use CAPS for constants
    if percent < MASTERY_LIMIT:
        print('A grade of', percent, 'does not indicate mastery.')
        print('Seek extra practice or help.')
    else:
        print('A grade of', percent, 'indicates mastery.')
        print('Keep up the good work!')

def letter_in_word(letter,word):
    '''Step 8 - return True if letter is in word.'''
    return letter in word

	asdfasdf
	
	asdfasdf