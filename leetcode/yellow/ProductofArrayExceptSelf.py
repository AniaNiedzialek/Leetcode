from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        answer = [0] * size
        answer[0] = 1

    


        for i in range(1, size):
            answer[i] = nums[i - 1] * answer[i - 1]
        power = 1
            
                # print(f"j is {j}")
           
        for i in reversed(range(size)):
            answer[i] = answer[i] * power
            power *= nums[i] 


            
        # print(f"answer is {answer}")
        return answer 
    

if __name__ == '__main__':
    solution = Solution()
    
    # Test Case 1:
    nums = [1,2,3,4]
    print(solution.productExceptSelf(nums))