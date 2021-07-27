# Link: https://www.hackerrank.com/challenges/nested-list/problem

# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    students_list = []
    for _ in range(int(input("How many students would you like to add: "))):
        name = input("Students name: ")
        score = float(input("Students score: "))
        students_list.append([name, score])

    students_list.sort(key=lambda student: student[1], reverse=True)
    for students_name in range(len(students_list)):
        if students_list[students_name] < max(students_list):
            print(students_list[students_name])

    print(students_list)
