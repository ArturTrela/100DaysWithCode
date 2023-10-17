from replit import clear
from ASCIIart import logo

# HINT: You can call clear() to clear the output in the console.


bidders = {

}
more_player = True


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = bidders
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        winner = bidder
    print(f'And the Winner is {bidder} and pay $ {bid_amount}')


while more_player:
    print(logo)
    name = input('What is your name ? : \n')
    bid = input("What's your bid ? \n $")
    clear_view = input("Is any more bidder? y/n ").lower()
    bidders[name] = bid

    if clear_view == 'y':
        clear()

    else:
        more_player = False
        find_highest_bid(bidders)
    # TO-DO poprawić wyświetlanie osoby która ma najwyższy wynik bo aktualnie wyświetla ostatni rekord który był wpisany