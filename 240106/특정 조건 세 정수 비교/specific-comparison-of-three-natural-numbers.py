a, b, c = map(int, input().split())

if a <= b and a <= c :
    min = a
elif b < a and b < c :
    min = b
elif c < a and c < b :
    min = c

if a == min :
    print(1, end=" ")
else :
    print(0, end=" ")

if a == b == c :
    print(1)
else :
    print(0)