'''Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
solution(n) = 99.

'''

def solution(n):
    lar=1
    for a in range(n):
        lar*=10
    return lar-1
