N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())

shirts = 0
pen_set = N // P
pen_sep = N % P

for i in [S, M, L, XL, XXL, XXXL]:
    shirts += i // T
    if i % T != 0:
        shirts += 1

print(shirts)
print(pen_set, pen_sep)