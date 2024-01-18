class Solution(object):
    def topKFrequent(self, nums, k):
        orb = {}

        for i in nums:
            if i in orb:
                orb[i] += 1
            else: orb[i] = 1
        
        sorted_orb = sorted(orb, key=orb.get, reverse=True)
        print(sorted_orb)
        return sorted_orb[:k]
