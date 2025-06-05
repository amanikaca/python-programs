print("enter two numbers")
a=int(input("enter the first number : "))
b=int(input("enter the second number : "))

mylist = list(map(int, input("Enter the numbers separated by space: ").split()))

#Arithemetic operators
print("\n ----------Arithemetic operators ----------")
print(f"add : {a+b}")
print(f"subtraction :{a-b}")
print(f"multiplication : {a*b}")
print("division Invalid" if b == 0 else f"division : {a / b}")
print("floor division Invalid" if b == 0 else f"floor division : {a//b}")
print(f"exponential : {a**b}")
print("modulus is  Invalid" if b == 0 else f"modulus : {a%b}")

#assignment operators
print("\n ----------Assignment operators ----------")
x=a
x+=b
print(f"x+=b: {x}")
x-=b
print(f"x-=b: {x}")
x*=b
print(f"x*=b: {x}")
x/=b
print(f"x/=b: {x}")
#comparison operators
print("\n ----------comparison  operators ----------")
print(f"a==b :{a==b}")
print(f"a!=b :{a!=b}")
print(f"a<=b :{a<=b}")
print(f"a>=b :{a>=b}")
print(f"a<b :{a<b}")
print(f"a>b :{a>b}")
#logical operators
print("\n ----------logical  operators ----------")
print(f"a<5 and b>5 :{a<5 and b>5}")
print(f"a<5 or b>5 :{a<5 or b>5}")
print(f"not(a>5) :{not(a>5)}")
#bitwise operators
print("\n ----------bitwise operators ----------")
print(f"a&b :{a&b}")
print(f"a|b :{a|b}")
print(f"a^b :{a^b}")
print(f"a<<b :{a<<b}")
print(f"a>>b :{a>>b}")
print(f"~a :{~a}")
#special operators
print("\n ----------special operators ----------")
 #Identity operators
print("\n    ----------identity operators ----------")
 
print(f"a is b :{a is b}")
print(f"a is not b :{a is not  b}")
 #membership operators
print("\n    ----------membership operators ----------")
print(mylist)
print(f"a in mylist :{a in mylist}")
print(f"b not in mylist :{a not  in mylist}")
