def lineup(artists, set_times):
    artistLineup = {
    }
    for i in range(len(artists)):
        artistLineup[artists[i]] = set_times[i]
    return artistLineup

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

##################################################
#2

def get_artist_info(artist__name, schedule):
    if (artist__name in schedule):
        artist_info = schedule[artist__name]
        return artist_info
    else:
        message = {
            "message": "Artist not found"
        }
        return message 


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  

#####################################################
#3
def total_sales(ticket_sales):
    sum = 0
    for key in ticket_sales:
        sum += ticket_sales[key]
    return sum

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

#######################################################
#4
def identify_conflicts(ven1, ven2):
    keys1 = list(ven1.keys())
    keys2 = list(ven2.keys())
    vals1 = list(ven1.values())
    vals2 = list(ven2.values())
    overlap = {
    }
    i = 0
    for word in keys1:
        if word == keys2[i] and vals1[i] == vals2[i]:
            overlap[word] = vals1[i]
            i += 1
        else:
            i += 1
            continue
    return overlap
    
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))

##########################################################
#5
def best_set(votes):
    # Make a empty frequency map
    freq_map = {
    }
    # Iterate through the votes map, if frequency map does not contain the name of an artist already, add them as the key with a value of 1 vote. If they already are in the map, add 1 to their vote count.
    for key in votes:
        if (votes[key] not in freq_map):
            freq_map[votes[key]] = 1
        else:
            freq_map[votes[key]] = freq_map[votes[key]] + 1
            
    # Create a winner variable to save the most votes. Iterate through the frequency map and compare each value of votes with the one stored in winner, if it is larger set winner equal to this value. Also set a variable with the key, or name, of the artist that is associated 
    # with the vote numbers
    winner = 0
    win = ""
    for key in freq_map:
        if (freq_map[key] > winner):
            winner = freq_map[key]
            win = key
        elif freq_map[key] == winner:
            winner = freq_map[key]
            win = key
        else:
            continue
    return win
            
            
    

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))

#############################################
# 7 and 8

def max_audience_performances(audiences):
    max_freq = {}
    for i in range(len(audiences)):
        if (audiences[i] in max_freq):
            max_freq[audiences[i]] += 1
        else:
            max_freq[audiences[i]] = 1
    max = 0
    for key in max_freq:
        if (key > max):
            max = key
        
    max_num = max * max_freq[max]
    return max_num
        
audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

###############################
# 8

def num_popular_pairs(popularity_scores):
    pop_songs = {
    }
    
    for i in range(len(popularity_scores)):
        if (popularity_scores[i] not in pop_songs):
            pop_songs[popularity_scores[i]] = 1
        else:
            pop_songs[popularity_scores[i]] += 1
    
    total_pairs = 0
    for key in pop_songs:
        maximum = pop_songs[key]
        if (maximum >= 2):
            total_pairs += maximum * (maximum - 1) // 2
            
    return total_pairs

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 

################################################
# 9
##### For every performer (character), calculate the absolute difference between their index in 
# s and their index in t. Then, add up all those difference. Loop over the first array, select a name
# then in the second array, loop until you find the name stored from the first array, then
# subtract the index of name in t from the index in s, and get the absolute value. Then add this to
# the total sum.

def find_stage_arrangement_difference(s, t):
    sum_dif = 0
    for i in range(len(s)):
        name = s[i]
        for j in range(len(t)):
            if (t[j] == name):
                sum_dif += abs(j - i) 
    return sum_dif

s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))


##########################################################

def most_endangered(species_list):
    list_pop = {}
    for dict in species_list:
        list_pop[dict['name']] = dict['population']
    x = (min(list_pop.values()))
    keys = [k for k, v in list_pop.items() if v == x]
    return keys
    
species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 65
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

##########################################################
def count_endangered_species(endangered_species, observed_species):
    endangered_species = set(endangered_species)
    count = 0
    speciesDict = {}
    for species in observed_species:
        if species in endangered_species:
            count += 1
            if species in speciesDict:
                speciesDict[species] += 1
            else:
                speciesDict[species] = 1
        else:
            continue
    return speciesDict

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))

######################################################################

def navigate_research_station(station_layout, observations):
    # Step 1: Create a dictionary that maps each observation point (character)
    # to its index in the station layout
    my_dict = {}
    for index, char in enumerate(station_layout):
        my_dict[char] = index

    # Step 2: Initialize total time and the current index (starting at index 0)
    total_sum = 0
    index = 0

    # Step 3: Loop through each observation point in the order given
    for char in observations:
        if char in my_dict:
            # Add the time it takes to move from current location to the target observation point
            total_sum += abs(index - my_dict[char])
            # Update current index to new location
            index = my_dict[char]

    # Step 4: Return the total time after completing all movements
    return total_sum

# Test Case 1: Custom station layout with a word
station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

# Test Case 2: Reversed observation order in a standard alphabet layout
station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

# Print results
print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

#############################################################################

def prioritize_observations(observed_species, priority_species):
    final_list = []
    non_prio = []
    prio_list = []
    # loop over observed species and split them into 2 lists, priority and non-priority
    for item in observed_species:
        if item in priority_species:
            prio_list.append(item)
        else:
            non_prio.append(item)
       
    # Make a second loop, that loops over priority species.  
    for species in priority_species:
        # Loop over your seperated list of priority species and add them to final list.
        for item in prio_list:
            if (item == species):
                final_list.append(item)
    # sort the non-prio list and add it to the final list
    non_prio.sort()
    final_list.extend(non_prio)
    return final_list

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2))

