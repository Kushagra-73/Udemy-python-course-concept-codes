
def max_bid(bidding_dict):
    
    # METHOD 1 - USING max(dict_name ,key=dict_name.get)
    
    highest_bidder=max(bid_data ,key=bid_data.get)
    bid_amt=bid_data[highest_bidder]
    print(f"The winner is {highest_bidder} with bidding amount {bid_amt}")
    

    # METHOD 2 - Using loop 

    # highest_bid=0
    # for bidder in bidding_dict:
    #     bid_amount=bidding_dict[bidder]
    #     if bid_amount>highest_bid:
    #         highest_bid=bid_amount
    #         winner=bidder

    # print(f"the winner is {winner} with bid amount ${highest_bid}")
    


bid_data = {}

new_bid=True
while new_bid:
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n$"))
    new=input("Are there any other bidders? 'yes' or 'no' :").lower()
    
    
    bid_data[name]=bid


    if new=="yes":
        print("\n" * 100)
    
        

    else :
        max_bid(bid_data)
        new_bid=False


    
    

   
