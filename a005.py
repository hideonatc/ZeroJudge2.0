t=int(input())
for i in range(0,t) : 
	a,b,c,d = map(int,input().split())
	if a+c==2*b and b+d==2*c :
		print(a,b,c,d,2*d-c)
	else :
		print(a,b,c,d,int(d*d/c))