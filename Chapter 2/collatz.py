from sys import exit    # Only importing exit() to handle a keyboard interrupt during the program running

def collatz(number):    # Defining Collatz function
    originalNumber = number    # The originalNumber variable will be used in the final output
    steps = 0   # Setting steps taken to get to number 1 to 0 steps by default
    while number != 1:
        if number == 0:
            print('That\'s not how this works!')
            break
        elif number % 2 == 0:   # If even, perform even function
            print('Dividing ' + str(number) + ' by 2... ', end='')
            number = number // 2    # Dividing number by 2 and reassigning variable number to new value
            print(number)
            steps += 1      # Adding to step count
        elif number % 2 == 1:   # If odd, perform odd function
            print('Multiplying 3 times '+ str(number) + ' and adding 1... ', end='')
            number = 3 * number + 1     # Multiplying number by three and adding 1, reassigning variable number to new value
            print(number)
            steps += 1      # Adding to step count
    if number == 1:     # Checking if number has been reduced to 1 yet
        print('The number \"' + str(originalNumber) + '\" took ' + str(steps) + ' steps to get to 1')   # Printing how many steps the original number took to reduce to 1

print('Enter number to be Collatz\'d :')
try:
    collatz(int(input()))
except ValueError:      # Handles non-integer value in input field
    print('That\'s not an integer!')
except KeyboardInterrupt:   # Handles CTRL-C (not really necessary but cleans up the error output)
    exit()
