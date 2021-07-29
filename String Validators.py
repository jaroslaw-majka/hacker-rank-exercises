# https://www.hackerrank.com/challenges/string-validators/problem

# Your task is to find out if the string  contains:
# alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    s = input()
    i = 0

    # In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
    while i < len(s):
        if s[i].isalnum():
            print(True)
            i = 0
            break
        elif i == len(s) - 1 and s[i].isalnum() is False:
            print(False)
            i = 0
            break
        i += 1

    # In the second line, print True if s has any alphabetical characters. Otherwise, print False.
    while i < len(s):
        if s[i].isalpha():
            print(True)
            i = 0
            break
        elif i == len(s)-1 and s[i].isalpha() is False:
            print(False)
            i = 0
            break
        i += 1

    # In the third line, print True if s has any digits. Otherwise, print False.
    while i < len(s):
        if s[i].isdigit():
            print(True)
            i = 0
            break
        elif i == len(s)-1 and s[i].isdigit() is False:
            print(False)
            i = 0
            break
        i += 1

    # In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
    while i < len(s):
        if s[i].islower():
            print(True)
            i = 0
            break
        elif i == len(s)-1 and s[i].islower() is False:
            print(False)
            i = 0
            break
        i += 1

    # In the fifth line, print True if s has any uppercase characters. Otherwise, print False.
    while i < len(s):
        if s[i].isupper():
            print(True)
            i = 0
            break
        elif i == len(s)-1 and s[i].isupper() is False:
            print(False)
            i = 0
            break
        i += 1
