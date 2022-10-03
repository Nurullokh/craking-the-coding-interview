"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""

# So, a palindrome is a string that is the same forwards and backwards. 
# For a word being read forwards and backwards the same, it should have an
# even number of almost all character, so that half can be on one side and half can be on the other
# side. At most one character (the middle character) can have an odd count. 
# To be more precise, strings with even length (after removing all non-letter characters) must have
# all even counts of characters. Strings of an odd length must have exactly one character with
# an odd count. Of course, an "even" string can't have an odd number of exactly one character,
# otherwise it wouldn't be an even-length string (an odd number+ many even numbers= an odd
# number). Likewise, a string with odd length can't have all characters with even counts (sum of
# evens is even). It's therefore sufficient to say that, to be a permutation ot a palindrome, a string
# can have no more than one character that is odd. This will cover both the odd and the even cases.

def is_permutation_of_palindrome(s):
    # counting the frequencies
    dc = {}
    for c in s:
        if c in dc:
            dc[c] += 1
        else:
            dc[c] = 1
    
    # to check for no more than 1 character has odd number of frequencies
    found = False
    for v in dc.values():
        if v % 2 == 1:
            if found:
                return False
            found = True

    return True

# Time complexity is O(n)

# True 
print(is_permutation_of_palindrome("abba"))

# False
print(is_permutation_of_palindrome("goody"))

