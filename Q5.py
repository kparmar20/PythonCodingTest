#Write a function that takes a list/array of strings as input and determines whether it
# contains duplicate strings. Your function should print “Contains duplicates” if the
# list does contain duplicates; otherwise, it should print “Does not contain duplicates”.

#You should write some test code to show that your function works as expected.



def duplicate_list(list_in):
    list_length=len(list_in)
    #print(list_length)
    set_list_in=set(list_in)
    set_length=len(set_list_in)
    #print(set_length)

    if set_length==list_length:
        print("Does not contain duplicates")
    else:
        print ("Contains duplicates")


duplicate_list(['xxx','xyz','xxx','abc'])
duplicate_list(['xxx','xyz','abc','def','a'])