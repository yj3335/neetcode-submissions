class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                time, tweetID = self.tweetMap[followeeId][index]
                minHeap.append([time, tweetID, followeeId, index-1])
        heapq.heapify(minHeap)

        while minHeap and len(res)<10:
            time, tweetID, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetID)
            if index >= 0:
                time, tweetID = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetID, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
