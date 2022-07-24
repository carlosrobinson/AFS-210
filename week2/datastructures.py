Data1 = (7, False, "Apple", True, 7, 98.6) 

Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}

Data3 = ["A", 7, -1, 3.14, True, 7 ] 

Data4 =  {"name": "Joe",  "age": 26,   "active": True,  "hourly_wage": 14.75}


# Data1
print(end="Data set 1: \n\t")
print(len(Data1))
print(end="\t")
print(Data1[3])
print(end="\t")
print(Data1.count(7))
print(end="\t")
print(end="\n")


# Data2
print(end="Data set 2: \n\t")
removedItem = Data2.pop()
print(f'The item "{removedItem}" was removed')
Data2.add("Alpha")
print(end="\t")
print(Data2)
print(end="\n")


# Data3
print(end="Data set 3: \n\t")
reversed(Data3)
newData = Data3[::-1]
newData[1] = "B"
newData.remove("A")
print(newData)
print(end="\n")


# Data4
print(end="Data set 4: \n\t")
hourly_wage = Data4.get("hourly_wage")
pay = hourly_wage * 40
print(pay, end="\n")
Data4.update({"active": False})
Data4.update({"address": "123 West Main Street"})
print(end="\t")
print(Data4)

