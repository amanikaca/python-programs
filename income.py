name=input("enter the name: ")
income=int(input("enter your income: "))
print("enter your expenses ....")
#expenses=[]
total=0
count=0
for i in range(5):
    while True :
        value=input(f"expense{i+1} :")
        if not value.isdigit():
          print("invalid")
          continue
        expenses=int(value)    
        total+=expenses
        count+=1 
        break

print(f"total expenses ={total}")     
if total<income:
    print("profit")
elif total==income:
     print("no difference")
else:
    print("loss")
         
        
#output
#C:\Users\Dell\Desktop\-\Python>py income.py
#enter the name: Akku
#enter your income: 5000
#enter your expenses ....
#expense1 :1500
#expense2 :500
#expense3 :300
#expense4 :150
#expense5 :25
#total expenses =2475
#profit