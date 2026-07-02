class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # userId -> list[tweetId]
        self.follows = defaultdict(set) # followerId -> list[followee]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = set(self.follows[userId])
        users.add(userId)

        for user in users:
            for time, tweetId in self.tweets[user]:
                heapq.heappush(heap, (-time, tweetId))

        res = []
        while heap and len(res) < 10:
            _, tweetId = heapq.heappop(heap)
            res.append(tweetId)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
