def average_price(arr):
    if len(arr)==0: return 0
    return sum(arr)/len(arr)

def find_element(arr, element):
    for i in range(0, len(arr)):
        if element==arr[i]:
            return i
    return -1

def largest_digit(num):
    c_num = [int(i) for i in str(num)]
    c_num.sort(reverse=True)
    output = int(''.join([str(i) for i in c_num])) 
    return output

def smallest_digit(num):
    odds = [i for i in str(num) if int(i)%2==1]
    nums = [int(i) for i in odds]
    nums.sort()
    output = int(''.join([str(i) for i in nums]))
    return output

from dataclasses import dataclass

@dataclass
class Meeting:
    start_time: int
    end_time: int
    num_people: int

def max_people_in_meetings(meetings):
    curr_total, max_total = 0, 0
    events = []
    for meeting in meetings:
        events.append((meeting.start_time, meeting.num_people))
        events.append((meeting.end_time, -meeting.num_people))
    
    events.sort(key=lambda x:(x[0],-x[1]))
    
    for e in events:
        #(1,10)
        curr_total += e[1]
        max_total = max(max_total, curr_total)
    
    return max_total

meetings = [
    Meeting(1, 5, 10),
    Meeting(2, 6, 5),
    Meeting(4, 8, 12),
    Meeting(7, 10, 8),
]

def max_overlapping_meetings(meetings):
    curr_overlap, max_overlap = 0, 0
    events = []

    for meet in meetings:
        start, end = meet[0], meet[1]
        events.append((start, 1))
        events.append((end, -1))
    events.sort(key=lambda x:(x[0],-x[1]))

    for e in events:
        curr_overlap += e[1]
        max_overlap = max(max_overlap, curr_overlap)

    return max_overlap

overlap_meetings = [
    (1, 4),
    (2, 5),
    (9, 12),
    (5, 9),
    (5, 12)
]

def max_classes_in_two_consecutive_years(classes):
    counts = {}
    for year in classes:
        counts[year] = counts.get(year,0)+1
    scounts = sorted(counts.items(), key=lambda x:x[0])
    max_classes = 0
    curr_classes = 0
    print(scounts)
    for i in range(1,len(scounts)):
        if scounts[i][0] == scounts[i-1][0] + 1:
            curr_classes = scounts[i][1] + scounts[i-1][1]
            max_classes = max(max_classes, curr_classes)

    return max_classes

workshops = [2020, 2020, 2021, 2021, 2021, 2022, 2024, 2025, 2025]

def validIP(addr):
    # 0-255, 4 numbers separated by dots
    pfx = addr.split(".")
    if len(pfx)!=4:
        return False
    for item in pfx:
        item = int(item)
        if item < 0 or item > 255:
            return False

    return True

def max_classes_in_consecutive_years(workshops):
    d = {}
    for year in workshops:
        d[year] = d.get(year,0) + 1
    d = sorted(d.items(), key=lambda x:x[0])

    curr = max_classes = 0
    for i in range(len(d)):
        if i!=0 and d[i][0] != d[i-1][0] + 1: # reset
            curr = 0
        curr += d[i][1]
        max_classes = max(max_classes, curr)

    return max_classes

workshops = [2020, 2020, 2021, 2021, 2021, 2022, 2024, 2025, 2025, 2026, 2026, 2027, 2028]

def max_points_3_books(arr):
    hmap = {}
    for item in arr:
        book, points = item
        hmap[book] = max(hmap.get(book,0), points)
    s_map = sorted(hmap.values(), reverse=True)
    output = sum(s_map[:3]) 
    return output


# Example
books = [
    ("Math", 90),
    ("Science", 80),
    ("Literature", 85),
    ("Math", 75),
    ("Science", 95),
    ("Art", 70),
    ("Literature", 60)
]

