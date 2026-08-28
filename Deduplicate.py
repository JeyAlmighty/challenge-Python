# Deduplikasi

nums = [1, 2, 2, 3, 3, 4]

# Output:
# [1, 2, 3, 4]
unique_ordered = []
for i in nums:
    if i not in unique_ordered:
        unique_ordered.append(i)
print(unique_ordered)