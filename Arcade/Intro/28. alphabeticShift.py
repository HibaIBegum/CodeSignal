'''Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".'''

def solution(inputString):
    map=[0]*256
    new =""
    for i in inputString:
        if i =='z':
            new += chr(ord(i)-25)
        else:
            new += chr(ord(i)+1)
    return new

