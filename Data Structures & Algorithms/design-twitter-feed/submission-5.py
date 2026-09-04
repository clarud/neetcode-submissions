from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.timer = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        uids = set(self.following[userId])
        uids.add(userId)

        pool = []
        for uid in uids:
            pool.extend(self.tweets[uid])
        top = heapq.nlargest(10, pool)
        return [x[1] for x in top]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId not in self.following[followerId]:
            return
        self.following[followerId].remove(followeeId)
