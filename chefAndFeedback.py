ans=[]
for i in xrange(int(raw_input())):
	fbk=raw_input()
	if "010" in fbk or"101" in fbk:
		ans.append("GOOD")
	else:
		ans.append("BAD") 
for j in xrange(len(ans)):
	print ans[j]