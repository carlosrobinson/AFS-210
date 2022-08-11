class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size
        

    def hashfunction(self,key):
        # Insert your hashing function code
        hash_key = str(key)
        hv = 0
        for ch in hash_key:
            hv +=  ord(ch)
        return (hv * len(hash_key))  % self.size
        

    def rehash(self,key):
        # Insert your secondary hashing function code
        return key // self.size 

    def put(self,key,data):
        # Insert your code here to store key and data 
        items = [key, data]
        h = self.hashfunction(key)
        if self.slots[h] is None:
            self.slots[h] = items[0]
            self.data[h] = items[1]
        else:
            if self.slots[h] is key:
              self.data[h] = items[1]  
            else:
                h = self.rehash(key)
                if self.slots[h] is None:
                    self.slots[h] = items[0]
                    self.data[h] = items[1]
                else:
                    return None
            
        
 
    def get(self,key):
        # Insert your code here to get data by key
        h = self.hashfunction(key)
        if self.slots[h] is key: 
            return self.data[h]
        else:
            h = self.rehash(key)
        if(self.slots[h] == key):
            return self.data[h]
        else:
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
