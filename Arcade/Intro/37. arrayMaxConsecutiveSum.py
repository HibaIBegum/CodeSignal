'''Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.'''


def solution(a, k):
    total = sum(a[:k])
    res = total

    for i in range(len(a) - k):
        total += a[i + k] - a[i]
        res = max(res, total)
    return res

