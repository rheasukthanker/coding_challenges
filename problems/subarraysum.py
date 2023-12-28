class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       # O(n^2) still bad 
       '''start_idx = -1
       end_idx = -1
       if len(arr) == 1:
           if sum(arr) == s:
               return [1,1]
           else:
               return [-1]
       for i in range(n):
           sum_arr = arr[i]
           if sum_arr == s:
               start_idx = i+1
               end_idx = i+1
               break
           for j in range(i+1,n):
               sum_arr = sum_arr + arr[j]
               if sum_arr == s:
                   start_idx = i+1
                   end_idx = j+1
                   break
           if sum_arr == s:
               break
       if end_idx == -1:
           return [-1]
       else:
           return [start_idx, end_idx]'''
       # O(nlog(n)) still nor optimal
       '''if len(arr) == 1:
           if sum(arr) == s:
               return [1,1]
           else:
               return [-1]
       start_pointer = 0
       end_pointer = 1
       sum_arr = 0
       flag = True
       while start_pointer<=n-1 and end_pointer<=n-1:
           if flag:
              sum_arr = arr[start_pointer]
              if sum_arr == s:
                 return [start_pointer+1, start_pointer+1]
              flag = False
              if sum_arr > s:
                  end_pointer = start_pointer+2
                  start_pointer = start_pointer+1
                  flag = True
                  continue 
           sum_arr = sum_arr + arr[end_pointer]
           if sum_arr == s:
               break
           elif sum_arr > s:
                end_pointer = start_pointer+2
                start_pointer = start_pointer +1
                flag = True
           else:
               end_pointer = end_pointer+1
       if sum_arr!=s:
            return [-1]
       return [start_pointer+1,end_pointer+1]'''
       # O(n) -> quite elegant
       curr_sum = 0
       index_map = {}
       target_sum = s
       for i, num in enumerate(arr):
        curr_sum += num
        if curr_sum == target_sum:
            return [1, i+1]
        if curr_sum - target_sum in index_map:
            return [index_map[curr_sum - target_sum] + 2, i+1]
        index_map[curr_sum] = i
       return [-1]
