# Link: https://www.hackerrank.com/challenges/itertools-product/problem

import itertools

if __name__ == "__main__":
    a, b = input().split(), input().split()
    print(" ".join("({}, {})".format(*element) for element in tuple(itertools.product(a, b))))
