'''A bot starts at the origin — (0, 0)(0,0) — and can make the following moves:

(1) UP
(2) DOWN
(3) LEFT
(4) RIGHT
Each move has a magnitude of 1 unit. Accept the sequence of moves made by the bot as input. The first entry in the sequence is always START while the last entry in the sequence is always STOP. '''

steer = input()
x = 0
y = 0
while steer == 'START':
	
	steer = input()
	
	if steer == 'UP':
		y = y + 1
		steer = 'START'
		print(y)
	if steer == 'DOWN':
		y = y - 1
		steer = 'START'
		print(y)
	if steer == 'RIGHT':
		x = x + 1
		steer = 'START'
		print(x)
	if steer == 'LEFT':
		x = x -1
		steer = 'START'
		print(x)
	if steer == 'STOP':
		break
		
print(abs(x) + abs(y))	
