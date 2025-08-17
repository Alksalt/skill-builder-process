from collections import Counter

def count_let(s):
    return Counter(s)
def factorial(num):
    if num in (0, 1):
        return 1
    return num * factorial(num - 1)
def calculation(s):
    n = len(s)
    denominator = 1
    for let in count_let(s).values():
        denominator *= factorial(let)
    return factorial(n) / denominator

s = 'statistics'
print(calculation(s))