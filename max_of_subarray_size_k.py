#User function Template for python3
import math
class Solution:
    
 #Function to find maximum of each subarray of size k.
 def max_of_subarrays(self,arr,n,k):
        
    """ Create a Double Ended Queue, Qi that 
    will store indexes of array elements. 
    The queue will store indexes of useful 
    elements in every window and it will
    maintain decreasing order of values from
    front to rear in Qi, i.e., arr[Qi.front[]]
    to arr[Qi.rear()] are sorted in decreasing
    order"""
    Qi = deque()
    K = k
    N = n
 
    # Process first k (or first window)
    # elements of array
    for i in range(K):
 
        # For every element, the previous
        # smaller elements are useless
        # so remove them from Qi
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
 
        # Add new element at rear of queue
        Qi.append(i)
 
    # Process rest of the elements, i.e.
    # from arr[k] to arr[n-1]
    li_max  = []
    for i in range(K, N):
 
        # The element at the front of the
        # queue is the largest element of
        # previous window, so print it
        li_max.append(arr[Qi[0]])
 
        # Remove the elements which are
        # out of this window
        while Qi and Qi[0] <= i-K:
 
            # remove from front of deque
            Qi.popleft()
 
        # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
 
        # Add current element at the rear of Qi
        Qi.append(i)
 
    # Print the maximum element of last window
    li_max.append(arr[Qi[0]])
    return li_max
