# from replit import clear
# HINT: You can call clear() to clear the output in the console.
# from art import logo

# print(logo)


def bid():

    should_end = True
    while not should_end:
        # Ask for name input
        i_name = input("What is the name of the bidder?\n")

        # Ask for Bid price
        i_bid_price = int(input("What is the your bid price? $\n"))

        # Assigning the name and bid of the person in a dictionary
        bidding = {}
        bidding["name"] = i_name
        bidding["bid"] = i_bid_price

        restart = input("Are there any more bidders? Type 'yes' or 'no' \n")
        if restart == 'no':
            should_end = False
            print("The Winner is .......")

        print(bidding)


bid()



print("hello")