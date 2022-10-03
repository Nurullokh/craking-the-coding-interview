# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# We will assume that string is ASCII (128 characters)

def is_unique(input_str: str) -> bool:
    if len(input_str) > 128:
        return False
    
    bool_char_set = [False] * 128
    for char in input_str:
        char_code_in_ascci = ord(char)

        # return False if char was found already
        if bool_char_set[char_code_in_ascci]:
            return False
        
        # if not found, change the element in that index to True
        bool_char_set[char_code_in_ascci] = True

    # if there is no duplicate, return True
    return True

# Time complexity is O(n)

# True
print(is_unique("abc"))

# False
print(is_unique("bba"))

