'''Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".'''

def solution(inputString):
    res =""
    for ele in inputString:
        if ele.isdigit():
            res += ele
        else:
            break
    return res

