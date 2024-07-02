from itertools import product

excluded_suit = input().strip()
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(excluded_suit)

for rank, suit in product(ranks, suits):
    print(f"{rank} {suit}")
