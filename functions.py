#list
print("list")
print("-----")
my_list=[1,3,4,6,2]
string=["a","b",'c','d']
print(f"my_list :{my_list}")
my_list.append(5)
print(f"append 5 in the list :{my_list}")
my_list.insert(1,9)
print(f"insert 9 at 1st index :{my_list}")
my_list.extend(string)
print(f"extend list :{my_list}")
print(f"1 index  is pop from list:{my_list.pop(1)}")
print(f"remaining list :{my_list}")
my_list.remove('a')
print(f"a is removed from list {my_list}")
names=['u','a','i','n','a']
print(f"names :{names}")
names.sort()
print(f"sorted names :{names}")
names.reverse()
print(f"reversed :{names}")
print(f"index of i :{names.index("i")}")
print(f"count of a in names list :{names.index('a')}")
print(f"length of names:{len(names)}")

#tuple
print("tuple")
print("------")
tuple=(2,5,7,9,7)
print(f"tuple :{tuple}")
print(f"index of 5 :{tuple.index(5)}")
print(f"count of 7 :{tuple.count(7)}")
print(f"length of tuple :{len(tuple)}")

#set
print("set")
print('-----')
set = {1, 2, 3,4,5,6,7}
print(f"my set :{set}")
set.add(8)
print(f"add 8 to the set {set}")
set.remove(7)
print(f"remove 3 from set:{set}")
set.discard(2)
print(f"discard 2 from set :{set}")
set.pop()
print(f"pop :{set}")
set.clear()
print(f"clear :{set}")
set1={1,6,8,43,5}
set2={6,8,9,3,56}
print(f"set1:{set1}")
print(f"set2:{set2}")
result=set1.union(set2)
print(f"union of set1 and set2 :{result}")
result2=set1.intersection(set2)
print(f"intersection of set1 and set2:{result2}")
result3=set1.difference(set2)
print(f"difference of set1 and set2:{result3}")
result4=set1.issuperset(set2)
print(f"superset :{result4}")

#dictionary
print("dictinary")
print("==========")
dict = {'name': 'Amanika', 'age': 22}
print(f"dictionary :{dict}")
print(f" name:{dict.get('name')}")
print(f"{dict.keys()}")
print(f"{dict.values()}")
print(f"{dict.items()}")
dict1= {'name':'Arun','age':23,'dept':'cse'}
print(f"dictionary 1:{dict1}")
dict.update(dict1)
print(f"update dictionary :{dict}")
dict.pop('name')
print(f"pop:{dict}")
dict.popitem()
print(f"popitem:{dict}")
print(f"length :{len(dict)}")
dict.clear()
print(f"clear :{dict}")

#output
#list
#-----
#my_list :[1, 3, 4, 6, 2]
#append 5 in the list :[1, 3, 4, 6, 2, 5]
#insert 9 at 1st index :[1, 9, 3, 4, 6, 2, 5]
#extend list :[1, 9, 3, 4, 6, 2, 5, 'a', 'b', 'c', 'd']
#1 index  is pop from list:9
#remaining list :[1, 3, 4, 6, 2, 5, 'a', 'b', 'c', 'd']
#a is removed from list [1, 3, 4, 6, 2, 5, 'b', 'c', 'd']
#names :['u', 'a', 'i', 'n', 'a']
#sorted names :['a', 'a', 'i', 'n', 'u']
#reversed :['u', 'n', 'i', 'a', 'a']
#index of i :2
#count of a in names list :3
#length of names:5
#tuple
#------
#tuple :(2, 5, 7, 9, 7)
#index of 5 :1
#count of 7 :2
#length of tuple :5
#set
#-----
#my set :{1, 2, 3, 4, 5, 6, 7}
#add 8 to the set {1, 2, 3, 4, 5, 6, 7, 8}
#remove 3 from set:{1, 2, 3, 4, 5, 6, 8}
#discard 2 from set :{1, 3, 4, 5, 6, 8}
#pop :{3, 4, 5, 6, 8}
#clear :set()
#set1:{1, 5, 6, 8, 43}
#set2:{3, 6, 8, 9, 56}
#union of set1 and set2 :{1, 3, 5, 6, 8, 9, 43, 56}
#intersection of set1 and set2:{8, 6}
#difference of set1 and set2:{1, 43, 5}
#superset :False
#dictinary
#==========
#dictionary :{'name': 'Amanika', 'age': 22}
 #name:Amanika
#dict_keys(['name', 'age'])
#dict_values(['Amanika', 22])
#dict_items([('name', 'Amanika'), ('age', 22)])
#dictionary 1:{'name': 'Arun', 'age': 23, 'dept': 'cse'}
#update dictionary :{'name': 'Arun', 'age': 23, 'dept': 'cse'}
#pop:{'age': 23, 'dept': 'cse'}
#popitem:{'age': 23}
#length :1
#clear :{}