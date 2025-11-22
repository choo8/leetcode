class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products = [nums[-1]] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            products[i] = products[i + 1] * nums[i]

        forward_product = 1
        for i, n in enumerate(nums):
            if i == 0:
                products[i] = products[i + 1]
            elif i == len(nums) - 1:
                products[i] = forward_product
            else:
                products[i] = forward_product * products[i + 1]
            forward_product *= n

        return products


if __name__ == "__main__":
    solution = Solution()

    nums = [1,2,3,4]
    assert solution.productExceptSelf(nums) == [24,12,8,6]

    nums = [-1,1,0,-3,3]
    assert solution.productExceptSelf(nums) == [0,0,9,0,0]

