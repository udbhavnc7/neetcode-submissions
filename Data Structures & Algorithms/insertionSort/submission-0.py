from typing import List

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []

        for i in range(len(pairs)):
            key = pairs[i]
            j = i - 1

            while j >= 0 and pairs[j].key > key.key:
                pairs[j + 1] = pairs[j]
                j -= 1

            pairs[j + 1] = key
            states.append(pairs.copy())

        return states