#Write a function that prints the numbers from 1 to 100. However, for multiples of 3 it
# should print “Fizz” instead of the number; for multiples of 5 it should print “Buzz”.
# For multiples of 3 and 5, print “FizzBuzz”.

def FizzBuzz():
    for i in range(1,101):
        if i%3==0 | i%5==0:
            print(i, "FizzBuzz")
        elif i%3==0:
            print(i, "Fizz")
        elif i%5==0:
            print(i, "Buzz")
        else:
            print(i)

FizzBuzz()