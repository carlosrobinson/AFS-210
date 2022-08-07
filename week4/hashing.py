# class HashItem: 
#     def __init__(self, key, value): 
#         self.key = key 
#         self.value = value 
        
        
class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size
        

    def hashfunction(self,key):
        # Insert your hashing function code
        mult = 1
        hv = 0
        for ch in [key]:
            hv += mult * ch
            mult += 1
        return hv % self.size 

    def rehash(self,key):
        # Insert your secondary hashing function code
        mult = 1
        hv = 0
        for ch in [key]:
            hv += mult * ch
            mult += 1
        return hv // self.size + 1

    def put(self,key,data):
        # Insert your code here to store key and data 
        h = self.hashfunction(key)
        while self.slots[h] is not None: 
            if self.slots[h] is key: 
                break 
            h = (h + 1) % self.size 
        self.slots[h] = key
        self.data[h] = data
            
            
            
        
 
    def get(self,key):
        # Insert your code here to get data by key
        h = self.hashfunction(key)
        if self.slots[h] is not None: 
            if self.slots[h] is key: 
                return self.data[h]
            h = (h+ 1) % self.size
        return None

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
# Store remaining input data
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# print the slot values
print(H.slots)

# print the data values
print(H.data)

# print the value for key 52
print(H.get(52))
