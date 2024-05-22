class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        max_arr, min_arr = [0] * n, [0] * n

        # Calculate the minimum prices from the start to each index
        min1 = float('inf')
        for i in range(n):
            if prices[i] < min1:
                min1 = prices[i]
            min_arr[i] = min1

        # Calculate the maximum prices from each index to the end
        max1 = 0
        for i in range(n - 1, -1, -1):
            if prices[i] > max1:
                max1 = prices[i]
            max_arr[i] = max1

        # Find the maximum difference between max and min arrays
        ans = 0
        for i in range(n):
            x = max_arr[i] - min_arr[i]
            if x > ans:
                ans = x

        return ans
    

    """
    TC, SC = O(N)
    """