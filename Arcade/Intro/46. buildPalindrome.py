'''Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".'''

def solution(st):
    if st == st[::-1]:  # Check for initial palindrome
        return st
    index = 0
    subStr = st[index:]
    while subStr != subStr[::-1]:  # while substring is not a palindrome
        index += 1
        subStr = st[index:]
    return st + st[index - 1::-1]

