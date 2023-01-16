'''Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]'''


def solution(picture):
    m = len(picture)  # rows
    n = len(picture[0])  # columns
    newpic = ['*' * (n + 2) for y in range(m + 2)]
    for ind, text in enumerate(picture):
        newpic[ind + 1] = '*' + text + '*'
    return newpic


