class Solution:
    def countArrangement(self, n: int) -> int:
        permutations = [i for i in range(n+1)]
        def swap(i,j):
            temp = permutations[i]
            permutations[i]=permutations[j]
            permutations[j] = temp
        def recurse(ind,permutations):
            if ind == n+1:
                return 1 
            c = 0
            for i in range(ind,n+1):
                if (permutations[i]%(ind) == 0 or (ind)%permutations[i]==0):
                    permutations[ind],permutations[i] = permutations[i],permutations[ind]
                    c+=recurse(ind+1,permutations)
                    permutations[ind],permutations[i] = permutations[i],permutations[ind]
            return c

        return recurse(1,permutations)