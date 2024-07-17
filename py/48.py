'''
Problem: #48 - Collatz Sequence
Link: https://www.codeabbey.com/index/task_view/collatz-sequence
Tags: arithmetic, classical, c-1, c-0, simple
'''

def collatz(n, count):
    if n == 1:
        answers.append(count)
    else:
        if n % 2 == 0:
            n = n / 2
            collatz(n, count + 1)
        else: 
            n = 3 * n + 1
            collatz(n, count + 1)

print("input data:")
t = int(input())
n = [int(x) for x in input().split()]

answers = []

for i in n:
    collatz(n = i, count = 0)

print("answer:")
for a in answers:
    print(a, end = ' ')



