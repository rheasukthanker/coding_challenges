'''Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.'''

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: for S1, return '0'
        if n == 1:
            return "0"

        # Calculate the length of Sn
        length = 1 << n  # Equivalent to 2^n
        print(length)
        # If k is in the first half of the string, recurse with n-1
        if k < length // 2:
            return self.findKthBit(n - 1, k)

        # If k is exactly in the middle, return '1'
        elif k == length // 2:
            return "1"

        # If k is in the second half of the string
        else:
            # Find the corresponding bit in the first half and invert it
            corresponding_bit = self.findKthBit(n - 1, length - k)
            return "1" if corresponding_bit == "0" else "0"
