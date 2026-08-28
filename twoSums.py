# dua jumlah

nums = [2, 7, 11, 15]
target = 9

# Output:
# [0, 1]

for i in range(len(nums)):
    if nums[i] < target:
        jumlah = target - nums[i]
        if jumlah in nums:
            index_angka = nums.index(jumlah)
            print([i, index_angka])
            break