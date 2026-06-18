#Problem 1
"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
# No starter code is provided for this problem
# Add your code here
flights = {
    "JFK" : ["LAX", "DFW"],
    "DFW" : ["JFK", "ATL"],
    "LAX" : ["JFK"]
}
print()
print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])

#Problem 2
def bidirectional_flights(flights):
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))