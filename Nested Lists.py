# Link: https://www.hackerrank.com/challenges/nested-list/problem

# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    students_list = []
    for _ in range(int(input("How many students would you like to add: "))):
        name = input("Students name: ")
        score = float(input("Students score: "))
        students_list.append([name, score])

    students_list.sort(key=lambda student: student[1])
    min_students_score = float(students_list[0][1])
    for i in range(len(students_list)):
        if students_list[i][1] > min_students_score:
            second_worst_score = students_list[i][1]
            break

    final_students_list = []
    for i in range(len(students_list)):
        if students_list[i][1] == second_worst_score:
            final_students_list.append(students_list[i][0])
            print(final_students_list)

    final_students_list.sort()
    for i in range(len(final_students_list)):
        print(final_students_list[i])

