def manage_stage_changes(changes):
    stack = []
    if not changes:
        return stack
    for item in changes:
            if "Schedule" in item:
                stack.append(item[len(item) - 1])
            elif "Cancel" in item:
                if not stack:
                    continue
                else:
                    cancelled = stack.pop()
            else:
                if stack:
                    stack.append(cancelled)
                else:
                    continue
    return stack

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]))

##########################################

from collections import deque

def process_performance_requests(requests):
    queue = deque()
    group = []
    for request in requests:
        group.append(request[0])
    group.sort(reverse=True)
    print(group)
    ### Loop over numbers in group
    for num in group:
        ### Loop over requests in request list
        for request in requests:
            if num == request[0] and request[1] not in queue:
                queue.append(request[1])
    requests = []
    for item in queue:
        requests.append(item)
    return requests

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(1, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

#################################################

def collect_festival_points(points):
    stack = []
    print(points)
    total = 0
    for point in points:
        stack.append(point)
        total += point
    return total
        
print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 

###################################################

def booth_navigation(clues):
    if not clues:
        return 0
    stack = []
    
    for clue in clues:
        if clue != "back":
            stack.append(clue)
        elif clue == "back" and stack:
            stack.pop()
    return stack

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 

###################################################

## Axel Mejia
## Roy Alcalaque
