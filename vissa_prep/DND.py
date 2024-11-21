N,m=map(int, input().split())
n=list(map(int, input().split()))
num1=0
num2=0
for i in range(N):
    if n[i]%m==0:
        num1+=n[i]
    else:
        num2+=n[i]
print(num1-num2)
