while True:
    try:
        A, B = map(int, input().split())
        if A == B == 0:
            break
        else:
            print(A+B)
    except:
        break