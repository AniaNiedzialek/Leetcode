from typing import List

class Solution:
	def findMinArrowShots(self, points: List[List[int]]) -> int:
		size = len(points)
		if size <= 1:
			return size

		points = sorted(points, key=lambda x: x[0])
		# print(points)
		result = []

		for interval in points:
			if len(result) == 0:
				result.append(interval)
			else:
				if self.hasOverlap(result[-1], interval):
					result[-1][0] = max(result[-1][0], interval[0])
					result[-1][1] = min(result[-1][1], interval[1])
				else:
					result.append(interval)

		# print(result)
		return len(result)



	def hasOverlap(self, interval_a: List[int], interval_b: List[int]) -> bool:
		if (
			interval_a[0] <= interval_b[0] <= interval_a[1] or
			interval_a[0] <= interval_b[1] <= interval_a[1]
			
		):
			return True

		# if (
		# 	interval_b[0] <= interval_a[0] <= interval_b[1] or
		# 	interval_b[0] <= interval_a[1] <= interval_b[1]
		# ):
		# 	return True

		return False