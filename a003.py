m,d = input().split()
m,d = int(m),int(d)
if (m*2+d)%3 == 0 :
	print("普通")
elif (m*2+d)%3 == 1 :
	print("吉")
else :
	print("大吉")