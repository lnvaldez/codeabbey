'''
Problem: #23- Bubble in Array
Link: https://www.codeabbey.com/index/task_view/bubble-in-array
Tags: arrays, loops, if-else, sorting, c-0, implementation
'''

def swap(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

def checksum(lst):
    r = 0
    for i in lst:
        r = (r + i) * 113
        r = r % 10000007
    return r

data = [int(x) for x in input().split() if x != '-1']
count = 0

for i in range(len(data) - 1): 
    if data[i] > data[i + 1]:
        swap(data, i, i + 1)
        count += 1

print(count, checksum(data))
