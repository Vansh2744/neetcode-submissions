class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited_indices = set()
        for i in range(len(strs)):
            if i in visited_indices:
                continue
            arr = [strs[i]]
            visited_indices.add(i)
            for j in range(i + 1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    arr.append(strs[j])
                    visited_indices.add(j)

            result.append(arr)

        return result