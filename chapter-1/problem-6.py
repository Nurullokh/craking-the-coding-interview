"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

def string_compression(s):
    if not s:
        return ""
    char = s[0]
    count = 0
    out = ""
    for i in range(len(s)):
        if s[i] == char:
            count += 1
        elif s[i] != char:
            out += char + str(count)
            char = s[i]
            count = 1
    out += s[-1] + str(count)
    if len(out) > len(s):
        return s
    return out

# Time complexity is O(n)

print(string_compression("aabcccccaaa"))
print(string_compression("abcde"))
print(string_compression("a"))
print(string_compression(""))
