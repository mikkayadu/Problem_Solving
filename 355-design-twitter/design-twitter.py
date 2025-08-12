class Twitter:

    def __init__(self):
        self.MAXTIMESTAMP = 10
        self.following = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.timestamp = 0        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        self.timestamp += 1

        if len(self.tweets) > self.MAXTIMESTAMP:
            self.tweets[userId].pop()
        

    def getNewsFeed(self, userId: int) -> List[int]:
        relevant_users = self.following[userId] | {userId}
        heap = []
        for user in relevant_users:
            if self.tweets[user]:
                timestamp, tweetId = self.tweets[user][0]
                heappush(heap, (-timestamp, tweetId, user, 0))
        
        news_feed = []
        while heap and len(news_feed) < 10:
            timestamp, tweetId, user, tweet_index = heappop(heap)
            news_feed.append(tweetId)

            if tweet_index + 1 < len(self.tweets[user]):
                timestamp, tweetId = self.tweets[user][tweet_index +1]
                heappush(heap, (-timestamp, tweetId, user, tweet_index+1))
        
        return news_feed



    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)