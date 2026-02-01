N = int(input())
A = [0]
result = []
B = [int(input()) for _ in range(N)]
index = 0
i = 1

while i <= N or len(A) > 1:
    if A[-1] < B[index]:
        A.append(i)
        result.append("+")
        i += 1
    elif A[-1] == B[index]:
        A.pop()
        result.append("-")
        index += 1
    else:
        print("NO")
        quit()

for i in range(len(result)):
    print(result[i])