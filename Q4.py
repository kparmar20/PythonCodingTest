#A palindrome is a string that reads the same way backwards as it does forwards, e.g.
# “radar” or “madam”. Write a function that takes a string as input and prints “Palindrome”
# if the input string is a palindrome but “Not palindrome” otherwise. For the empty string
# (i.e. “”), your function should print “Empty string”.

#Do not use any built-in library functions to answer this question (and if you’re using
# Python, do not use anything like my_string[::-1]).

#You should also write some test code to show that your function works as expected.


def palinedrome(input_string):

    #confirm string is >0 length
    while len(input_string)==0:
        print("Empty string")
        return

    #extract string and reverse string as two variables
    input_forward=input_string
    #print(input_forward)

    a=[]
    for x in range((len(input_string) - 1), -1, -1):
        a.append(input_string[x])
    input_reverse=''.join(a)
    #print(input_reverse)
#compare two variables and if same print "palinedrome"
    if input_forward==input_reverse:
        print("Palindrome")
    else:
        print("Not palindrome")

palinedrome('')