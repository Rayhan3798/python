# type conversion 
# 2 type one is conversion (automatically done by python) and casting (manually)
# conversion
a=2
b=2.25
sum=a+b
print("sum=",sum) #  output float value 4.25
# here float is superior value which python conver 2 int value in float value

#casting 
# c="2"
d=2
# sum=c+d
# print(sum) # where c is a str value so python can't convert 
c=int("2")
sum=c+d
print(sum)