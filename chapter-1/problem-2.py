# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

def check_permutation(s1, s2):
    # the lengths of strings have to be equal to each other.
    if len(s1) != len(s2):
        return False
    
    # then we should sort the strings and check whether they are equal or not
    # coz' when 2 words should be permutation of each other, they
    # need to have exactly the same characters and their frequencies.

    return sorted(s1) == sorted(s2)

# Time complexity is O(n logn)

# True
print(check_permutation("word", "dwor"))

# False
print(check_permutation("abab", "bada"))