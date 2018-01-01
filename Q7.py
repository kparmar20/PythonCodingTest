#A word is an anagram of another word if the first word’s letters can be rearranged to
# form the second word. For example, “ward” and “draw” are anagrams of one another, as
# are “silent” and “listen”.

#Write a function that determines whether two strings are anagrams of another. Your
# function should take two strings as input and print “Anagram” if they are anagrams;
# otherwise, it should print “Not anagram”. For simplicity, treat blank spaces as if they
# are any other character.

#You should write some test code to show that your function works as expected.

def anagram(input_string1, input_string2):

    #take two strings and order characters
    input1=''.join(sorted(input_string1))
    input2=''.join(sorted(input_string2))

    #compare two strings
    if input1==input2:
        print("Anagram")
    else:
        print("Not Anagram")

anagram('ward','draw')
anagram('python','typhon')