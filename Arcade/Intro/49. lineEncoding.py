'''Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
solution(s) = "2a3bc".

'''

from collections import Counter
def solution(s):
    start = s[0]
    cnt =1
    temp =""
    for i in range(1,len(s)):
        if start == s[i]:
            cnt +=1
        else:
            if cnt==1:
                temp += start
            else:
                temp += str(cnt)+start
            start = s[i]
            cnt =1
    if cnt ==1:
        temp+= start
    else:
        temp += str(cnt)+start
    return temp

