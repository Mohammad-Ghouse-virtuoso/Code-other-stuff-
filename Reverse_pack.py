# Input reading
n = int(input())
arr = list(map(int, input().strip()))

# Count the frequency of each unique number
freq_dict = {}
for num in arr:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

# Create the new list based on the frequency counts
new_list = []
for num, freq in freq_dict.items():
    new_list.extend([freq] * num)

# Sort the new list
new_list.sort()

# Output the sorted new list
print(new_list)


#Test cases 5 are working!!
