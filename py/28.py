'''
Problem: #28- Body Mass Index
Link: https://www.codeabbey.com/index/task_view/body-mass-index
Tags: practical, arithmetic, if-else, c-1, c-0, simple
'''

print("input data:")
n = int(input())
ans = []

def bmi(w : int, h : float) -> float:
    bmi = w / pow(h, 2)

    if bmi < 18.5:
        return 'under'
    elif 18.5 <= bmi <= 25.0:
        return 'normal'
    elif 25.0 <= bmi <= 30.0:
        return 'over'
    else:
        return 'obese'
    

for i in range(0, n):
    w, h = input().split()
    w = int(w)
    h = float(h)

    bmi_eval = bmi(w, h)
    ans.append(bmi_eval)

print("answer:")
for a in ans:
    print(a, end = ' ')

