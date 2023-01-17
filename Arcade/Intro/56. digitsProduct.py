'''

Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
solution(product) = 26;
For product = 19, the output should be
solution(product) = -1.
'''


def solution(product):
    res = ""
    i = 9
    if product == 0: return 10
    if 1 <= product <= 9: return product
    while (product != 0):
        if product % i == 0:
            product //= i
            res = str(i) + res
            continue
        i -= 1
        if i == 1:
            if product > 10: return -1
            break
    return int(res)


