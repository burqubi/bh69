a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input())
for i in range(n):
    a.insert(0, a.pop())
print(a)