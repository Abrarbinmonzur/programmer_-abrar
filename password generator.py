import random 
upper="ASDFGHJKL"
lower="brinmozu"
number="1234567890"
symbol="!@#$"
string= upper+lower+number+symbol
length=8
password="".join(random.sample(string,length))
print("password you generated is."+ password)