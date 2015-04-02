'''
Created on Oct 24, 2011

@author: Meredith, Kai, David
'''
print('--- Palindrome Tester ---')
phrase = input('Enter a word or phrase (blank line to quit): ')
while phrase != '':
    phrase_alnum = ''#idea of a palindrome
    phrase_backwards = ''#idea of a palindrome backwards
    for c in phrase:# c is all the letter in phrase
        if str.isalnum(c):# if c is alphanumeric, phrase_alnum will concatenate
            phrase_alnum = phrase_alnum + c
    phrase_alnum = phrase_alnum.lower()  # makes phrase_alnum lowercase
    for b in phrase_alnum:#b is all the letters in phrase_alnum
        phrase_backwards = b + phrase_backwards#
    if phrase_alnum == phrase_backwards:
        print("Your input is '" + phrase + "' is a palindrome.")
    else:
        print("Your input is '" + phrase + "' is NOT a palindrome.")
    phrase = input('Enter a word or phrase (blank line to quit): ')
print('Bye.')