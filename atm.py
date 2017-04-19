x,y=(raw_input().split())
x,y=int(x),float(y)
round(y,2)
if x%5==0:
	if (0.5+x)<=y:
		print '%.2f'%(y-x-0.5)
	else:
		print '%.2f'%y 
else:
	print '%.2f'%y
		
