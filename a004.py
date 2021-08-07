try:
	while 1==1 :
		y = int(input())
		if y%400==0 or (y%4==0 and y%100!=00) :
			print("閏年")
		else :
			print("平年")
except EOFError:
	pass