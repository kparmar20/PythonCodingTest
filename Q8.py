#Write a function that finds the largest prime factor of any number greater than 1.
# Your function should take a single number as input and return its largest prime factor.
# For example, the prime factors of 78 are 2, 3 and 13, so its largest prime factor is 13.

#You should also write some test code to show that your function works as expected.


def largest_prime_factor(int):

    largest_prime=[]
    #do a %x=0 check, start with int/2 (largest poss) and then
    if int<=2:
        print(int)
        return
    for x in range(2,int+1):
        if int%x==0:
            largest_prime.append(x)
    print(largest_prime)

    for y in largest_prime:
        print(y)



def findLargestPrimeFactor(input_int):
    primeFactor = 1
    x = 2

    while x <= input_int / x:
        if input_int % x == 0:
            primeFactor = x
            #input_int /= x
            input_int=input_int/x
        else:
            #x += 1
            x=x+1

    if primeFactor < input_int:
        primeFactor = input_int

    print(primeFactor)


#largest_prime_factor(4)
findLargestPrimeFactor(37)