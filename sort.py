#Sort a List of Tuples by the Second Item Using Lambda Function.
# [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("David", 85)]  


data = [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("David", 85)]
sorted_data = sorted(data, key=lambda x: x[1])

print(f"sorted :{sorted_data}")

#output

#sorted :[('Bob', 72), ('David', 85), ('Alice', 88), ('Charlie', 95)]