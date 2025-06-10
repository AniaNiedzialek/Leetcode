class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # heap and visited set to ensure we dont go to the same index twice

        # heap - store the sume and the indices
        heap = [[nums1[0] + nums2[0], 0, 0]]
        res = []
        visited = set((0,0))     
        # case 1 - heap true and k > 0
        while heap and k > 0:
            _, i1, i2 = heappop(heap)
            res.append([nums1[i1], nums2[i2]])
            k -= 1
            # check before adding next values
            next_i = i1 + 1
            if next_i < len(nums1) and (next_i, i2) not in visited:
                heappush(heap, [nums1[next_i] + nums2[i2], next_i, i2])                
                visited.add((next_i, i2))
            next_i = i2 + 1
            if next_i < len(nums2) and (i1, next_i) not in visited:
                heappush(heap, [nums1[i1] + nums2[next_i], i1, next_i])
                visited.add((i1, next_i))
        return res

# time: O min(k log k (n1 + n2) * log(n1 + n2))
# space: O min(k, n1 * n2)