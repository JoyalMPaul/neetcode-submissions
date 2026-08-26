class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for string in strs:
            sort = sorted(string)

            anagram = [0] * 26
            for s in sort:
                anagram[ord(s) - ord("a")] += 1

            anagram = tuple(anagram)
            
            seen[anagram].append(string)
        
        return list(seen.values())