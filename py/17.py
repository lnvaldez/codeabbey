'''
Problem: #17 - Array Checksum
Link: https://www.codeabbey.com/index/task_view/array-checksum
Tags: arithmetic, modulo, hash, loops, c-1, c-0, implementation
'''

n = int(input())

data = [int(x) for x in input().split()]

result = 0 

for d in data:
    result = (result + d) * 113 

print(result % 10000007)