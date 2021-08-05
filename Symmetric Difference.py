# Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

def set_diff_printer(n: set, m: set):
    # The functions accepts 2 sets of which creates a new set, which contains only differences between the two.
    final_set = m.difference(n)
    final_set.update(n.difference(m))
    # Then converts new set into a list. converts data into int and sorts
    my_list = list(final_set)
    my_list = list(map(int, my_list))
    my_list.sort()
    # As the requirement was to print each iteration one below another function below does just that.
    for i in range(len(my_list)):
        print(my_list[i])


if __name__ == "__main__":
    m_set_lenght = int(input())
    m_elements_set = set(input().split())
    n_set_lenght = int(input())
    n_elements_set = set(input().split())

    set_diff_printer(n_elements_set, m_elements_set)
