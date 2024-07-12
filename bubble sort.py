lis = [7,15,6,8,90,56]

for i in range(len(lis)):
    for j in range(0,len(lis)-i-1):
        if lis[j]>lis[j+1]:
            lis[j+1],lis[j]=lis[j],lis[j+1]

print(lis)