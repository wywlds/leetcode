from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.needs_map = {}
        return self.shoppingOffers_internal(price, special, needs)

    def shoppingOffers_internal(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        if str(needs) in self.needs_map:
            return self.needs_map[str(needs)]
        best_price = self.dot(price, needs)
        for special_offer in special:
            special_price = special_offer[-1]
            new_needs = []
            for i, offer_c in enumerate(special_offer[:-1]):
                if needs[i] - offer_c >= 0:
                    new_needs.append(needs[i] - offer_c)
                else:
                    break
            if len(new_needs) == len(price):
                best_price = min(best_price, special_price + self.shoppingOffers_internal(price, special, new_needs))
        self.needs_map[str(needs)] = best_price
        return best_price

    def dot(self, price, needs):
        return sum([price_i * need_i for price_i, need_i in zip(price, needs)])

if __name__=="__main__":
    price = [1, 1, 1]
    special = [[1, 1, 0, 0], [2, 2, 1, 0]]
    needs = [1, 1, 1]
    solution = Solution()
    print(solution.shoppingOffers(price, special, needs))