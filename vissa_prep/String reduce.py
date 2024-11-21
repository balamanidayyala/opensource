S=input().strip()
redu=""
count=1
for i in range(1, len(S)):
    if S[i]==S[i-1]:
        count+=1
    else:
        redu+=S[i-1]+str(count)
        count=1
redu+=S[-1]+str(count)
print(redu)
    
