logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the Silent Auction!")

bids = {}

keep_going = True
while keep_going is True:
    bid_name = (input("What is your name? "))
    bid_price = int(input("What is your bid? $"))
    bids[bid_name] = bid_price

    highest_bidder = max(bids, key = bids.get)
    highest_price = bids[highest_bidder]

    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if other_bidder == 'no':
        keep_going = False
        print(f"The winner is {highest_bidder} with a bid of ${highest_price}.")
    else:
        keep_going = True
