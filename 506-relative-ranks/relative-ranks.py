class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sorted = sorted(score,reverse=True)
        ans = []
        hash_map = {}
        rank = 4
        for i in range(len(score_sorted)):
            if i==0:
                hash_map[score_sorted[i]] = "Gold Medal"
            elif i ==1:
                hash_map[score_sorted[i]] = "Silver Medal"
            elif i == 2:
                hash_map[score_sorted[i]] = "Bronze Medal"
            else:
                hash_map[score_sorted[i]] = rank
                rank+=1
        for s in score:
            ans.append(str(hash_map[s]))
        return ans
        