#Write a function that takes a list/array of strings as input and “deduplicates” it. Your
# function should return a new list/array of strings with all duplicates removed. It’s fine
# if your new list/array is not in the same order as the original list.

#You should write some test code to show that your function works as expected.


def deduplicate_list(list_in):
    set_list_in=set(list_in)

    print(set_list_in)


deduplicate_list(['xxx','xyz','xxx','abc'])
deduplicate_list(['xxx','xyz','abc','def','a'])