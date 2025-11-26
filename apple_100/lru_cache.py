#https://leetcode.com/problems/lru-cache/
class LRUCache:

    def __init__(self, capacity: int):
        self.d={}
        self.cap=capacity
    def get(self, key: int) -> int:
        retval=self.d.get(key,-1)
        if retval!=-1:
           del self.d[key]
           self.d[key]=retval
        return retval
        

    def put(self, key: int, value: int) -> None:
        present=False
        val=self.d.get(key,-1)
        flag=key in self.d.keys()
        if val==-1:
         if len(self.d)>=self.cap:
          if flag:
             del self.d[key]
          else:
              del self.d[list(self.d.keys())[0]]
         else:
          if flag:
             del self.d[key]
        else:
            del self.d[key]
        self.d[key]=value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)