class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        triplets = set()
        for i in range(n - 1):
 
            # Find all pairs with sum
            # equals to "-arr[i]"
            s = set()
            for j in range(i + 1, n):
                x = -(arr[i] + arr[j])
                if x in s:
                   triplets.add(tuple(sorted([x,arr[i],arr[j]])))
                else:
                   s.add(arr[j])
        return len(triplets)
