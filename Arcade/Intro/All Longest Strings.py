'''Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].'''

def solution(inputArray):
    ml = max(len(s) for s in inputArray)
    result = list(s for s in inputArray if len(s) == ml)
    return result
