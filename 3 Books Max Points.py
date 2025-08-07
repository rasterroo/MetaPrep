from collections import defaultdict
from itertools import combinations

def max_points(arr):
    hmap = dict()
    for book in arr:
        subject, val = book
        hmap[subject] = max(hmap.get(subject,0), val)
    sort_hmap = sorted(hmap.items(), key=lambda x:x[1], reverse=True)
    max_points = sum([val for key,val in sort_hmap[:3]])
    return max_points

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

print(max_points(books))  # Output: 270 (95 from Science, 90 from Math, 85 from Literature)
