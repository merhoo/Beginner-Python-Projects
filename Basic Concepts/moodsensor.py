'''
Created on Oct 4, 2011

@author: Meredith
'''
import random
print('--- Mood Sensor v1.0 ---')
print('Your ttrue emotions are coming across my screen.')
print('At this moment, you are...')
mood = random.randint(1, 4)

if mood <= 1:
    print('''
    HAPPY!
     -------
    |       |
    | O   O |
    |   <   |
    | .   . |
    |  ...  |
     -------''')
elif mood <= 2:
    print('''
    Neutral
     -------
    |       |
    | o   o |
    |   <   |
    |  ___  |
    |       |
     -------''')
elif mood <= 3:
    print('''
    Sad
     -------
    |       |
    | o   o |
    |   <   |
    |  ...  |
    |'     '|
     -------''')
else:
    print('...yikes, in a really bad mood!!! Cheer up!')