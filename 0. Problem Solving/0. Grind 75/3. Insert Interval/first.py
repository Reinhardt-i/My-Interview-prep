class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        merged = []

        for interval in intervals :

            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else :
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    

"""
Time Complexity

	1.	Appending the new interval: This operation is O(1).
	2.	Sorting the intervals: Sorting takes O(n log n), where n is the number of intervals including the new interval.
	3.	Merging the intervals: This involves a single pass through the intervals, which is O(n).

Therefore, the overall time complexity is O(n log n) due to the sorting step.

"""