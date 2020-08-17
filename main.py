# num = int(input('Enter an integer: '))

# if num % 2 == 0 and num % 3 == 0:
#     print('{} is divisible by both 2 and 3'.format(num))
# elif num % 3 == 0:
#     print('{} is divisible by 3'.format(num))
# elif num % 2 == 0:
#     print('{} is divisible by 2'.format(num))
# else:
#     print('{} is divisible by neither 2 or 3'.format(num))


some_string = input('Enter a string of length between 3 and 10 characters: ')

if not (len(some_string) < 3 or len(some_string) > 10):
    print('{} is a good string length'.format(some_string))
else:
    print('{} is not between the appropriate bounds'.format(some_string))