"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""


def is_one_edit_away(s1, s2):
    # if they are equal to each other then
    # the case is True.
    if s1 == s2:
        return True
    
    # finding a shorter one
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    # counting frequencies
    dc_s1 = {}
    dc_s2 = {}
    for c in s1:
        if c in dc_s1:
            dc_s1[c] += 1
        else:
            dc_s1[c] = 1

    for c in s2:
        if c in dc_s2:
            dc_s2[c] += 1
        else:
            dc_s2[c] = 1

    # checking through the shorter one's dictionary
    # whether the character is in the bigger one's dictionary
    # and if there are 2 or more character which are not in the first dictionary
    # then we have to return False, because it is not 1 edit away.
    # Also, if a character is found on the bigger dictionary, 
    # we decrement its frequency.
    diff = 0
    for c in dc_s2:
        if diff == 0 and c not in dc_s1:
            diff += 1
        elif diff >= 1 and c not in dc_s1:
            return False
        elif c in dc_s1:
            dc_s1[c] -= 1
    
    # then we run through the bigger dictionary and check whether a character
    # has more than 1 frequency. If there is one, return False, coz it is not
    # 1 edit away. If everything is find then return True.
    for c in dc_s1:
        if c not in dc_s2:
            if dc_s1[c] >= 2:
                return False
        elif dc_s2[c] > 1:
            return False
    return True

# Time complexity is O(n)

print(is_one_edit_away("kamd", "hamp"))

# True
print(is_one_edit_away("pale", "ple"))

# False
print(is_one_edit_away("kale", "kadm"))

# True
print(is_one_edit_away("pales", "pale"))

# False
print(is_one_edit_away("bale", "pake"))


    