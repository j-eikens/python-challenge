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
        county.append(row[1])
        ballot_ID.append(row[0])

          
    #find unique candidates
    list_set = set(candidates)

    unique_list = (list(list_set))


    #search for 
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

    print(dictionary)  
    print("---------------------")
    
    # print(len(dictionary["Total Votes"]))

    #Find who is has the most votes
    mostvotes = 0
    
    for element in range(len(dictionary["Total Votes"])):  
        
        #print(element)

        if element > mostvotes:

            mostvotes = element
            #print(element)


    # for element in dictionary["Total Votes"]:  
        
    #     print(element)

    #     if element > mostvotes:

    #         mostvotes = element

    print('----------')  
    print(element)      
    print(mostvotes)








  
        
