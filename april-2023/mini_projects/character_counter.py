# def count(s):
#     count = {}

#     for char in s:
#         if char in count:
#             count[char] += 1
#         else: count[char] = 1
#     return(count)
        
# count("aabb")

from collections import Counter

def count(string):
    print(Counter(string))

count("this is a test")