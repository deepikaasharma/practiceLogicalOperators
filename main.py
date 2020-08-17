num = int(input('Enter an integer: '))

if num % 2 == 0 and num % 3 == 0:
    print('{} is divisible by both 2 and 3'.format(num))
elif num % 3 == 0:
    print('{} is divisible by 3'.format(num))
elif num % 2 == 0:
    print('{} is divisible by 2'.format(num))
else:
    print('{} is divisible by neither 2 or 3'.format(num))