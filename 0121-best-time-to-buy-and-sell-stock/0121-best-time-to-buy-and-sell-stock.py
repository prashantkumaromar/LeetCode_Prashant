class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price_so_for = float('inf')
        # max_profit =0
        # for price in prices:
        #     min_price_so_for = min(min_price_so_for, price)   # keep track of min element so for 
        #     # using this 
        #     max_profit = max(max_profit, price- min_price_so_for) 
        # return max_profit

# can also solve by 2 pointer 

        l =0 
        r = 1
        max_profit =0
        for k in range(r, len(prices)):
            if prices[l] < prices[k]:
                max_profit = max(max_profit,prices[k]-prices[l] )
        
            else:
                l =r

            r+=1
        return max_profit





















        # n = len(prices)
        # max_profit1 =0
        # max_profit2 =0
        # prices_sorted = sorted(prices)
        # idx_max_sorted = n-1
        # idx_min_sorted   = 0
        # curr_max_val = prices_sorted[idx_max_sorted]

        # curr_min_val = prices_sorted[idx_min_sorted]

        # ind_max_in_prices = prices.index(curr_max_val)

        # ind_min_in_prices = prices.index(curr_min_val)

        # for i in prices_sorted[::-1]:
        #     if prices.index(i) > ind_min_in_prices:
        #         profit1 = i - curr_min_val
        #         if profit1 > max_profit1:
        #                 max_profit1 = profit1
        # for i in prices_sorted:
        #     if prices.index(i) < ind_max_in_prices:
        #         profit2 = curr_max_val - i
        #         if profit2 > max_profit2:
        #                 max_profit2 = profit2
        # return max(max_profit1, max_profit2)



        
        # while idx_min_sorted < idx_max_sorted:
        #     if ind_max_in_prices  < ind_min_in_prices:
        #         idx_max_sorted -=1
        #         if curr_max_val - curr_min_val > max_profit:
        #             max_profit = curr_max_val - curr_min_val
                
        #     else:
        #         profit = curr_max_val - curr_min_val
        #         if profit > max_profit:
        #             max_profit = profit
        #             idx_min_sorted +=1

        # return max_profit





        # max = prices_sorted[max_index]
        # min = prices_sorted[min_index]
        # for i, val in enumerate(prices):


































 #     # self.prices = prices
    #     left_index =0
    #     right_index =len(prices)-1
    #     max_profit =0
    #     while left_index < right_index:
    #         if prices[left_index] > prices[right_index]:
    #             left_index+=1
    #         else:
    #             profit = prices[right_index]-prices[left_index]
    #             right_index-=1
    #             if profit >max_profit:
    #                 max_profit = profit
    #     return max_profit



