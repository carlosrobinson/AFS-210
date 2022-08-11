    def put(self,key,data):
        # Insert your code here to store key and data 
        items = [key, data]
        h = self.hashfunction(key)
        while self.slots[h] is not None:
            if self.slots[h] is key: 
                break 
            h = (h + 1) % self.size
        self.slots[h] = items[0]
        self.data[h] = items[1]