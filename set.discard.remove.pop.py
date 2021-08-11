# Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

# The first line contains integer n, the number of elements in the set s.
n = int(input())

# The second line contains n space separated elements of set s.
# All of the elements are non-negative integers, less than or equal to 9.
s = set(map(int, input().split()))

# The third line contains integer N, the number of commands.
number_of_commands = int(input())

for i in range(number_of_commands):
    user_command = str(input())

    if user_command == "pop":
        s.pop()
    elif "remove" in user_command:
        item_to_be_removed = user_command.split()
        try:
            s.remove(int(item_to_be_removed[-1]))
        except:
            continue
    elif "discard" in user_command:
        item_to_be_discarded = user_command.split()
        s.discard(int(item_to_be_discarded[-1]))

print(sum(s))

