'''
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
solution(text) = "steady".
'''
import re


def solution(text):
    longest = []
    word = []
    for char in text:
        if ord("A") <= ord(char) <= ord("Z") or ord("a") <= ord(char) <= ord("z"):
            word.append(char)
        else:
            if len(word) > len(longest):
                longest = word
            word = []
    if len(word) > len(longest):
        longest = word
    return "".join(longest)


