a = int(input())
b = int(input())
c = int(input())
money_before = 100 * b + c
money_after = int(money_before * (100 + a ) / 100)
print(money_after // 100, money_after % 100)