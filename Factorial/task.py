num = int(input())
fact = 1
i = 1
if 1 <= num <= 100:
    while i <= num:
        fact *= i
        i += 1
print(fact)