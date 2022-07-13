import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#variables for approach 1
candidates = []
county = []
ballot_ID = []

totalvotes = []
percentagevotes = []

# #variables for approach 2
# candidates = []
# county = []
# ballot_ID = []

# total_vote = []
# percent_vote = []

# unique_candidates = []


with open(csvpath) as csvfile:
    
    election_data = csv.reader(csvfile, delimiter=',')

    csv_header = next(election_data)


#--------------------------------------------------------------------------
#approach 2

#     votes = 0

#     for row in election_data:

#         votes += 1

#         candidates.append(row[2])
#         county.append(row[1])
#         ballot_ID.append(row[0])

#     #find unique candidates
#     for candidate in candidates:
        
#         if candidate not in unique_candidates:
            
#             unique_candidates.append(candidate)

    
#     resultsdictionary = (unique_candidates)

#     print(resultsdictionary)
    


#     # count = 1
#     # #count votes for each candidate
#     # for candidate in unique_candidates:

#     #     if unique_candidates.value == candidates:

#     #         count += 1

#     # print(unique_candidates)
#     # print(count)



# #Results
# print('Election Results')
# print('------------------------')
# print(f'Total Votes: {votes}')

#-------------------------------------------------------------------------



# approach 1 - more complex???

# appending rows to variables.
    for row in election_data:

        candidates.append(row[2])
        county.append(row[1])
        ballot_ID.append(row[0])

          
    #find unique candidates
    list_set = set(candidates)

    unique_list = (list(list_set))


    #find instances of unique candidates - BSC claims there is an easier way 
    counter = 0

    for row in unique_list: 

        for candidate in candidates:

            if candidate == row:

                counter += 1

        totalvotes.append(counter)
        percentagevotes.append(str(round(counter / len(ballot_ID) * 100, 3)) + "%")
    
        counter = 0


    #create dictionary
    dictionary = {"Candidate": unique_list, "Total Votes": totalvotes, "Percentage Votes": percentagevotes}

    #trying to create different dictionary
    dictionary2 = {"Charles Casper Stockham:": totalvotes[1], "Total Votes" : totalvotes}

 
    #Find who is has the most votes
    mostvotes = 0
    
    #This returns maximum votes
    for element in dictionary["Total Votes"]:  
        
        #print(element)

        if element > mostvotes:

            mostvotes = element
            #print(mostvotes)


    #Finds winner
    index = totalvotes.index(mostvotes)

    winner = unique_list[index]

    print('Election Results')
    print('----------------------------')
    print(f'Total Votes: {mostvotes}')
    print('----------------------------')
    
    for i in range(3):
        print(f"{dictionary['Candidate'][i]}: {dictionary['Percentage Votes'][i]} ({dictionary['Total Votes'][i]})")

    print('----------------------------')
    print(f'Winner:  {winner}')
    print('----------------------------')

    # for key, value in dictionary.items():
    #     print(key, ":", value)

    #print(dictionary2)










  
        
