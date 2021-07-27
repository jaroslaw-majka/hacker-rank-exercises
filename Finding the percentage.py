# Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Constraints
# 2 <= n <= 10
# 0 <= marks[i] <= 100
# length of marks arrays = 3

if __name__ == '__main__':
    n = int(input("How many students would you like to add? "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Please give me their name and score in one line: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Which student's average would you like to see? ")

    score_sum = 0.0
    for i in range(len(student_marks[query_name])):
        score_sum += student_marks[query_name][i]
    average = score_sum / len(student_marks[query_name])
    print("%.2f" % average)
