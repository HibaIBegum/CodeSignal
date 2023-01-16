'''Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

'''


def solution(a):
    hold = sorted([x for x in a if x != -1])
    print(hold)
    j = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = hold[j]
            j += 1
    return a


