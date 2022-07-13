import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')


candidates = []
county = []
ballot_ID = []
totalvotes = []
percentagevotes = []


with open(csvpath) as csvfile:
    
    election_data = csv.reader(csvfile, delimiter=',')

    csv_header = next(election_data)

# appending rows to variables.
    for row in election_data:

        candidates.append(row[2])
          
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
        percentagevotes.append(str(round(counter / len(candidates) * 100, 3)) + "%")
    
        counter = 0


    #create dictionary
    dictionary = {"Candidate": unique_list, "Total Votes": totalvotes, "Percentage Votes": percentagevotes}
 
    #Find who is has the most votes
    mostvotes = 0
    
    #This returns maximum votes
    for element in dictionary["Total Votes"]:  
        
        if element > mostvotes:

            mostvotes = element
 
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

export_file = os.path.join("..","analysis","PyPoll_Results.txt")
with open (export_file, 'w') as txt_file:
    txt_file.write(
    f'Election Results\n'
    f'Election Results\n'
    f'----------------------------\n'
    f'Total Votes: {mostvotes}\n'
    f'----------------------------\n'
    

    f"{dictionary['Candidate'][0]}: {dictionary['Percentage Votes'][0]} ({dictionary['Total Votes'][0]})\n"
    f"{dictionary['Candidate'][1]}: {dictionary['Percentage Votes'][1]} ({dictionary['Total Votes'][1]})\n"
    f"{dictionary['Candidate'][2]}: {dictionary['Percentage Votes'][2]} ({dictionary['Total Votes'][2]})\n"

    f'----------------------------\n'
    f'Winner:  {winner}\n'
    f'----------------------------')









  
        
