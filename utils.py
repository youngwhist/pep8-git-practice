import os,sys
def average(numbers):
    if len(numbers)==0: return 0
    return sum(numbers)/len(numbers)
def max_value(numbers) :
    result=numbers[0]
    for n in numbers:
        if n>result:result=n
    return result
