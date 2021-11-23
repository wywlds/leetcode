from typing import List

import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell_q = []
        buy_q = []
        for price, quantity, is_sell in orders:
            if not is_sell:
                while len(sell_q) != 0 and sell_q[0][0] <= price and quantity > 0:
                    _, sell_quantity = sell_q[0]
                    if sell_quantity > quantity:
                        sell_q[0][1] -= quantity
                        quantity = 0
                    else:
                        heapq.heappop(sell_q)
                        quantity -= sell_quantity
                if quantity != 0:
                    heapq.heappush(buy_q, [-price, quantity])
            else:
                while len(buy_q) != 0 and - buy_q[0][0] >= price and quantity > 0:
                    _, buy_quantity = buy_q[0]
                    if buy_quantity > quantity:
                        buy_q[0][1] -= quantity
                        quantity = 0
                    else:
                        heapq.heappop(buy_q)
                        quantity -= buy_quantity
                if quantity != 0:
                    heapq.heappush(sell_q, [price, quantity])
        BASE = 10 ** 9 + 7
        return sum([it[1] for it in sell_q]) + sum([it[1] for it in buy_q]) % BASE


if __name__=="__main__":
    orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
    solution = Solution()
    print(solution.getNumberOfBacklogOrders(orders))