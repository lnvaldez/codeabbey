'''
Problem: #14 - Modular Calculator
Link: https://www.codeabbey.com/index/task_view/modular-calculator
Tags: arithmetic, modulo, loops, c-0, implementation
'''

print("input data:")
n = int(input())
loop = True
op = None

while loop:
    op, m = input().split(' ')
    m = int(m)
    
    if op == '+':
        n = n + m 
    elif op == '*':
        n = n * m 
    else:
        n = n % m 
        answer = n
        loop = False

print("answer:")
print(answer)