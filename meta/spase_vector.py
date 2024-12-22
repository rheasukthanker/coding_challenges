'''Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?'''

# TC: O(n), SC O(1)
class SparseVector:
    def __init__(self, nums):
        self.array = nums

    def dotProduct(self, vec):
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1 * num2
        return result

# TC: O(n), SC O(n)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.non_sparse_inds = []
        for i,n in enumerate(nums):
            if n!=0:
                self.non_sparse_inds.append(i)
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dp = 0
        sparsity_me = len(self.non_sparse_inds)
        sparsity_vec = len(vec.non_sparse_inds)
        min_length = min(sparsity_me,sparsity_vec)
        if min_length ==  sparsity_me:
            for ind in self.non_sparse_inds:
                dp = dp + self.nums[ind]*vec.nums[ind]
        else:
            for ind in vec.non_sparse_inds:
                dp = dp + self.nums[ind]*vec.nums[ind]
        return dp



        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
