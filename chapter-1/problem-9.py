"""String Rotation: Assume you have a method i5Su b5tring which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to i5Sub5tring (e.g., "waterbottle" is a rotation of" erbottlewat")"""

def string_rotation(s1, s2):
    l = len(s1)
    if l == len(s2) and l > 0:
        s1 = 2 * s1
        return s2 in s1
    return False

# Time complexity - O(1)
# True
print(string_rotation("good", "dgoo"))
