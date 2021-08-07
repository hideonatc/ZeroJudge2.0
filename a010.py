n = int(input())
for i in range(2,100000000):
	cnt=0
	while n%i==0:
		n/=i
		cnt+=1
	if cnt==1:
		print(str(i),end='')
	elif cnt>1:
		print(str(i)+"^"+str(cnt),end='')
	if n!=1 and cnt!=0 :
		print(" * ",end='')
	if n==1 :
		print()
		break