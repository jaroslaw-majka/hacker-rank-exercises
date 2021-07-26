# Link to the quiz: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a_list = list(arr)[:n]
    a_list.sort(reverse=True)
    for i in range(n):
        if a_list[i] < max(a_list):
            print(a_list[i])
            break
