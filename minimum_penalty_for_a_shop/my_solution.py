# https://leetcode.com/problems/minimum-penalty-for-a-shop/
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
         0123
        "YYNY"


        N = len(customers)
        iterate through customers & calculate the amount of penalty if we're closed at time N (which is the number of 'N' we have in customers)
        have 2 variables called min_penalty = N & earliest_time_with_min_penalty = N

        have 1 variable called curr_penalty to save the current penalty as we reversely iterate through customers
        curr_penalty = min_penalty
        iterate reversely from reversed(range(len(customers))). Each time we iterate through a customer, if customer == 'N', we decrement the earliest_time_with_min_penalty and decrement curr_penalty
        else if customer == 'Y':
            curr_penalty += 1

        if curr_penalty <= min_penalty and i < earliest_time_with_min_penalty:
            min_penalty = curr_penalty
            earliest_time_with_min_penalty = i
        """
        N = len(customers)
        min_penalty = N
        earliest_time_with_min_penalty = N
        penalty_if_always_open = 0

        for customer in customers:
            penalty_if_always_open += 1 if customer == 'N' else 0

        min_penalty = penalty_if_always_open

        curr_penalty = min_penalty

        for i in reversed(range(N)):
            customer = customers[i]
            if customer == 'N':
                curr_penalty -= 1
            else:  # customer == 'Y':
                curr_penalty += 1

            if curr_penalty <= min_penalty and i < earliest_time_with_min_penalty:
                min_penalty = curr_penalty
                earliest_time_with_min_penalty = i

        return earliest_time_with_min_penalty
