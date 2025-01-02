'''You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.'''
# TC: O(nlogn), SC: O(n)
from sortedcontainers import SortedDict

class StockPrice:
    def __init__(self):
        self.latest_time = 0
        # Store price of each stock at each timestamp.
        self.timestamp_price_map = {}
        # Store stock prices in increasing order to get min and max price.
        self.price_frequency = SortedDict()
        
    def update(self, timestamp: int, price: int) -> None:
        # Update latest_time to latest timestamp.
        self.latest_time = max(self.latest_time, timestamp)
        
        # If same timestamp occurs again, previous price was wrong. 
        if timestamp in self.timestamp_price_map:
            # Remove previous price.
            old_price = self.timestamp_price_map[timestamp]
            self.price_frequency[old_price] -= 1
            
            # Remove the entry from the sorted-dictionary.
            if not self.price_frequency[old_price]:
                del self.price_frequency[old_price]
        
        # Add latest price for timestamp.
        self.timestamp_price_map[timestamp] = price
        
        if price in self.price_frequency:
            self.price_frequency[price] += 1
        else:
            self.price_frequency[price] = 1

    def current(self) -> int:
        # Return latest price of the stock.
        return self.timestamp_price_map[self.latest_time]
        
    def maximum(self) -> int:
        # Return the maximum price stored at the end of sorted-dictionary.
        return self.price_frequency.peekitem(-1)[0]
        
    def minimum(self) -> int:
        # Return the maximum price stored at the front of sorted-dictionary.
        return self.price_frequency.peekitem(0)[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
