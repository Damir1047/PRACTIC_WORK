A = int(input())
B = int(input())
C = int(input())

p = (A+B+C)/2
print(p)
S = (p*(p-A)*(p-B)*(p-C))**(1/2)

print(S)