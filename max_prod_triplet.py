# A O(n) Python3 program to find maximum 
# product pair in an array.
import sys

# Function to find a maximum product 
# of a triplet in array of integers 
# of size n 
def maxProduct(arr, n):

	# If size is less than 3, no
	# triplet exists
	if (n < 3):
		return -1

	# Initialize Maximum, second 
	# maximum and third maximum 
	# element
	maxA = -sys.maxsize - 1
	maxB = -sys.maxsize - 1
	maxC = -sys.maxsize - 1

	# Initialize Minimum and 
	# second minimum element
	minA = sys.maxsize
	minB = sys.maxsize

	for i in range(n):

		# Update Maximum, second 
		# maximum and third maximum 
		# element
		if (arr[i] > maxA):
			maxC = maxB
			maxB = maxA
			maxA = arr[i]
			
		# Update second maximum and 
		# third maximum element
		else if (arr[i] > maxB):
			maxC = maxB
			maxB = arr[i]
			
		# Update third maximum element
		else if (arr[i] > maxC):
			maxC = arr[i]

		# Update Minimum and second 
		# minimum element
		if (arr[i] < minA):
			minB = minA
			minA = arr[i]

		# Update second minimum element
		else if (arr[i] < minB):
			minB = arr[i]

	return max(minA * minB * maxA,
			maxA * maxB * maxC)

# Driver Code
arr = [ 1, -4, 3, -6, 7, 0 ]
n = len(arr)

Max = maxProduct(arr, n)

if (Max == -1):
	print("No Triplet Exists")
else:
	print("Maximum product is", Max)

# This code is contributed by avanitrachhadiya2155
