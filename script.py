# 2. Saving users' data which we gather by inputs, into a dictionary
# {name : price}
# starting with and empty dictionary
bids = {}


# 5 for checking to see if the bidding should go on or stop
# then we have to use the while loop
continue_bidding = True


# NOTE : we need to declare the funtion before we use it in the while loop
# 7. comparing bids
# since comparison is like a separate piece of functionality, we can define a function
# so we can reuse it
# `bidding_dictionary` is our parameter
# and we are gonna pass our dictionary (`bids = {}`)
def find_highest_bidder(bidding_dictionary):

    winner = ""
    highest_bid = 0

    # 8. looping through the dictionary (`bidding_dictionary`)
    # and look for each bids

    # bidder_name is the key name in the dictionary
    for bidder_name in bidding_dictionary:
        # bid_amount would be the value for each key (bidder_name)
        # value = dictionary_name[key]
        # so our parameter `bidding_dictionary` is supposed to be `bids` dictionary
        # getting the values for each key would basically be : `bids["name"]`
        bid_amount = bidding_dictionary[bidder_name]

        # 9. now we need to figure out what the higher bid amount is
        # we can do this in different ways

        # A :
        # set the initial highest bid to 0 `highest_bid = 0`
        # and every time we loop through a new bid_amount,
        # we can check to see if it's bigger than the current highest bid
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            # now we can check to see who the winner is
            # winner would be the person who currently has the higher amount
            winner = bidder_name

    # now back to the while loop
    print(f"The winner is {winner} with a bid of ${bid_amount}")

    # B :
    # We coulda also use the max() function for this:
    # max(bidding_dictionary)


# 6. using the while loop to check if the bid should keep going or stop
while continue_bidding:

    # 1.Asking the user for some inputs and then storing them in an empty dictionary
    name = input("What is your name?\n").lower()
    price = int(input("What isyour bid? $\n"))

    # 3. assiging the name variable as the key and set the value to price
    bids[name] = price

    # 4. are there any bidders?
    # if thereare more bidders, then the bidding wil continue
    # and if not, then it'll stop the bidding
    # and compare the bids to see who had the higher bids
    should_continue = input("Are there any bidders? Type 'Yes' or 'No'\n").lower()
    if should_continue == "no":
        continue_bidding = False
        # 10.
        find_highest_bidder(bids)
    # 11.
    elif should_continue == "yes":
        # when the user types yes, we dont want to show the prebious name and bid amount,
        # we want to clear the screen insted
        print("\n" * 100)
