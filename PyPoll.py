# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize variables.
total_votes = 0
candidate_options = []
candidate_votes = {}

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that cadidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary.
print(candidate_votes)

# Print the candidate list.
#print(candidate_options)


# 3. Print the total votes.
#print(total_votes)

