#time of the day
t = int(input())
if t < 0 or t>=24 :
    print('INVALID')
    
elif 0<= t and t<=5:
    print('NIGHT')
    
elif 6<= t and t<=11:
    print('MORNING')
    
elif 12<= t and t<=17:
    print('AFTERNOON')
    
elif 18<= t and t<=23:
    print('EVENING')
