'''
Problem: #13 - Weighted Sum of Digits
Link: https://www.codeabbey.com/index/task_view/weighted-sum-of-digits
Tags: arithmetic, modulo, hash, c-1, c-0, simple
'''

print("input data:")
n = int(input())
ans = []

data = [int(x) for x in input().split()]

def wsd(num):
    a = 0
    res = list(map(int, str(num)))

    for i in range(0, len(res)):
        a += res[i] * (i + 1)

    return a

for d in data:
    ans.append(wsd(d))

print("answer:")
for a in ans:
    print(a, end = ' ')
