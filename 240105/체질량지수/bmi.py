a = input().split()

height = int(a[0]) * 0.01
weight = int(a[1])

bmi = int(weight / (height * height))

print(bmi)
if bmi >= 25:
    print("Obesity")