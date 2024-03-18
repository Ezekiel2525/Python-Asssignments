s1, s2, s3 = [], [], []
for i in range(3):
    se1 = int(input("Enter the number for the first set: "))
    se2 = int(input("Enter the number for the second set: "))
    se3 = int(input("Enter the number for the third set: "))
    s1.append(se1)
    s2.append(se2)
    s3.append(se3)
set1, set2, set3 = set(s1), set(s2), set(s3)
print(set1, set2, set3)
operation = input("""
                    1. union
                    2. Intersection
                    >>>   """)
if operation == "1":
    set4 = set1.union(set2).union(set3) 
    print(set4)
elif operation == "2":
    set4 = set1.intersection(set2).intersection(set3)
    print(set4)