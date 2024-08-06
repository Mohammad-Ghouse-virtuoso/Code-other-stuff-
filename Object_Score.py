N, M = map(int, input().split())
capacities = list(map(int, input().split()))

items = []
for _ in range(M):
    price, weight = map(int, input().split())
    items.append((price, weight))

# Sort items by price to allow early termination during processing
items.sort()

# Process each family member's capacity
for capacity in capacities:
    max_weight = 0
    for price, weight in items:
        if price > capacity:
            break  # Early termination as further items can't be bought
        max_weight += weight
    print(max_weight)
#1/5 - test cases passed!
