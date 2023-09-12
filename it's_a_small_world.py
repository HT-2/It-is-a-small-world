# IT'S A SMALL WORLD
# Project Solution by:- Meet Turakhia, Hetal Tiwari, Devansh Sharma


n = int(input("Enter the number of casts: ")) # taking the input n which represents the number of casts
casts = [] # list of all the n cast

# for loop to get the casts from the user alternatively we can take input from a text file
# Note:- We are storing the casts as a list of n sets, it is important that all casts are stored as sets so that we can use the set properties and get our output
# in O(N) Time Complexity
for i in range(n):
    casts.append(set(input(f"Enter the cast of Movie {i + 1} (Names should be comma seperated): ").split(", ")))

# Checking for shortest connection 1
# Logic used:- if set1 = {'a', 'b', 'c'} is one set of actors and set2 = {'c', 'd', 'e'} is the other set than set1 - set2 = {'a', 'b'} and 
# hence, the length of set1 - set2 < length set 1 and with that we can check for shortest connection 1 in this case i.e. 'c'.

if(len(casts[0] - casts[1]) < len(casts[0])):
    print(f'Shortest Connection is {1}, actor = "{casts[0] - (casts[0] - casts[1])}"')
    exit(0)

# checking for connection 2 
# Logic used:- if length of set1 - set2 is not less than set1 meaning if no common element in the sets, we will iterate over the other sets and check
# if length of set1 - seti is less than length of set1 and if it is less meaning something is common in between them than we will check if same is true 
# for length of set2 - seti is less than length of set2, if yes than we have a shortest connection of 2 at cast i 
# else shortest connection is more than 2 or no connection.
for i in range(2, n):
    if(len(casts[0] - casts[i]) < len(casts[0])):
        tempCast = casts[i]
        if(len(casts[1] - tempCast) < len(casts[1])):
            print(f'Shortest Connection is {2}, cast = {tempCast}')
            exit(0)
else:
    print("Shortest Connection > 2 or No Connection")
    exit(0)

# Final Results & Evaluation :-
# Time Complexity:- O(N)
# Space Complexity:- O(N) / O(1) Depending on Condition.


    