from numpy import random, around, array, unique
from pandas import DataFrame

#Generate a random number
def gen_num(poss_nums, excl_nums=[]):
    """Function to select a number given limits
    and numbers to exclude"""
    intersect = set(poss_nums).intersection(excl_nums)
    if len(intersect) == len(poss_nums):
        print(poss_nums)
        print(excl_nums)
        raise ValueError("all possible numbers have been used")
    diff = max(poss_nums) - min(poss_nums)
    rand_num = around(random.rand() * diff + min(poss_nums))
    if rand_num in excl_nums \
        or rand_num not in poss_nums:
        rand_num = gen_num(poss_nums, excl_nums)
    return rand_num

def update_excl_nums(new_num, poss_nums, excl_nums):
    """Function to update the exclusion list
    
    args:
    ----
    new_num - int - the number selected
    poss_nums - list - the selection of numbers to choose from
    excl_nums - list - number sot be excluded form the selection

    returns:
    ----
    list
    """
    #Append the new number
    excl_nums.append(new_num)
    #Calc the intersection between possible numbers and excluded numbers
    intersect = set(poss_nums).intersection(excl_nums)
    if len(intersect) == len(poss_nums):
        #reset the excl nums
        excl_nums = []
    return excl_nums

def gen_nums(nums, poss_nums, excl_nums=[]):
    """Function to generate the number for a ticket
    
    args:
    ----
    nums - int - the number of numbers to put on a ticket
    poss_nums - list - the selection of numbers to choose from
    excl_nums - list - number sot be excluded form the selection

    returns:
    ----
    list, list
    """
    out_nums = []
    for _ in range(nums):
        #generate the new number
        new_num = gen_num(poss_nums=poss_nums, excl_nums=excl_nums)
        #update to the excl_nums
        excl_nums = update_excl_nums(new_num, poss_nums, excl_nums)
        #append to nums
        out_nums.append(new_num)
    return out_nums, excl_nums

def count_nums(nums):
    """Count the number of items in a numpy array"""
    #flatten
    nums = array(nums).flatten()
    #count
    vals, counts = unique(nums, return_counts=True)
    return dict(zip(vals, counts))

def gen_tickets(num_tickets, seed=None):
    """Function for generating multiple tickets"""
    #Set the random seed
    if seed is not None:
        random.seed(int(seed))
    #Create range of possible numbers
    main_poss_nums = array(range(50)) + 1
    star_poss_nums = array(range(12)) + 1
    #Create list for excluded numbers
    main_excl_nums = []
    star_excl_nums = []
    #Create holder for all tickets
    tickets = []
    for _ in range(num_tickets):
        main, main_excl_nums = gen_nums(5, main_poss_nums, main_excl_nums)
        stars, star_excl_nums = gen_nums(2, star_poss_nums, star_excl_nums)
        #Sort the values
        main = sorted(main)
        stars = sorted(stars)
        #update datatypes
        main = [int(v) for v in main]
        stars = [int(v) for v in stars]
        #Append to the tickets object
        tickets.append([main, stars])
    #count all main numbers
    main_counts = count_nums([v[0] for v in tickets])
    #print them
    print("key-count")
    print("---------")
    _ = [print(f"{k}-{v}") for k,v in main_counts.items()]
    #count all main numbers
    star_counts = count_nums([v[1] for v in tickets])
    #print them
    print("key-count")
    print("---------")
    _ = [print(f"{k}-{v}") for k,v in star_counts.items()]
    #convert to dataframe
    tickets = DataFrame(tickets, columns=["main","stars"])
    return tickets
