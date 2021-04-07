import heapq


class Element:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, e2):
        # Compares by count and then by reverse alphabetical order
        if self.count == e2.count:
            return self.word > e2.word
        return self.count < e2.count


class Solution:
    def topKFrequent(self, words, k: int):
        wordFreq = {}

        # Obtain frequency of each word
        for w in words:
            wordFreq[w] = wordFreq.get(w, 0) + 1

        freqHeap = []  # Heap used to determine order of different possible frequencies
        minValue = -1  # Used to avoid unnecessary pushes to heap

        # Go through word, frequency pairs
        for w, freq in wordFreq.items():
            element = Element(w, freq)

            # Add first k elements
            if len(freqHeap) < k:
                heapq.heappush(freqHeap, element)
            elif freq >= minValue:
                # Then if there's a larger frequency, add it to the heap
                heapq.heappushpop(freqHeap, element)

            minValue = freqHeap[0].count

        # Initialize list of size k
        kFreqWords = [None] * k

        # Fill out kFreqWords
        for i in range(k - 1, -1, -1):
            element = heapq.heappop(freqHeap)
            kFreqWords[i] = element.word

        return kFreqWords
