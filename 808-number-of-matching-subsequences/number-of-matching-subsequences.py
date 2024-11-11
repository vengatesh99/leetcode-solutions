class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        group_dict = defaultdict(list)
        ans = 0
        for word in words:
            group_dict[word[0]].append((word,0))
        for i,ch in enumerate(s):
            if ch in group_dict:
                word_state = group_dict[ch]
                del group_dict[ch]
                for state_word,state_ind in word_state:
                    new_state_ind = state_ind+1
                    if new_state_ind == len(state_word):
                        group_dict[None].append(state_word)
                    else:
                        group_dict[state_word[new_state_ind]].append((state_word,new_state_ind))
        return len(group_dict[None])
                

