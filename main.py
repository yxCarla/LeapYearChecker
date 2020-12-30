print('Welcome to the Leap Year Checker!')


def check_year():
    year = int(input('Please enter a year.\n'))
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                if year < 2020:
                    print('The year 'f'{year} was a leap year.')
                else:
                    print('The year 'f'{year} is a leap year.')
            elif year < 2020:
                print('The year 'f'{year} was not a leap year.')
            else:
                print('The year 'f'{year} is not a leap year.')
        elif year < 2020:
            print('The year 'f'{year} was a leap year.')
        else:
            print('The year 'f'{year} is a leap year.')
    elif year < 2020:
        print('The year 'f'{year} was not a leap year.')
    else:
        print('The year 'f'{year} is not a leap year.')

    check = input('Would you like to check another year? Please enter either yes or no.\n')
    if check.lower() in 'yes':
        check_year()
    if check.lower() in 'no':
        print('Thank you for using the Leap Year Checker!')


check_year()
