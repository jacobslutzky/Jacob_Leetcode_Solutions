class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue = []
        for i in deck:
            if queue:
                queue.insert(0,queue.pop(-1))
            queue.insert(0,i)
        return queue