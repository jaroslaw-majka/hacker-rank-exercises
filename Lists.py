# link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    working_list = []
    for _ in range(N):
        user_input = input().split()
        if "insert" in user_input:
            working_list.insert(int(user_input[1]), int(user_input[2]))
            user_input = []
        elif "print" in user_input:
            print(working_list)
            user_input = []
        elif "remove" in user_input:
            working_list.remove(int(user_input[1]))
            user_input = []
        elif "append" in user_input:
            working_list.append(int(user_input[1]))
            user_input = []
        elif "sort" in user_input:
            working_list.sort()
            user_input = []
        elif "pop" in user_input:
            working_list.pop()
            user_input = []
        elif "reverse" in user_input:
            working_list.reverse()
            user_input = []