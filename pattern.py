n = int(input("enter a number"))
x=2*n-1
ref = []
res=[]
temp = [n for i in range(2*n-1)]
res.append(temp)
count = 1
while count<n:
    temp = res[len(res) -1].copy()
    i=count
    j=x-1 -i  
    while i <= j:
         if i == j:
            temp[i] = temp[i] - 1
         else:
           temp[i] = temp[i] - 1
           temp[j] = temp[j] - 1
         i = i + 1
         j = j - 1
    res.append(temp)
    count = count+1
for i in res:
    ref.append(i)
for k in range(len(res)-2,-1,-1):
    ref.append(res[k])
for k in ref:
    print(k)


