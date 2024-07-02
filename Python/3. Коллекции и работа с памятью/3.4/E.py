mom_wishlist = input().strip().split(", ")
dad_wishlist = input().strip().split(", ")
daughter_wishlist = input().strip().split(", ")

combined_list = sorted(mom_wishlist + dad_wishlist + daughter_wishlist)

for idx, item in enumerate(combined_list, start=1):
    print(f"{idx}. {item}")
