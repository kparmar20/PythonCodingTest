#Write a function to search for a character within a string. Given a character and string
# as inputs, your function should return the index of the first occurrence of the character
# within the string. If the string does not contain the character, your function should return -1.

#Do not use any built-in library functions to answer this question (e.g. if you’re using
# Python, do not use the find() or index() functions).

#You should also write some test code to show that your function works as expected.


def char_search(input_character, input_string):
    found=False
    for x in range(len(input_string)):
        if found==False:
            if input_character==input_string[x]:
                found=True
                print("Index value",x)
    if found==False:
        print("-1")
char_search('x','xiuytfddrt')