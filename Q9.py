#An n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, the 5-digit number 15234 is pandigital, as is the 6-digit number 463215.

#Write a function that takes a number as input and prints “Pandigital” if the input
# number is pandigital but “Not pandigital” otherwise.

#You should also write some test code to show that your function works as expected.



def pandigital(input_int):

    input_int_len= len(str(input_int))
    #print("input_int_len",input_int_len)
    input2=map(str,list(range(1,input_int_len+1)))
    input2=''.join(input2)
    #print("input2",input2)

    #take input and order
    input1=''.join(sorted(str(input_int)))
    #print("input1",input1)

    #compare two strings
    if input1==input2:
        print("Pandigital")
    else:
        print("Not Pandigital")

pandigital(46312)