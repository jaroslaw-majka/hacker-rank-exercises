# Link to the quiz: https://www.hackerrank.com/challenges/list-comprehensions/problem

# Using list comprehensions You are given three integers and representing the dimensions of a cuboid
# along with an integer . Print a list of all possible coordinates given by on a 3D grid where the sum of
# is not equal to n Here, 0 <= i <= x; 0 <= j <= y, 0 <= k <= z


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print([[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if sum([i, j, k]) != n])
