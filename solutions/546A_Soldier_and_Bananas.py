"""
Problem: Soldier and Bananas (546A)
Codeforces Submission ID: 388417140
Author: habebaabdelrahem4
"""

k, n, w = map(int, input().split())

# 1. نحسب التكلفة خطوة بخطوة بالـ Loop
total_cost = 0
for i in range(1, w + 1):
    total_cost += i * k  # الموزة الأولى 1*k، التانية 2*k، وهكذا

# 2. نشوف محتاج يستلف ولا لأ بـ if العادية
if total_cost > n:
    print(total_cost - n)
else:
    print(0)