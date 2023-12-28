class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        arr = []
        for i in range(n):
            arr.append([start[i],end[i]])
        selected = []
        
        # Sort jobs according to finish time
        arr.sort(key=lambda x: x[1])
        # The first activity always gets selected
        i = 0
        selected.append(arr[i])
 
        for j in range(1, n):
 
         '''If this activity has start time greater than or
           equal to the finish time of previously selected
           activity, then select it'''
         if arr[j][0] > arr[i][1]:
            selected.append(arr[j])
            i = j
        return len(selected)
