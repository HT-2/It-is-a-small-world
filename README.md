# It-is-a-small-world

Problem Statement:
In this project you will design and implement one algorithm related to strings. You will design
the algorithm, describe the algorithm using clear pseudocode, and implement it using
C/C++/C#/Java/Python, compile, test it, and submit BOTH the report (as a PDF file) and the
files. The execution should take less than one hour for each input example.
We assume that the name of each actor is a string, thus a cast is a set of strings, ordered in
alphabetical order. But it does not matter whether they are listed alphabetically or not, but for
simplicity, let’s list them in alphabetical order.
The input will be a positive integer n > 2, and a list of n casts from which the first two sets are
more significant, CAST[0] and CAST[1]. If the two casts CAST[0] and CAST[1] have at least
one string in common, then the shortest connection is 1. If the two casts CAST[0] and CAST[1]
do not have any string in common, then look for another cast in the list of n casts, let’s called it
tempCast, such that CAST[0] and tempCast have a string in common, and CAST[1] and
tempCast have a string common, then the shortest connection is 2. Else the shortest connection is
greater than 2 or there is no connection.

Summary:
1. Take the input n which represents the number of casts.
2. For loop to get the casts from the user alternatively we can took input from a text file
3. We are storing the casts as a list of n sets, it is important that all casts are stored as sets so
that we can use the set properties and get our output
4. Checking for shortest connection 1
5. If set1 = {'a', 'b', 'c'} is one set of actors and set2 = {'c', 'd', 'e'} is the other set than set1 -
set2 = {'a', 'b'} and
6. Hence, the length of set1 - set2 < length set 1 and with that we can check for shortest
connection 1 in this case i.e. 'c'.
7. Checking for connection 2
8. If length of set1 - set2 is not less than set1 meaning if no common element in the sets, we
will iterate over the other sets and check
9. if length of set1 - seti is less than length of set1 and if it is less meaning something is
common in between them than we will check if same is true
10. For length of set2 - seti is less than length of set2, if yes than we have a shortest
connection of 2 at cast i
11. Else shortest connection is more than 2 or no connection.

Solution:
Pseudocode:
\\\n = int(input("Enter the number of casts: "))
casts = []
for i in range(n):
casts.append(set(input(f"Enter the cast of Movie {i + 1} (Names should be comma seperated):
").split(", ")))
if(len(casts[0] - casts[1]) < len(casts[0])):
print(f'Shortest Connection is {1}, actor = "{casts[0] - (casts[0] - casts[1])}"')
exit(0)
for i in range(2, n):
if(len(casts[0] - casts[i]) < len(casts[0])):
tempCast = casts[i]
if(len(casts[1] - tempCast) < len(casts[1])):
print(f'Shortest Connection is {2}, cast = {tempCast}')
exit(0)
else:
print("Shortest Connection > 2 or No Connection")
exit(0)\\\

Time Complexity:- O(N)
Space Complexity:- O(N) / O(1) Depending on condition.
Input example 1: Shortest Connection 1
Input example 2: Shortest Connection 2
Input example 3: Shortest Connection >2 or No Connection
