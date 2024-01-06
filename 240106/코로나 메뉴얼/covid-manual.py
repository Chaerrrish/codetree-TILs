x = input().split()
y = input().split()
z = input().split()

a = 0

if x[0] == "Y" and int(x[1]) >= 37 :
    a += 1

if y[0] == "Y" and int(y[1]) >= 37 :
    a += 1
if z[0] == "Y" and int(z[1]) >= 37 :
    a += 1

if a >= 2 :
    print("E")
else :
    print("N")