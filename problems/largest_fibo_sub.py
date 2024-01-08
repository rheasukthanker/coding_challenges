# find largest subsequence where all numbers are fibonacci
class Solution:
    def findFibSubset(self, arr, n):
        # code here
        max_num = max(arr)
        fibo_sub = []
        fibo_all = self.gen_fibo(max_num)
        for a in arr:
            if a in fibo_all:
                fibo_sub.append(a)
        return fibo_sub
        
    def gen_fibo(self,num):
        fibo_list = [0,1,1]
        while fibo_list[-1]<=num:
            fibo_list.append(self.fibo(fibo_list))
        return fibo_list
        
    def fibo(self,arr):
        return arr[-1]+arr[-2]
