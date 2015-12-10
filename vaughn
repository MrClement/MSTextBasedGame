def vaughns():
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
	import time
	items = ['Meeuw', 'Mediocre Electronics Manifest', 'jquery.js', 'users', 'pacman.js']
	users = ['Clement, Alex']
	mema = ['Read Me', 'Manifest', 'Mediocre_Electronics.HTML']
	functions = {'ls': items}
	def usersa():
		user = raw_input('clement_alex: users clement_alex$')
		if(user=='ls'):
			print users
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
		else:
			print(user, 'is not a valid directory/folder')
			mem()
	def login():
		user = raw_input('clement_alex:~ clement_alex$')
		str(user)	
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
				print('sorry I do not understand that')
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
vaughns()
