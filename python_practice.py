print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
#How many votes did you get?
my_votes = int(input("How many votes did you get in the election?"))
#Total votes in the eleciton
total_votes = int(input("What is the total votes in the election?"))
#Calculate the percentage of votes you recieved
percentage_votes = (my_votes / total_votes)*100
print("I recieved " + str(percentage_votes)+"% of the total votes.")

