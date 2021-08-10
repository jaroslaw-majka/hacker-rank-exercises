# Link: https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == "__main__":
    number_of_entries = int(input())
    entries_set = set()
    for i in range(number_of_entries):
        entries_set.add(input())
    print(len(entries_set))