N = int(input())

count = 0
num = list(map(int, input().split()))

for i in num:
    result = True
    for j in range(2, int(i**0.5 + 1)):
        if i % j == 0:
            result = False

    if i == 1:
        result = False

    if result == True:
        count += 1

print(count)