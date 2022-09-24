def traders():
	'''recieves employment id until its '-1', and collects trade amounts until its 0 and sums the trade amounts'''
	
	id = input('id: ')
	while (id != '-1'):
		trade_amount = int(input('enter amounts: '))
		profit_loss = 0
		while (trade_amount !=0):
			profit_loss += trade_amount
			trade_amount = int(input('enter amounts: '))
			
		print(f'profit/loss for employee {id} is {profit_loss}')
		id = input('\nid: ')
			
traders()	
