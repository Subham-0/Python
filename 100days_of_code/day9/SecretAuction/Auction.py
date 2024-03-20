from logo import logo_of_order
print(logo_of_order)
print("Welcome to the secret auction program")
secret_auction = {}


def highest_bid(auction):
    winner = max(auction, key=auction.get)
    max_bid = auction[winner]
    print(f"The winner is {winner} with a bid of {max_bid}") 
    
    #or  

# def highest_bid(auction):
#     highest_bid_amount = 0   
#     winner = "" 
#     for bidder in auction:
#         bid_amount = auction[bidder]
#         if bid_amount > highest_bid_amount:
#             highest_bid_amount = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of {highest_bid_amount}")  
      
while True:
    
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    secret_auction[name] = bid
    dis = input("Are there any other bider? type yes or no")
    if dis == "no":
        highest_bid(secret_auction)
        break


    