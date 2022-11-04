import random
start = int(input('請輸入起始值:'))
end = int(input('請輸入終值:'))
pwd = random.randint(start,end)
count = 0
while True:
	count += 1
	user = int(input('請猜一個數字:'))
	if user == pwd:
		print('猜對了')
		print('你猜了第{}次'.format(count))
		break
	elif user > pwd:
		print('比答案大')
	else:
		print('比答案小')
	print('你猜了第{}次'.format(count))