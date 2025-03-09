# arithmetic operators
a=5
b=2

print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a%b) # remainder
print(a**b) # power a^b

  # relational operator
c=50
d=20
print(a==b) # flase 
print(a!=b)  # true
print(a>b)  # true 
print(a<b) # false 
print(a>=b) # true 
print(a<=b) # false 
  
# assignment operator 
num=20 
num=num+10
print("num:",num) # 20+10=30
# or 
num+=10
print("num:",num) # 30+10=40
num-=5
print("num:",num) # 40-5=35
num/=5
print("num:",num) # 35/5=7
num*=6
print("num:",num) # 7*6=42
num%=5
print("num:",num) # 42%5=2(remainder)
num**=4 
print("num:",num) # 2^4=16

 # logical operator 
m=2 
n=5
print(not False)
print(not (m==n))  # m not equal to n so not operator show reverse ans true 

val1= True 
val2= False 
print("and operation :",val1 and val2   ) # false 
print("or operation :",val1 or val2) # true 

print("and operation :",(m==n)and(m>=n)) # flase 
print("or operation :",(m==n)or(m>=n))  # true