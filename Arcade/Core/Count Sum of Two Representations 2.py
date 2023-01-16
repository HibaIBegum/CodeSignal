'''Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2, and r = 4, the output should be
solution(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.'''

import math
def solution(n, l, r):
    if n%2==0:
        return math.floor(max(0,min(n/2-l,r-n/2)+(n+1)%2))
    else:
        return math.floor(max(0,min(n/2-l,r-n/2)+(n)%2))

