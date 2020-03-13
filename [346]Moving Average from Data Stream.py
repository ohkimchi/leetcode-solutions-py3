# Given a stream of integers and a window size, calculate the moving average
# of all integers in the sliding window.
#
# Example: 
#
# 
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
# 
#
# 
# Related Topics Design Queue


# leetcode submit region begin(Prohibit modification and deletion)
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])
        return window_sum / (min(len(queue), size))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# leetcode submit region end(Prohibit modification and deletion)
