class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i]<=price:
                span+=1
            else:
                break
        self.stack.append(price)
        return span
    

        