# Link:https://www.hackerrank.com/challenges/swap-case/problem

# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    user_input = str(input("Please give me your input: "))
    print(swap_case(user_input))
