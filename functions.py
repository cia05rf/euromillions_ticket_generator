"""Functions for generating random euromillions numbers

tickets will be generated to ensure that all numbers are
used and numbers are not used again until all other options
have been used.
"""
from pathlib import Path
from datetime import datetime

from libs import gen_tickets

def create_tickets(num_tickets):
    tickets = gen_tickets(num_tickets)
    #output
    date = datetime.strftime(datetime.today(), "%Y%m%d")
    tickets.to_csv(Path(f"out/tickets{date}.csv"), index=False)

if __name__ == "__main__":
    create_tickets(78)