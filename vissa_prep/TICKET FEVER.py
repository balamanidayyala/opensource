T=int(input())
for _ in range(T):
    N,M=map(int, input().split())
    if M>=N:
        print("0")
    else:
        print(N-M)
        
