def vaughns():
	import time
	def netstat():
		print 'Active Internet connections'
		print 'Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)'
		time.sleep(1)
		print'tcp4       0      0  10.80.9.46.64499       17.134.62.217.https    SYN_SENT'
		print'tcp4       0   1436  10.80.9.46.64498       kdsdcprime.kentd.ldap  ESTABLISHED'
	def clear():
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
		print('')
	items = ['Meeuw', 'Mediocre Electronics Manifest', 'jquery.js', 'users', 'pacman.js']
	users = ['Clement, Alex']
	files = ['my documents', 'treasure map', 'kali']
	mema = ['Read Me', 'Manifest', 'Mediocre_Electronics.HTML']
	functions = {'ls': items}
	def filesa():
		user = raw_input('clement_alex: users clement_alex$')
		if(user=='pwd'):
			login()
		x = user[:3]
		if(x=='cd treasure map'):
			print("you don't have the authority to acess that file")
		print(user[3:], 'is not a valid directory')
		filsa()
	def usersa():
		user = raw_input('clement_alex: users clement_alex$')
		if(user=='ls'):
			print users
			usersa()
		if(user=='cd clement, alex'):
			print files
			filesa()
		else:
			print 'invalid syntax'
			usersa()
		if(user=='pwd'):
			login()
	def mem():
		user = raw_input('clement_alex: Mediocre_Electronics_Manifest clement_alex$')
		if(user=='pwd'):
			login()
		if(user=='ls'):
			print mema
			mem()
		if(user=='./Read Me'):
			print('At mediocre electronics we strive to fulfill one rule and one rule only, achieve complete and total mediocrity in all of our work here. This is why we feel that you should never use one of our products without talking to an adult first, this of course is only because we are terribly conserned about your mental health and just remember the frustration that our products bring you is not worth it.')
			mem()
		if(user=='./Manifest'):
			print("print('hi')")
			mem()
		if(user=='reboot'):
			print('powering down ubuntu shell')
			time.sleep(2)
			clear()
			return 0
		if(user=='help'):
			print ('Mr. Clement you told me to disable that command')
			mem()
		else:
			print(user, 'is not a valid directory/folder')
			mem()
	def login():
		user = raw_input('clement_alex:~ clement_alex$')
		str(user)
		if(user=='help'):
			print ('Mr. Clement you told me to disable that command')
			login()
		if(user=='reboot'):
			print('powering down ubuntu shell')
			time.sleep(2)
			clear()
			return 0
		x = user[:3]
		if(x=='cd '):
			y = user[3:]
			if(y=='users'):
				print users
				usersa()
			if(y=='Mediocre Electronics Manifest'):
				print mema
				mem()
			else:
				print(y, 'is not a valid directory')
			login()
		print (functions.get(user, "Sorry but I don't find that here"))
		login()
	def type():
		x = raw_input('Hello Please Enter Your Username')
		if(x=='clement'):
			y = raw_input('Hello Please Enter Your Password')
			if(y=='alex'):
				login()
			else:
				print('incorrect')
				type()
		else:
			print('incorrect')
			type()
	type()
