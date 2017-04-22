T=int(raw_input())
ans=[]
for i in range(0,T):
	J=raw_input()
	S=raw_input()
	count=0
	for i in S:
		if i in J:
			count+=1
	ans.append(str(count))
print '\n'.join(ans)

