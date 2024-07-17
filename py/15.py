'''
Problem: #15 - Maximum of Array
Link: https://www.codeabbey.com/index/task_view/maximum-of-array
Tags: loops, if-else, c-0, simple
'''

print("input data:")
n = [int(x) for x in input().split(' ')]

min_n = min(n)
max_n = max(n)

print("answer:")
print(f"{max_n} {min_n}")