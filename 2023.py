import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
sys.setrecursionlimit(10**6)

def isPrime(n):
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True
        
def DFS(n):
    if len(str(n)) == N:
        print(f'{str(n)}\n')
        return
    else:
        for i in [1, 3, 5, 7, 9]:
            if isPrime(10 * n + i):
                DFS(10 * n + i)

for i in [2, 3, 5, 7]:
    DFS(i)