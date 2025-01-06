from collections import defaultdict, Counter
class Solution:
    def quickSort(self, arr, low, high, counterMap):
        if low >= high:
            return
        else:
            partition_ind = self.partitionFind(arr, low, high, counterMap)
            self.quickSort(arr, low, partition_ind - 1, counterMap)
            self.quickSort(arr, partition_ind + 1, high, counterMap)

    def partitionFind(self, arr, low, high, counterMap):
        pivot = counterMap[arr[low]]
        i = low ; j = high

        while i < j:

            while i < high and counterMap[arr[i]] >= pivot:  # descending order
                i += 1

            while j > low and counterMap[arr[j]] <= pivot:   # descending order
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]

        return j

    def topKFrequent_Brute(self, nums: list[int], k: int) -> list[int]:
        counterMap = defaultdict(int)      

        # Hashing the elements : frequency in counterMap
        for i in nums:              # O(n)
            counterMap[i] += 1

        # Adding the unique elements to a new list i,e lst
        lst = []
        for key in counterMap:      # O(n)
            lst.append(key)
        
        # Applying Quick Sort on the list elements ... sorting based on the frequency count of unique elements ..(Descending order ..higher frequency first)
        self.quickSort(lst, 0, len(lst) - 1, counterMap)    # O(n log n)

        # Returning the k frquent element
        return lst[0:k]             # O(k)
    

    def topKFrequent_Optimal(self, nums, k):
        counterMap = Counter(nums)  # O(n)

        n = len(nums)
        freqCountLst = [[] for _ in range(0, n + 1)]    # O(n)

        for element, count in counterMap.items():       # O(n)
            freqCountLst[count].append(element)

        resLst = []
        while n and k:  # O(n)
            elements = freqCountLst[n]
            if elements:    # + O(n)
                for element in elements:
                    resLst.append(element)
                    k -= 1
            n -= 1

        return resLst




S = Solution()
nums = [5, 5, 1, 1, 2, 5, 3]; k = 2
# nums = [1]; k = 1
print(S.topKFrequent_Brute(nums, k))
print(S.topKFrequent_Optimal(nums, k))