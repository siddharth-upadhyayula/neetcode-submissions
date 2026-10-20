class StockSpanner:

    def __init__(self):
        self.StockSpanner = []

    def next(self, price: int) -> int:
        count = 1
        while self.StockSpanner and self.StockSpanner[-1][0] <= price:
            count += self.StockSpanner.pop()[1]
        self.StockSpanner.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)