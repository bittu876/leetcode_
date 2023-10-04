class MyHashMap(object):

    def __init__(self):
        self.hash_table = {}
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hash_table[key] = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_table.keys():
           return -1
        else:
            return self.hash_table[key]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hash_table.keys(): 
            del self.hash_table[key]
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)