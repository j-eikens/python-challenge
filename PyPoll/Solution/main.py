import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

candidates = []
county = []
ballot_ID = []

secondrow = []

with open(csvpath) as csvfile:
    
    election_data = csv.reader(csvfile, delimiter=',')

    csv_header = next(election_data)

#----------------------------------------------------------------------
    #unique value function - this will print all result three times
    # def unique1(list):
        
    #     unique_candidates = []
            
    #     for candidate in candidates:

    #         if candidate not in unique_candidates:
    #             unique_candidates.append(candidate)
        
    #     for candidate in unique_candidates:
    #         print(unique_candidates)

#----------------------------------------------------------------------
    # def unique1(list1):

    #     list_set = set(list1)

    #     unique_list = (list(list_set))

    #     print(unique_list)

    #     return unique_list

#----------------------------------------------------------------------
# appending rows to variables. This works.

    for row in election_data:

        candidates.append(row[2])
        county.append(row[1])
        ballot_ID.append(row[0])

        # if candidates == str(unique_list[0]):
        #     total += row
        #     print (total)

#---------------------------------------------------------------------

    #find unique candidates
    list_set = set(candidates)

    unique_list = (list(list_set))

    print(unique_list)
#-------------------------------------------------------------------------
#trying to count votes for candidates (not working)
    # total = 0  

    # for row in election_data:

    #     total = 0

    #     if candidates == str(unique_list[0]):
    #         total += row  
    #         print (total)
    # print(total)

#------------------------------------------------------------------------  
#total votes - this works
  
    # number of ballots cast
    print(len(ballot_ID))

#------------------------------------------------------------------------
#this will count all the times Diana is input. Can I feed a list into the input???

    # #returns number of times
    # from collections import Counter

    # list = candidates

    # x = "Diana DeGette"
    # d = Counter(list)

    # print('{} has occured {}times'.format(x, d[x]))




  
        
