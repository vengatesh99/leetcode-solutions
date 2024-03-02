class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = 0
        my_dict = {0:-1}
        for i in range(len(nums)):
            pre_sum+=nums[i]
            pre_sum %= k
            if pre_sum == 0 and i>0:
                return True
            elif pre_sum in my_dict:
                if (i - my_dict[pre_sum]) > 1:
                    return True
            else:
                my_dict[pre_sum] = i
            
        return False