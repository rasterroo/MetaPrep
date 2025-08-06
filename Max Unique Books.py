# Determine the maximum number of unique books that can be bought, given an array of book prices and a budget (each book can be purchased only once)
def max_unique_books(arr, budget):
    arr.sort()
    num_books = 0
 
    for cost in arr:
        if budget-cost<0: break
        num_books+=1
        budget -= cost

    return num_books
