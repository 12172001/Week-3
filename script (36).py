a = int(input())
b = int(input())
c = int(input())
d = int(input())
i = 1
sum = b * 100 + c
p1 = 100 + a
while i <= d:
    n = sum * p1 / 100
    sum = n
    i += 1
print(int(sum / 100), int(sum % 100))