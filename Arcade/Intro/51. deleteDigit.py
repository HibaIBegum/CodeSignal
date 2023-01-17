'''Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.'''


def solution(n):
    s = str(n)
    for i in range(len(s)):
        print(int(s[:i] + s[i + 1:]))
    return max([int(s[:i] + s[i + 1:]) for i in range(len(s))])


