a, b, c = map(int, input().split())

if (a > b and b > c) or (a < b and b < c) :
    print(b)
elif (b > c and c > a) or (b < c and c < a) :
    print(c)
elif (c > a and a > b) or (c < a and a < b) :
    print(a)