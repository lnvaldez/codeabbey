'''
Problem: #43- Dice Rolling
Link: https://www.codeabbey.com/index/task_view/dice-rolling
Tags: games, floating-point, random, arithmetic, c-0, simple
'''

n = int(input())
ans = []

for i in range(0, n):
    d = float(input())
    ans.append(int(d * 6) + 1)

print("answer:")
for a in ans:
    print(a, end = ' ')

