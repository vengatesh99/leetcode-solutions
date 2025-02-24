class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        perfect_match = set(wordlist)
        words_cap = {}
        words_vowel = {}
        ans = []
        def devowel(word):
            return "".join("*" if ch in "aeiou" else ch for ch in word)
        for word in wordlist:
            if word.lower() not in words_cap:
                words_cap[word.lower()] = word
            novowel = devowel(word.lower())
            if novowel not in words_vowel:
                words_vowel[novowel] = word
        for query in queries:
            if query in perfect_match:
                ans.append(query)
            elif query.lower() in words_cap:
                ans.append(words_cap[query.lower()])
            else:
                novowel = devowel(query.lower())
                if novowel in words_vowel:
                    ans.append(words_vowel[novowel])
                else:
                    ans.append("")
        return ans