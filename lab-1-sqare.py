a = int(input())
b = int(input())
c = int(input())
d = b*b-4*a*c
if d >0:
    x1 = (b-d**(1/2))/(2*a)
    x2 = (b+d**(1/2))/(2*a)
    print(x1, x2)
elif d==0:
    x1 = (b - d ** (1 / 2)) / (2 * a)
    print(x1)
else:
    print("Корней нет")






