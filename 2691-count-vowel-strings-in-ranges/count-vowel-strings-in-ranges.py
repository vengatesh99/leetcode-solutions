class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a','e','i','o','u'}
        prefix_arr = [0 for _ in range(len(words)+1)]
        ans = []
        for i in range(len(prefix_arr)):
            prefix_arr[i] = prefix_arr[i-1]+ 1 if words[i-1][-1] in vowels and words[i-1][0] in vowels else prefix_arr[i-1]
        for l,r in queries:
            ans.append(prefix_arr[r+1]-prefix_arr[l])
        return ans