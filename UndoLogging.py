import sys
import copy
disc = {}
mainmemory = {}
sha1=0
a = []
fg=0
varx={}
ff=0
arf=0
local = {}
local1=0
active = []
countz=0
maxlen = 0
i = 0
def end_line2(temp):
	temp =  map(lambda x: x.strip(), temp)
	return temp 
fname = sys.argv[1]
q = int(sys.argv[2])
mz=[]
r4=0
transactions = {}
r5=0
mapping = {}
mm = 0
mm1=0
flag = 0
fileopen="2018201065_1.txt"
fout = open(fileopen, "w")

def getting_max_len():
	global maxlen
	global transactions
	for i in transactions.keys():
		if maxlen < len(transactions[i]):
			maxlen = len(transactions[i])

def end_line1(temp):
	temp =  map(lambda x: x.strip(), temp)
	return temp 

def getting_round_robin_transaction():
	i = 0
	global maxlen
	global a
	while i < maxlen:
		global transactions
		trans_keys=transactions.keys()
		for j in trans_keys:
			x = 0
			q_val=q
			len_trans=len(transactions[j])
			while x < q_val :
				if x+i<len_trans:
					tuple_t=(j,transactions[j][x+i])
					a.append(tuple_t)
					x = x + 1 
				else:
					break

		i = i + q
def end_line(temp):
	temp =  map(lambda x: x.strip(), temp)
	return temp 

def file_read():
	with open(fname,'r') as f:
		c = 0
		global flag
		flag1=0
		global mm
		global transactions
		for line in f:
			res1=0
			if c == 0:
				var = line.split(" ")
				var1=var
				i = 0
				len_var=len(var)
				while i < len_var:
					temp4=var[i]
					convstrvar=var[i+1]
					convstrint=int(convstrvar)
					disc[var[i]]=convstrint
					copyformem=convstrint
					mainmemory[var[i]]=copyformem
					i=i+2
			else:
				if flag == 1:
					global mm
					var = line.split(" ")
					w4=var[0]
					mapping[var[0]]=mm
					mapping[mm]=var[0]
					varx[mm]=[]
					at = var[0]
					flag = 0
					transactions[mm]=[]
					mm = mm + 1
					
				else:
					if line=="\n":
						flag = 1
						flag1=1
					else:
						
						flag = 0
						# print(at)
						flag1=0
						mapping_point=mapping[at]
						transactions[mapping_point].append(line)
			flag1=0
			c = c + 1

file_read()
getting_max_len()



getting_round_robin_transaction()


# print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
# print(a)

trans = map(lambda x: (x[0], x[1].strip("\n")), a)

nl = 0


def file_write(fout,ans):
	fout.write(ans)
	# fout.write("\n")

for i in trans:
	x1=0
	if i[0] not in active:
		trans_name=i[0]
		active.append(i[0])
		wr=''
		wr = '<START '+ mapping[i[0]]+'>'
		flag=1
		kk = mainmemory.keys()
		###memory keys
		kk.sort()
		file_write(fout,wr)
		file_write(fout,"\n")
		sp = 0
		for w in kk:
			if w in mz:
				if sp == 0:
					tempstr=mainmemory[w]
					str1=str(tempstr)
					wr=w+" "+str1
				else:
					tempstr=mainmemory[w]
					str1=str(tempstr)
					wr = " "+w+" "+str1
				sp = sp + 1
				file_write(fout,wr)
		file_write(fout,"\n")
		kk = disc.keys()
		flag=1
		kk.sort()
		sp = 0
		for w in kk:
			if sp == 0:
				tempstr=disc[w]
				str1=str(tempstr)
				wr=w+" "+str1
			else:
				tempstr=disc[w]
				str1=str(tempstr)
				wr = " "+w+" "+str1
			sp = sp + 1
			file_write(fout,wr)
		file_write(fout,"\n")
	
	e = i[1]
	
	if '=' in e:
		
		temp = e.split(':=')
		#remove \n
		temp=end_line(temp)
		w5=temp[0]
		w6=temp[1]
		m1=copy.deepcopy(mainmemory)
		#need to evaluate equal
		z4= eval(temp[1], m1, local)
		w8=temp[0]
		local[temp[0]]=z4

	if 'READ' in e:
		temp1=""
		temp = e.split('(')[1].split(')')[0].split(',')
		#first read 
		temp=end_line(temp)
		#than remove \n
		mem2=0
		mem1=temp
		r4=temp[1]
		var_local=temp[1]
		local[temp[1]] = mainmemory[temp[0]]
		flag=1
		#variable list mei nahi 
		#har transaction ke saame dict insert ke samne read and than utput mei pop
		if temp[0] not in varx[i[0]]:
			rf1=temp[0]
			mz.append(temp[0])
			transaction_no=i[0]
			varx[i[0]].append(temp[0])
			flag=0
	if 'WRITE' in e:
		temp2=""
		temp = e.split('(')[1].split(')')[0].split(',')
		temp3=""
		temp=end_line(temp)
		#mapping mei T1 ko ek value assign
		wr=""
		wr = '<'+mapping[i[0]]+', '+temp[0]+', '+str(mainmemory[temp[0]])+'>'
		wz1=wr
		file_write(fout,wr)
		mainmemory[temp[0]] = local[temp[1]]
		file_write(fout,"\n")
		#list of keys and sort them
		kk = mainmemory.keys()
		flag=1
		kk.sort()
		sp = 0
		####main_memory and dick variable printing
		for w in kk:
			if w in mz:
				if sp == 0:
					tempstr=mainmemory[w]
					str1=str(tempstr)
					wr=w+" "+str1
				else:
					tempstr=mainmemory[w]
					str1=str(tempstr)
					wr = " "+w+" "+str1
				sp = sp + 1
				file_write(fout,wr)
		file_write(fout,"\n")
		kk = disc.keys()
		flag=1
		kk.sort()
		sp = 0
		for w in kk:
			if sp == 0:
				tempstr=disc[w]
				str1=str(tempstr)
				wr=w+" "+str1
			else:
				tempstr=disc[w]
				str1=str(tempstr)
				wr = " "+w+" "+str1
			sp = sp + 1
			file_write(fout,wr)
		file_write(fout,"\n")

	#main memory and disc variable printing end
	if 'OUTPUT' in e:
		
		temp = e.split('(')[1].split(')')[0]
		main_mem_temp=mainmemory[temp]
		disc_temp=disc[temp]
		disc[temp] = main_mem_temp
		l = varx[i[0]]
		remove_char=temp
		l.remove(remove_char)
		if len(l) == 0:
			wr=""
			wr = '<COMMIT '+ mapping[i[0]]+'>'
			file_write(fout,wr)
			kk = mainmemory.keys()
			kk.sort()
			file_write(fout,"\n")
			sp = 0
			for w in kk:
				if w in mz:
					if sp == 0:
						tempstr=mainmemory[w]
						str1=str(tempstr)
						wr=w+" "+str1
					else:
						tempstr=mainmemory[w]
						str1=str(tempstr)
						wr = " "+w+" "+str1
					file_write(fout,wr)
					sp = sp + 1

			file_write(fout,"\n")
			kk = disc.keys()
			kk.sort()
			sp = 0
			for w in kk:
				if sp == 0:
					tempstr=disc[w]
					str1=str(tempstr)
					wr=w+" "+str1
				else:
					tempstr=disc[w]
					str1=str(tempstr)
					wr = " "+w+" "+str1
				file_write(fout,wr)
				sp = sp + 1
			# if nl != len(trans)-1:
			file_write(fout,"\n")
	nl = nl + 1
fout.close()