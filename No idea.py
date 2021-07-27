# https://www.hackerrank.com/challenges/no-idea/problem?h_r=next-challenge&h_v=zen

# There is an array of n integers.
# There are also  disjoint sets, A and B, each containing m integers.
# You like all the integers in set A and dislike all the integers in set B.
# Your initial happiness is 0.
# For each  integer in the array, if i in A, you add 1 to your happiness.
# If i in B, you add -1 to your happiness.
# Otherwise, your happiness does not change. Output your final happiness at the end.

# Constraints
# 1 <= n <= 10^5
# 1 <= m <= 10^5
# 1<= Any integer in the input <= 10^9

if __name__ == '__main__':
    happiness = 0
    n, m = map(int, input("Please give the values for n and m: ").split())
    users_array = list(input("Please give {} elements of the array: ".format(n)).split())
    a_set = set(input("Please give {} elements for A set: ".format(m)).split())
    b_set = set(input("Please give {} elements for b set: ".format(m)).split())

    for i in range(len(users_array)):
        if users_array[i] in a_set:
            happiness += 1
        if users_array[i] in b_set:
            happiness -= 1
    print("Your happiness is: {}".format(happiness))
