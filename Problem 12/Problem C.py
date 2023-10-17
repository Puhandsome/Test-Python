try:
    x = float(input('Enter a number:'))
    try:
        y = float(input('Enter another number:'))
    except:
        print('ERROR: Invalid input')
    finally:
        print('The sum is',(x+y))
except:
    print('ERROR: Invalid input')