"""Functions for generating random euromillions numbers

tickets will be generated to ensure that all numbers are
used and numbers are not used again until all other options
have been used.
"""
from pathlib import Path
from datetime import datetime
import argparse
import sys

from libs import gen_tickets
from utils.file import loop_mk_dir

def get_dir_path(folder):
    cur_path = Path(__file__).parent
    dir_path = cur_path / folder
    return dir_path

def create_tickets(num_tickets, folder="out", filename=f"tickets", seed=None):
    tickets = gen_tickets(num_tickets, seed=seed)
    #output
    date = datetime.strftime(datetime.today(), "%Y%m%d")
    #Get the dir path
    folder_path = get_dir_path(folder)
    #Make the dir
    loop_mk_dir(str(folder_path))
    tickets.to_csv(Path(folder) / f"{filename}-{date}.csv", index=False)
    print(f"{num_tickets} tickets generated")

if __name__ == "__main__":
    #Get the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', default="", help="Save location of output")
    parser.add_argument('-fn', '--filename', default="tickets", help="The name of the file to be output")
    parser.add_argument('-n', '--number', default=1, help="The number of tickets to generate")
    parser.add_argument('-s', '--seed', default=None, help="The random seed to be used for number generation")
    args = parser.parse_args()
    seed = None if args.seed == 0 else args.seed
    create_tickets(int(args.number), folder=args.folder, filename=args.filename, seed=seed)