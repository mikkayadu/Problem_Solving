class WordCount:
    def __init__(self, val, word):
        self.word=word
        self.val = val
    def __lt__(self, other):
        if self.val != other.val:
            return self.val > other.val
        return self.word < other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = []
        

        for word in count:
            heappush(heap, WordCount(count[word], word))
            
        print(heap)

        ans = []
        for _ in range(k):
            ans.append(heappop(heap).word)
        
        return ans
        