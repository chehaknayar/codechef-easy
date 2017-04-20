computed_jobs=[]
jobs_to_be_done=[]
T=int(raw_input())
n=[]
m=[]
completed_jobs_list=[]
jobs_to_be_done_list=[]
for i in range(0,T):
	
	a,b=raw_input().split()
	a,b=int(a),int(b)
	n.append(a)
	m.append(b)
	completed_jobs = map(int, raw_input().split())
	completed_jobs_list.append(completed_jobs)
	
for j in range(0,len(completed_jobs_list)):
	jobs_to_be_done=[]
	for k in range(0,n[j]):
		if k+1 not in completed_jobs_list[j]:
			jobs_to_be_done.append(k+1)
			jobs_to_be_done.sort()

	jobs_to_be_done_list.append(jobs_to_be_done)		

chefs_jobs=[]
assistants_jobs=[]
for l in range(0,T):
	for p in range(0,len(jobs_to_be_done_list[l])):
		if p%2==0:
			chefs_jobs.append(jobs_to_be_done_list[l][p])
			chefs_jobs = map(str, chefs_jobs)
			
		else:
			assistants_jobs.append(jobs_to_be_done_list[l][p])
			assistants_jobs = map(str, assistants_jobs)
	
	print " ".join(chefs_jobs)
	print " ".join(assistants_jobs)
	chefs_jobs=[]
	assistants_jobs=[]

