'''Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.'''

def solution(n):
    while n:
        if (n%10)%2!=0:
            return False
        print('before ',n)
        n = n//10
        print('after ',n)
    return True

