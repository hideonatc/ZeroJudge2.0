s = input()
for i in s:
	print(chr(ord(i)+ord('*')-ord('1')),end='')
print()