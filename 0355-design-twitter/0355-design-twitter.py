import heapq
class Twitter:

    def __init__(self):
        self.tweets_by_users = {}
        self.following = {}
        self.tweetCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets_by_users:
            self.tweets_by_users[userId].insert(0,(self.tweetCount, tweetId))
        else:
            self.tweets_by_users[userId] = [(self.tweetCount, tweetId)]

        self.tweetCount-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.tweets_by_users:
            tweets = self.tweets_by_users[userId].copy()
        else:
            tweets = []
        heapq.heapify(tweets)
        output = []
        if userId in self.following:
            for following in self.following[userId]:
                if following in self.tweets_by_users:
                    for i in range(min(10,len(self.tweets_by_users[following]))):
                        tweetCount, tweetId = self.tweets_by_users[following][i]
                        heapq.heappush(tweets, (tweetCount,tweetId))
            
        for i in range(10):
            if not tweets:
                break
            output.append(heapq.heappop(tweets)[1])
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)