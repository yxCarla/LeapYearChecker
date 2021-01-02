print('Welcome to the Leap Year Checker!')


def check_year():
    try:
        year = int(input('Please enter a year.\n'))
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    if year < 2021:
                        print('The year 'f'{year} was a leap year.')
                    else:
                        print('The year 'f'{year} is a leap year.')
                elif year < 2021:
                    print('The year 'f'{year} was not a leap year.')
                else:
                    print('The year 'f'{year} is not a leap year.')
            elif year < 2021:
                print('The year 'f'{year} was a leap year.')
            else:
                print('The year 'f'{year} is a leap year.')
        elif year < 2021:
            print('The year 'f'{year} was not a leap year.')
        else:
            print('The year 'f'{year} is not a leap year.')
    except ValueError:
        print('Oops! Invalid year entered! Try again.')
        check_year()

    check = input('Would you like to check another year? Please enter either yes or no.\n')
    if check.lower() in ('yes', 'y'):
        check_year()
    if check.lower() in ('no', 'n'):
        print('Thank you for using the Leap Year Checker!')
    if check.lower() not in ('yes', 'no', 'n', 'y'):
        print('Invalid response received, exited.')


check_year()
