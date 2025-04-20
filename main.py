students=("Malak","Malika","Nadin","Nour")

print(students)

print("Best student:", students[0])
print(" Second Best student:", students[1])
print("Good student:", students[2])
print("Average student:", students[3])

print("The length of the tuple",len(students))
print("The index of Mazen:",students.index("Mazen"))
print("Occurence of Mazen:",students.count("Malak"))

for i in students:
    print("Loop is at :",i)