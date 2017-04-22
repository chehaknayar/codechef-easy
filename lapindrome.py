T=int(raw_input())
ans=[]
for i in range(0,T):
	char_list=list(raw_input())
	length=len(char_list)
	c=[]
	d=[]
	a=len(char_list)/2
	for i in range(0,a):
		c.append(char_list[i])
		c.sort()
   	if len(char_list)%2!=0:
 		a+=1		
	for j in range(a,length):
		d.append(char_list[j])
		d.sort()
	if c==d:
			ans.append('YES')
	else:
			ans.append('NO')
print '\n'.join(ans)
		 
