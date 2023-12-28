class Solution:
    def allPairs(self, A, B, N, M, X):
        #  Compute pairs in A and B summing up to X
        complements_A = {}
        for a in A:
            complements_A[X-a] = a 
        pairs = []
        for b in B:
            if b in complements_A:
                #print(complements_A[b],b)
                pairs.append((complements_A[b],b))
        return sorted(pairs)
