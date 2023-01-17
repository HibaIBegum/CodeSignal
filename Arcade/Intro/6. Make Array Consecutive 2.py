'''Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.'''


def solution(statues):
    sol = 0
    statues.sort()
    Min = statues.pop(0)
    for i in statues:
        print('value missing is ', i - Min, 'i is ', i)
        if i - Min > 1:
            sol += i - Min - 1
            Min = i
        else:
            Min = i
        print('Min here is ', Min, 'Sol is ', sol)
    return sol
