from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k:int )-> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        tuples = [] 
        for num in freq:
            tuples.append((num, freq[num]))
        tuples = sorted(tuples, key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(tuples[i][0])
        return ans

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
ans = sol.topKFrequent(nums, k)
print(ans)
