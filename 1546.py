n = int(input())
score = list(map(int, input().split()))
hap = sum(score)
hap = hap / max(score) * 100
print(hap / len(score))