import math
a,b,c = map(int,input().split())
k = b*b-4*a*c
if k > 0 :
	print("Two different roots x1="+str(int((-b+math.sqrt(k))/(2*a)))+" , x2="+str(int((-b-math.sqrt(k))/(2*a))))
elif k == 0 :
	print("Two same roots x="+str(int((-b/(2*a)))))
else :
	print("No real root")