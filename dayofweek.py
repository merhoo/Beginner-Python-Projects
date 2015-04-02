'''
Created on Dec 2, 2011

@author: Meredith
'''
import sys
DAYS = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday")
MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def get_date():#tests input to see if date is he right format
    str_date = input('Enter date: ')
    parts = str_date.split('/')#separates input into a tuple
    length = len(parts)
    if length != 3:
        raise ValueError('Invalid format for date.')
    for i in range(length):#assigns i to each part of date
        parts[i] = parts[i].strip()
        if len(parts[i]) == 0 or not parts[i].isdigit():#strips away alpha
            raise ValueError('Invalid format for date.')
    return int(parts[0]), int(parts[1]), int(parts[2])#when run in main, it returns parts as integers and ends.. goes to next line of code

def is_date_valid(month, day, year):#checks to see if valid format is also logic
    if month < 1 or month > 12 or day <1 or year < 0:
        return False
    days_in_month = DAYS_IN_MONTH[month - 1]#starts with 0, so if user puts in 11, it refers to November not December
    if month != 2:
        return day <= days_in_month
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:# if it is a leap year
        days_in_month += 1#adds another day to February
    return day <= days_in_month

def date_as_string(month, day, year):#matches the integer month with the actual month
    months = ('January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    return (months[month-1]) + ' ' + str(day) + ', ' + str(year)

def day_of_week(month, day, year):# tells what day of the week is of the entered date
    DAYS = ('Saturday','Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    J = year // 100 # century
    K = J % 100# year of century
    m = month
    q = day
    if month == 1 or 2:# January and February have to be equal to 13 or 14 in order for equation to compute the right day
        m += 12
        J -= 1
    h = (q + 26 *(m + 1) // 10 + K + K // 4 + J // 4 - (2*J)) % 7
    return DAYS[h]

def main():# where a program starts
    print('This program calculates the day of the week for any date.')
    try:#observes an error
        (month, day, year) = get_date()
    except ValueError as error:# when date is an error in get_date it prints error
        print('ERROR: ', error)
        sys.exit(1)
    if not is_date_valid(month, day, year):# when date is invalid in is_date_valid
        print(str(month) + '/' + str(day) + '/' + str(year) + ' is an invalid date.')
    print(date_as_string(month, day, year) + ' is a ' + day_of_week(month, day, year))#when date is valid it prints the date and the day of the week

if __name__=='__main__':# prints main
    main()