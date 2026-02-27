import copy

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = 0
maxres = 0

for i in num:
    for j in num:
        for k in num:
            if i != j and j != k and i != k:
                result = i + j + k
                if maxres <= result <= M:
                    maxres = copy.deepcopy(result)

print(maxres)