#A function written as concisely as possible which takes a range of values, a, and
#returns the maximum value when given an index of a from ranges.

def max_sum(a, ranges): 
    total = [sum(a[x:y]) for x, y in ranges]
    print(total)
  

max_sum([1,-2,3,4,-5,-4,3,2,1], [(1,3), (2,5), (4,7)])