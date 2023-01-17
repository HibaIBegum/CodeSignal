'''

Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
solution(matrix) = 6.
'''
def solution(matrix):
    sample = set()
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            sqaure =matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1]
            sample.add(sqaure)
    print(sample)
    return len(sample)

