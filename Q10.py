#Write a function that sorts a list/array of numbers. Your function should take a list/array
# of numbers as input and return the list/array in ascending order.

#Do not use any built-in library functions to answer this question (e.g. if you’re using
# Python, do not use the sort() function).

#You should also write some test code to show that your function works as expected.


def smallest_number(list_in):
    #find largest number, list_in

    smallest = list_in[0]
    for x in list_in:
        if x < smallest:
            smallest=x
    return smallest


def sort_list(list_in):

    list_out=[]
    while len(list_in)>1:
        y=smallest_number(list_in)
        list_out.append(y)
        list_in.remove(y)

    print(list_out)




sort_list([23,19,123,-1,-5])
sort_list([1345533,23,199989000,123,-1,-5])
sort_list([-1345533,-23,-199989000,-123,-1,-5])
