# Last updated: 1/2/2026, 12:17:52 PM
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count frequencies
        freq = Counter(words)  # O(n)

        # Step 2: Sort by (-frequency, word) -> O(n log n)
        sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        # Step 3: Extract top k words
        return [word for word, count in sorted_words[:k]]  # O(k)
