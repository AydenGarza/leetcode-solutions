class Solution:
    def longestConsecutive(self, nums:List[int]) -> int:
        num_set = set(nums)
        starts = set()
        
        max_len = 0
        for num in nums:
            if num-1 not in num_set and num not in starts:
                print(num)
                curr_len = 0
                curr_num = num
                while curr_num in num_set:
                    curr_len+=1
                    curr_num+=1
                starts.add(num)
                max_len=max(max_len, curr_len)
                 
        return max_len
